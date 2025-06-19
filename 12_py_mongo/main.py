from pymongo import MongoClient
from bson import ObjectId

db_url="mongodb+srv://lol:lol@cluster0.wrhey9d.mongodb.net/"

client = MongoClient(db_url, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)


def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_video(id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(id)},
        {"$set": {"name":name, "time":time}}
    )

def delete_video(id):
    video_collection.delete_one({
        "_id": ObjectId(id)
    })

def main():
    while True:
        print("Yt Manager with DB | Choose an option")
        print("1. List all the yt videos")
        print("2. Add a yt video")
        print("3. Update a yt video details")
        print("4. Delete a yt video")
        print("5. Exit the app")

        choice = input("Enter a choice:\n")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the name of video:\n")
            time = input("Enter the time of video:\n")
            add_video(name, time)

        elif choice == '3':
            id = input("Enter the id of the video to update:\n")
            name = input("Enter the name of video:\n")
            time = input("Enter the time of video:\n")
            update_video(id, name, time)

        elif choice == '4':
            id = input("Enter the id of the video to delete:\n")
            delete_video(id)

        elif choice == '5':
            break
        else:
            print("Invalid input ⁉️")


if __name__ == "__main__":
    main()




