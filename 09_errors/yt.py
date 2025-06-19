import json


def add_video(videos):
    name = input("Enter the name of video:\n")
    duration = input("Enter the duration of video:\n")
    videos.append({'name':name,'duration':duration})
    save_data_helper(videos)


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    enumerate_test = enumerate(videos, start=1)
    print("Enumerate object:", list(enumerate_test))
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name:{video['name']}, Duration: {video['duration']}")
    print("\n")
    print("*" * 70)

#  Response comes in  aformat of array/list
# Enumerate object: [
# (1, {'name': 'test', 'duration': '1o mins'}),
# (2, {'name': 'testtwo', 'duration': '4omins'})
#]



def update_video(videos):
    list_all_videos(videos)
    index = int(input("The index of the video you want to update:"))
    
    if 1 <= index <= len(videos):
        name = input("Enter the name of video:\n")
        duration = input("Enter the duration of video:\n")
        videos[index - 1] = {'name':name,'duration':duration}
        save_data_helper(videos)
    else:
        print("Invalid input ⁉️")




def delete_video(videos):
    list_all_videos(videos)
    index = int(input("The index of the video you want to delete:"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid input ⁉️")


def main():
    while True:
        videos = load_data()
        print("Yt Manager | Choose an option")
        print("1. List all the yt videos")
        print("2. Add a yt video")
        print("3. Update a yt video details")
        print("4. Delete a yt video")
        print("5. Exit the app")

        choice = input("Enter a choice:\n")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid input ⁉️")
            

if __name__ == "__main__":
    main()


