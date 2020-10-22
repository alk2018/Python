#Albert Kodus
#G01139458
#akodua
#218

import sys

import math

from collections import Counter;

def counts(xs):
	#creates the sequence and uses
	#the count method to count the duplicates.
	sq = {}
	for num in xs:
		sq[num] = xs.count(num)
	return sq
	
def weeklies(plants_d):
	weekly = []
	
	for key in plants_d:
		if (plants_d[key] == 'weekly'):
			list = weekly.append(key)
	
	return sorted(weekly)

def closest(d, what, here):

    num = 0

    for index in d:
        if d[index] == what:

            num = 1

    if num == 0:
        return None

    closest = sys.float_info.max


    for index in d:
        if d[index] == what:

            dist_spot = math.sqrt( (index[0]-here[0])*(index[0]-here[0]) + (index[1]-here[1])*(index[1]-here[1]))


            if dist_spot < closest:

                closest = dist_spot

                coordinates = index
		
    return coordinates

def file_counts(filename):
    freq = Counter();
    for line in open (filename, 'r'):
        for word in line.split():
            freq[word] += 1
    freq = {int(k):int(v) for k,v in freq.items()}
    return freq