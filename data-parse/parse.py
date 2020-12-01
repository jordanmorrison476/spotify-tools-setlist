# Python program to read 
# json file 
  
  
import json 
from extract import json_extract
  
# Opening JSON file 
f = open('C:/Users/Jorda/Desktop/Python/Learning Basics - Delete Spotify Playlists/jordanPlaylists2020.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
  
# Closing file 
f.close()

data

#print(data)

# Find every instance of `name` in a Python dictionary.
items = json_extract(data, 'uri')

items

# print(items)

playlistURls = items[1::2]  # Get every even-index value from a list
userProfileURLs = items[2::1]  # Get every odd-index value from a list

print('Playlists URLS = ', playlistURls)

''' now that you have all of your playlist urls in one nice array, delete the unwanted ones from Spotify programatically using the api '''
''' how do you know which playlists to delete hmmmmm? '''
''' either use a UI to group select playlists or some other way.... '''














# str_playlist_DICTIONARY = json.dumps(data, indent=2)

# #print(playlist_DICTIONARY)

# # Iterating through the json 
# # list 

# playlistItems_LIST = []

# for i in data['items']: 
#     playlistItems_LIST.append(i)

# # print(playlist_DICTIONARY)










# # using json.loads() 
# # convert dictionary string to dictionary 
# res = json.loads(str_playlist_DICTIONARY) 
  
# # print result 
# # print("The converted dictionary : " + str(res)) 

# # Find every instance of `name` in a Python dictionary.
# items = json_extract(str_playlist_DICTIONARY.json(), 'items')
# print(items)




