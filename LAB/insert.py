# 1. Creating empty list
songs = []

# 2. Insertion
for i in range(5):
    song = input("Enter your favorite song: ")
    songs.append(song)

# 3. Traversal
print("\nMy Top 5 Favorite Songs:")

for song in songs:
    print(song, end=" -> ")

print("End of the playlist")

# 4. Deletion
delete_song = input("\nEnter a song to delete: ")
songs.remove(delete_song)

print("\nAfter Deletion:")

for song in songs:
    print(song, end=" -> ")

print("End of the playlist")``