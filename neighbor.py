# list all zips that are within 5mi from the target zip for every zip code in the USA


import math
import csv

def main():
	locations = getData()
	locations = calc(locations)
	writeCSV(locations)

def distance(lat1, long1, lat2, long2):
	# calculate the distance according to their latitude and longitude
	r = 3958
	pi = 3.14159265359
	dPerR = 57.29578  # Number of degrees/radian (for conversion)
	dis = r * pi * ((lat1 - lat2)**2 +
	 math.cos(lat1 / dPerR) * math.cos(lat2 / dPerR) * (long1-long2)**2)**.5/180
	return dis

def getData():
	# read in the zip code document
	# create a list of locations, 
	# each location is a list of zip, lat, long, city, state, country, 
	# and later zips within 5mi radius
	# return: the big list
	locations = []
	File = open("/Users/shuanglechen/Dropbox/CS_project/winter/ZIP_CODES.txt",'r')
	#File = open("/Users/shuanglechen/Dropbox/CS_project/winter/ts.txt",'r')
	for line in File:
		if ",,," not in line:
			loc = line.strip().split('","')
			loc[0] = loc[0][1:]
			loc[1] = float(loc[1])
			loc[2] = float(loc[2])
			loc[6] = []
			locations.append(loc)
	File.close()
	return locations

def calc(locations):
	# input: locations, the list that contains zip and all other info
	# output: updated locateions
	# calculate the distance between each location, add those within 5 miles 
	# to the list
	"""
	for i in range(len(locations)):
		for j in range(len(locations)-i-1):
			dis = distance(locations[i][1],locations[i][2],locations[i+j+1][1],locations[i+j+1][2])
			print "%s, %s, %f" % (locations[i][0],locations[j][0],dis)
			if dis < 5.0:
				locations[i][6].append(locations[j][0])
				locations[j][6].append(locations[i][0])
	"""
	for loc in locations:
		for comp in locations:
			if loc[0] != comp[0]:
				dis = distance(loc[1],loc[2],comp[1],comp[2])
				if dis < 5.0:
					loc[6].append(comp[0])
	return locations

def write(locations):
	# take the updated location file and output it to a new text file: result
	File = open("/Users/shuanglechen/Dropbox/CS_project/winter/result.txt",'w')
	for i in range(len(locations)):
		File.write(locations[i][0])
		File.write(", ")
		File.write(str(locations[i][1]))
		File.write(", ")
		File.write(str(locations[i][2]))
		File.write(", ")
		File.write((locations[i][3]))
		File.write(", ")
		File.write(locations[i][4])
		File.write(", ")
		File.write(locations[i][5])
		File.write(", ")
		File.write(str(locations[i][6]))
		File.write("\n")

def writeCSV(locations):
	num=0
	writer = csv.writer(open("neighbors.csv","wb"))
	for loc in locations:
		writer.writerow([loc[0]]+[loc[1]]+[loc[2]]+[loc[3]]+[loc[4]]+[loc[5]]+[loc[6]])
		num=num+1
		print num
main()