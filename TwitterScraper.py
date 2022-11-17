''' Gary Schmidt :: Econ 151 :: Customizable Twitter Scraper :: This is my implementation of a basic 
script for scraping a custom queried set of tweets from Twitter, navigating around the potential challenges 
the Twitter API poses, particular when it pertains to finding historical data of tweets. The backbone of this algorithm
is learned from youtuber AI Spectrum, though there are future customizations I plan on implementing that will add 
ease of use for exporting the data and subsequently conducting easier sentiment analysis and from there 
data visulization. The algorithm relies primarily upon the package snscrape which is used to access this information
from twitter and then briefly uses the package panda in order to neatly package everything into a dataframe. '''

import csv
import math
import pandas as pd
import snscrape.modules.twitter as sntwitter



def main():


	#This is the important line in running the program -- best usage is to conduct whatever advanced search
	#you deserve in twitter and from there copy in the line of code that you plan on using. Use single 
	#quotation marks to avoid text parsing issues as twitter will use double quations
	
	#query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"

	query = '("ulvade" OR "ulvade OR shooting") (#ulvade) until:2022-05-31 since:2022-05-24'

	tweets = []

	#amount of tweets that you want to pull
	limits = 1000

	for tweet in sntwitter.TwitterSearchScraper(query).get_items():

		if len(tweets) == limits:
			break	
		else: 
			tweets.append([tweet.date, tweet.user.username, tweet.content])

	df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
		
	
	#use this line when you are desiring to just test the data pulling
	#print(df)

	#this line determines where you want the dataframe to save to -- make sure to change name
	df.to_csv(r'/Users/garyschmidt/Desktop/econ151data/Ulvade_Data.csv', index=False)


if __name__ == "__main__":
	main()