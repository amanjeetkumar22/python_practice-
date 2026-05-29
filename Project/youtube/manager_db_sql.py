import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute(''' 
       CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

''')

def list_videos():
    print("-"*60)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():## fetchall is a method 
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    con.commit()

def update_videos(id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(new_name,new_time,id))
    con.commit()
    
def delete_videos(id):
    cursor.execute("DELETE FROM videos where id = ? ",(id,)) ## when u enetered a value then write in the form of tuple (' ',)
    con.commit()
def main():
    while True:
        print("\n Youtube Manager app With DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update videos")
        print("4. Delet video")
        print("5. Exit App ")
        choice = input("Enter your choice:")

        if choice =='1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name,time)
        elif choice == '3':
            id = input("Enter video id to update : ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(id,name,time)
        elif choice == '4':
            id = input("Enter video id to delet: ")
            delete_videos(id)
        elif choice == '5':
            break

        else:
            print("Invalid choice")

    con.close()
if __name__ == "__main__":
    main()