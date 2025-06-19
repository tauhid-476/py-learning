import sqlite3

con = sqlite3.connect("yt_vids.db")
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
 ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name, time))
    con.commit()

def update_video(id, name , time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id=?",(name, time, id))
    con.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    con.commit()



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


    con.close()

if __name__ == "__main__":
    main()


