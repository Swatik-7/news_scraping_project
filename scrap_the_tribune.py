import requests
from bs4 import BeautifulSoup
import lxml
import csv
import re
import time

def main():
	source=requests.get("https://www.tribuneindia.com/news/nation/").text
	soup=BeautifulSoup(source,'lxml')
	
	csv_file=open('the_tribune.csv','w')

	csv_writer=csv.writer(csv_file)
	csv_writer.writerow(['19/06/19','THE TRIBUNE'])
	csv_writer.writerow(['headline','details','summary','web_link'])
	
	for article in soup.find_all('div',style="margin:0 0 0 1.5%; border-top:solid 1px #ccc;"):
		heading=article.h2.a.text
		summary=article.p.text
		link=article.h2.a['href']
		print(heading)
		print(summary)
		#print(link)
		nw_link=f'https://www.tribuneindia.com{link}'
		print(nw_link)
		source1=requests.get(nw_link).text
		soup1=BeautifulSoup(source1,'lxml')
		for data in soup1.find_all('span',class_='storyText'):
			story=data.text
			story=story.strip()
			#print(story)
		time.sleep(2)
		print()
		csv_writer.writerow([heading,story,summary,nw_link])
	csv_file.close()

main()
