from commons import makedirs

import requests
import json
import os
'''
Webtoon API of Rapid API, with this API, you can retrieve information about webtoons, episodes, and authors.
Ref: https://rapidapi.com/apidojo/api/webtoon

'''
def getWebtoon(filename='data.json'):

    url = "https://webtoon.p.rapidapi.com/canvas/episodes/list"

    querystring = {"titleNo":"36557","startIndex":"0","language":"th","pageSize":"5"}

    # Open the file containing the X-RapidAPI-Key for reading
    with open('RapidAPI-key.txt', 'r') as f:
        # Read the token from the file
        key = f.read().strip()

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "webtoon.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)

    # check if the request was successful
    if response.status_code == 200:
        # convert response to JSON object
        json_data = response.json()
        
        # write JSON data to file
        path = makedirs('temp', filename)

        with open( path, 'w') as f:
            json.dump(json_data, f)
            # print('JSON data saved to file.')
    else:
        print('Error: Failed to retrieve data.')
    
    return path


def readWebtoonData(filename='temp/data.json'):
    # open file and load JSON data
    with open(filename, 'r') as f:
        json_data = json.load(f)

    # access data inside the object
    message             = json_data['message']
    result              = message['result']
    episodeList         = result['episodeList']

    totalEpisodeCount   = episodeList['totalServiceEpisodeCount']
    # print('\ntotal episode:', totalEpisodeCount)

    lastEpisode         = episodeList['episode'][0]
    # print('\nname:', lastEpisode['episodeTitle'])
    # print('episode:', lastEpisode['episodeNo'])

    is_newEpisode, episodeDetail = False, dict()

    # Read the history JSON file
    if os.path.isfile('history.json'):

        with open('history.json', 'r') as f:
            history = json.load(f)
                
        # If New Episode arrived!
        if totalEpisodeCount != history['Webtoon']['totalServiceEpisodeCount']:
        # if history['Webtoon'] != episodeList:
            
            is_newEpisode = True

            episodeDetail['service'] = 'Webtoon'
            episodeDetail['episodeCount'] = totalEpisodeCount
            episodeDetail['episodeName'] = lastEpisode['episodeTitle']

            # Update history to current
            history['Webtoon'] = episodeList

            # Write JSON data to file
            with open( 'history.json', 'w') as f:

                json.dump(history, f)
                print('Updated history.')

            return is_newEpisode, episodeDetail
        

    else: 
        history = {
            'Webtoon': episodeList
        }
        
        # Write JSON data to file
        with open( 'history.json', 'w') as f:

            json.dump(history, f)
            print('Created history.')

    return is_newEpisode, episodeDetail