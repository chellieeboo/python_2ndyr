# 1. Creating empty list
my_songs = []

# 2. Insertion
my_songs.append("Nobody Gets Me")
my_songs.append("Shakira Waka Waka")
my_songs.append("Bow the Knee")
my_songs.append("When Answers Aren't Enough")
my_songs.append("Amazing Grace")

# 3. Traversal
print("My Top 5 Favorite Songs:")

for song in my_songs:
    print(song, end=" -> ")
print("End of the playlist")

# 4. Deletion
my_songs.remove("Nobody Gets Me")

print("\nAfter Deletion:")

for song in my_songs:
    print(song, end=" -> ")
print("End of the playlist")