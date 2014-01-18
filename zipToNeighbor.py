# zipToNeighbor.py

# this program takes in a file of zip code, then spit out all the
# neighbor zip codes (including itself)

import csv

def main():
	fileName = raw_input("the name of the company: ")
	address = '/Users/shuanglechen/Dropbox/CS_project/winter/data/'+fileName+'_raw.csv'
	inputReader = csv.reader(open(address, 'rU'))	
	ls = []
	zipList = []
	# if input zips
	for row in inputReader:
		ls.append(row[2].strip())
	print ls

	neighborReader = csv.reader(open("neighbors.csv",'rU'))
	for row in neighborReader:
		if row[0] in ls:
			print row[0]
			print row[6]
			for zipCode in eval(row[6]):
				if zipCode not in zipList:
					zipList.append(zipCode)
	
	for zipCode in ls:
		if zipCode not in zipList:
			zipList.append(zipCode)

	address = "data/"+fileName+"_zip.csv"
	writer = csv.writer(open(address,"wb"))
	for i in zipList:
		writer.writerow([i])

main()