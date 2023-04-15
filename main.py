from Webtoon import getWebtoon, readWebtoonData
# from Line import sendNotify

# getWebtoon()

# is_newEpisode, episodeDetail = readWebtoonData()

is_newEpisode, episodeDetail = readWebtoonData( getWebtoon() )

# If Webtoon new episode arrived!, send Line notify
# if is_newEpisode:

#     service         = episodeDetail['service']
#     episodeCount    = episodeDetail['episodeCount']
#     episodeName     = episodeDetail['episodeName']

#     sendNotify(
#         message=f'@{service} New episode!\n\n✨{episodeName}'
#     )