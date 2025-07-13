import sys
import io
from contextlib import contextmanager
import instaloader
import pandas as pd
import re
import os
import time
import json
import random

@contextmanager
def suppress_hd_profile_pic_warning():
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()
    try:
        yield
    finally:
        sys.stderr.seek(0)
        lines = sys.stderr.readlines()
        for line in lines:
            if "Unable to fetch high quality profile pic: 'hd_profile_pic_url_info'" not in line:
                old_stderr.write(line)
        sys.stderr = old_stderr

def count_digits(text):
    return sum(char.isdigit() for char in text)

def extract_bio_features(bio):
    suspicious_keywords = ['dm', 'promo', 'onlyfans', 'giveaway', 'forex', 'bitcoin', 'investor', 'collab', 'cashapp', 'trader']
    contains_link = bool(re.search(r'https?://', bio))
    keyword_hits = sum(kw in bio.lower() for kw in suspicious_keywords)
    hashtags_count = bio.count('#')
    mentions_count = bio.count('@')
    emoji_present = bool(re.search(r'[^\w\s,]', bio))
    return contains_link, keyword_hits > 0, hashtags_count, mentions_count, emoji_present

# Scraper Core
def scrape_instagram_profiles(usernames, existing_usernames=set()):
    L = instaloader.Instaloader()

    scraped_data = []

    for username in usernames:
        if username in existing_usernames:
            print(f"[-] Skipped (already exists): {username}")
            continue

        with suppress_hd_profile_pic_warning():
            try:
                profile = instaloader.Profile.from_username(L.context, username)
                bio = profile.biography or ""

                contains_link, has_suspicious_keywords, hashtag_count, mention_count, has_emoji = extract_bio_features(bio)

                has_profile_pic = True
                url = profile.profile_pic_url or ""
                lowered_url = url.lower()
                if (
                    "anonymous" in lowered_url
                    or "anon" in lowered_url
                    or "default" in lowered_url
                    or ("s150x150" in lowered_url and profile.username.lower() not in lowered_url)
                ):
                    has_profile_pic = False

                data = {
                    "username": profile.username,
                    "full_name": profile.full_name,
                    "has_profile_pic": has_profile_pic,
                    "followers": profile.followers,
                    "following": profile.followees,
                    "post_count": profile.mediacount,
                    "follow_ratio": round(profile.followers / profile.followees, 2) if profile.followees != 0 else 0,
                    "bio": bio,
                    "bio_length": len(bio),
                    "contains_link": contains_link,
                    "suspicious_keywords_present": has_suspicious_keywords,
                    "hashtags_count": hashtag_count,
                    "mentions_count": mention_count,
                    "emoji_in_bio": has_emoji,
                    "external_url": profile.external_url,
                    "is_verified": profile.is_verified,
                    "digit_count_in_username": count_digits(profile.username),
                    "label": ""
                }

                scraped_data.append(data)
                print(f"[+] Scraped: {username}")

                time.sleep(random.uniform(6, 10))  # safer delay for public access

            except Exception as e:
                print(f"[!] Failed to scrape {username}: {e}")
                continue

    return pd.DataFrame(scraped_data)

# Execution
if __name__ == "__main__":
    usernames_to_scrape = [
        "shaan_sakharkar.official","aryanb1511","_nehalshaikh_15","_sarmad.sk","k._sharib_","saifsk3429","aakash_yv_","omair___mohammad___khan___10","anishhh__07","murtaza.sakarwala","md_shafe_","ll_faisalll","zaidk.han8948","abulaasqureshi","brh.k9m1l","4hmed_5hah","hanchate_sanket","haaris__jr__10","kunal0330","rxhil_77","yusufkondkari_","k_qureshi8","syed_isar","shaikhfahad14","tauheed_476","rugved_patil_14","usmani_mariyam_","kulsumsayed_","khush_itripathi03","thepersonal331","mohdsalique786","shahzan_08","par.thx03","_aphylium_un_25_","nameissuyash","purviii_shah","pathanpvt_786","rahil_d3a","cantwithibaad","ayan_hanma","wannabe_krystum","b_nooh4","dani_yal.3791","dhongreafnan","aayushhh.a","truptgaikwad"
    ]

    csv_file = "instagram_profiles_scraped.csv"

    if os.path.exists(csv_file):
        try:
            existing_df = pd.read_csv(csv_file)
            if existing_df.empty or "username" not in existing_df.columns:
                existing_df = pd.DataFrame()
                existing_usernames = set()
            else:
                existing_usernames = set(existing_df["username"].astype(str).tolist())
        except pd.errors.EmptyDataError:
            print(f"[!] {csv_file} is empty, starting fresh...")
            existing_df = pd.DataFrame()
            existing_usernames = set()
    else:
        existing_df = pd.DataFrame()
        existing_usernames = set()

    new_df = scrape_instagram_profiles(usernames_to_scrape, existing_usernames)

    if not new_df.empty:
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_csv(csv_file, index=False)
        print(f"\n Appended {len(new_df)} new entries to {csv_file}")
    else:
        print("\n No new profiles scraped!")
