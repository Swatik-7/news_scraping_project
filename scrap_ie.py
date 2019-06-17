from bs4 import BeautifulSoup
import requests
import lxml
import time
import re
import csv 

def main():
	source=requests.get('https://indianexpress.com').text
	soup=BeautifulSoup(source,'lxml')

	csv_file=open('indian_exp_16_june.csv','w')

	csv_writer=csv.writer(csv_file)
	csv_writer.writerow(['heading','page_link'])

	for article in soup.find_all('a', class_=re.compile("(m-block-link__anchor)\s*(ie-event-tacking)*"),href=re.compile("(https://indianexpress.com/article/).*")):
		#print(article)
		heading=article['title']
		url=article['href']
		print(heading)
		print(url)
		time.sleep(2)
		print()		
		#line_no=line_no+1
		csv_writer.writerow([heading,url])
	csv_file.close()

main()



