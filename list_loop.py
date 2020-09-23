songs = ["ROCKSTAR", "Do It", "For The Night"]
print (songs[0])
print (songs[2])

print(songs[1:3])

# update the last element
songs[2] = "ZTFO"

songs.extend(["Down", "The Baddest", "Leave me Alone"])

print(songs)

# remove element from the list

songs.remove("Do It")

animals = ["Cat", "Dog", "Bird"]

animals.append("Tiger")

print(animals[2])

del animals [0]

for animal in animals:
    print(animal)
