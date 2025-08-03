import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS videos(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
time TEXT NOT NULL
)''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()

    if not rows:
        print("empty")
    else:
        for row in rows:
            print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) values(?,?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?", (video_id, new_name, new_time))
    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1.List Videos")
        print("2.Add Video")
        print("3.Update Video")
        print("4.Delete Video")
        print("5.Exit App")
        choice = input("Enter your choice : ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name : ")
                time = input("Enter the video time : ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video ID to update : ")
                new_name = input("Enter the video name : ")
                new_time = input("Enter the video time : ")
                update_video(video_id, new_name, new_time)
            case '4':
                video_id = input("Enter the video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")
    conn.close()

if __name__ == "__main__":
    main()