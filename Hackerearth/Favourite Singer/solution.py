number_songs = input()
dictionary = {}

songs = input().split(" ")

for song in songs:
    if song in dictionary:
        dictionary[song] += 1
    else:
        dictionary[song] = 1

counter = 0
favourites = 0

for x in dictionary:
    if counter <= dictionary[x]:
        counter = dictionary[x]

for x in dictionary:
    if counter == dictionary[x]:
        favourites += 1

print(favourites)
