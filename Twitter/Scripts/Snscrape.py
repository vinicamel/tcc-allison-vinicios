import snscrape.modules.twitter as sntwitter
import pandas as pd
from unidecode import unidecode

attributes_container = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('política Brasil lang:pt').get_items()):
    if i>1000:
        break
    clean_content = unidecode(tweet.rawContent)
    attributes_container.append([clean_content])
    
tweets_df = pd.DataFrame(attributes_container, columns=["Tweets"])

tweets_json = tweets_df.to_json(orient='records')

with open('tweets500.json', 'w') as file:
    file.write(tweets_json)