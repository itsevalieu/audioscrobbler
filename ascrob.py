import csv

user_playlist = []
def printListenersTimesPlayed(userID):
    print("Searching user's playlist...")
    print("Please be patient! I'm slow ):")
    user_playlist = getUserPlaylist(userID)
    for i in user_playlist:
        i[0] = findGoodId(i[0])
        i[0] = findArtistName(i[0])
        print(i[0], "-", i[1])

def getUserPlaylist(userID):
    with open('user_artist_data.txt', 'r') as file1:
        csv_reader = csv.reader(file1, delimiter=' ')
        for row in csv_reader:
            if row[0] == str(userID):
                user_playlist.append([int(row[1]), int(row[2])])
    return user_playlist

def findArtistName(artistID):
    with open('artist_data.txt', 'r') as file2:
        artist_reader = csv.reader(file2, delimiter='\t')
        for line in artist_reader:
            for column in line:
                if column == str(artistID):
                    return line[1]

def findGoodId(badID):
    with open('artist_alias.txt', 'r') as file3:
        reader = csv.reader(file3, delimiter='\t')
        for record in reader:
            if record[0] != str(badID):
                goodID = badID
                return goodID
            # elif not working properly, why?
            elif record[0] == str(badID):
                fixedID = int(record[1])
                return fixedID

printListenersTimesPlayed(1000002)
