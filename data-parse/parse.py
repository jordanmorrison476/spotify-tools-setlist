import json 
from extract import json_extract
''' To-Do: import all of your playlists into seperate JSON files manually and conc into a longer dict '''
# Opening JSON file 
f = open('C:/Users/Jorda/Desktop/Python/Learning Basics - Delete Spotify Playlists/data-parse/jordanPlaylists2020.json')
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
  
# Closing file 
f.close()

# Find every instance of `name` in a Python dictionary.
items = json_extract(data, 'uri')
playlistNames = json_extract(data, 'name')

playlistURls = items[1::2]  # Get every even-index value from a list
userProfileURLs = items[2::1]  # Get every odd-index value from a list

''' what are you trying to do here? '''
''' get all playlistURIs where name of playlist = My Setlist  '''

inputPlaylistName = input("Enter Playlist Name: ")

upprBound = len(playlistURls)

arr = []

for x in range(0, upprBound):
    arr.append({"name": playlistNames[x], "value" : playlistURls[x]})
    
for x in arr:
    if x["name"] == inputPlaylistName:
        chosenToDeletev1 = x["value"]
        y = chosenToDeletev1.split(":")
        print(y[2])
 
''' another problem... '''
''' Spotify doesn't let you bulk unfollow playlists using their web console ffs '''
''' Now import a Spotipy library to handle auth '''
''' declare a const array of playlists I want to keep '''
''' find all playlistUris where playlist name is not in the saved playlists array '''
''' iterate over all unwanted playists and unfollow each playlist individually ''' 
''' Show a deleteUnwantedPlaylist confirmation message '''