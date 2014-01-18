# this program aims to scrap the website and find zip codes for all walmarts across USA
# with beautiful soup

import urllib2
import csv
from bs4 import BeautifulSoup

def main():
	# default list of zip codes of major american cities
	ls = ['10001', '90001', '60601', '77001', '19101','85001','92101','78201','75201','48201',
	'95101','46201','32201','94101','43201','78701','38101','21201','28201','76101'] 
	for zipCode in ls:
		lookUp(ls, zipCode)
		if len(ls)>4200:
			break
	writer = csv.writer(open("walmart.csv","wb"))
	for i in ls:
		writer.writerow([i])



def lookUp(ls, target):
	# look up store's zip codes 
	# input: ls of all zip codes that have the store, target zip code to be looked up
	# output: updated ls with new zip codes that have the store
	url = 'http://www.walmart.com/storeLocator/ca_storefinder_results.do?serviceName=&rx_title=com.wm.www.apps.storelocator.page.serviceLink.title.default&rx_dest=%2Findex.gsp&sfrecords=50&sfsearch_single_line_address='+target
	try:
		soup = BeautifulSoup(urllib2.urlopen(url).read())
	except:
		print "oops"
		return ls
	for store in soup('div', {'class': 'storeContainer'}):
		divLevelOne = store.findAll('div')
		divLevelTwo = divLevelOne[1].findAll('div')
		line = divLevelTwo[5]
		parse = line.text.split()
		zipCode = parse[len(parse)-1]
		#print zipCode
		if zipCode not in ls:
			ls.append(zipCode.encode('UTF-8'))
			print len(ls)


main()