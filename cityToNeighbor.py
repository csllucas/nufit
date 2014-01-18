# this program takes in a file of zip code or city names, then spit out all the
# neighbor zip codes (including itself)

import csv

def main():
	fileName = raw_input("the name of the company: ")
	address = '/Users/shuanglechen/Dropbox/CS_project/winter/data/'+fileName+'_raw.csv'
	inputReader = csv.reader(open(address, 'rU'))	
	ls = []
	zipList = []
	# if input city names and state
	lsState = []
	for row in inputReader:
		ls.append(row[0].strip().upper())
		lsState.append(row[1].strip())

	neighborReader = csv.reader(open("neighbors.csv",'rU'))
	for row in neighborReader:
		for i in range(len(ls)):
			if row[3] == ls[i] and row[4] == lsState[i]:
				for zipCode in eval(row[6]):
					if zipCode not in zipList:
						zipList.append(zipCode)
				if row[0] not in zipList:
					zipList.append(row[0])

	address = "data/"+fileName+"_zip.csv"
	writer = csv.writer(open(address,"wb"))
	for i in zipList:
		writer.writerow([i])

main()