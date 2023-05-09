import math

def Direction():
	numText = input("Give me a list of integers: ").strip()
	numList = numText.split(",")

	print("Greatest: " + str(fGreat(numList)))
	print("Lowest: " + str(fLow(numList)))
	print("Mean: " + str(fMean(numList)))
	print("Median: " + str(fMedian(numList)))
	print("Lowest To Greatest: " + ','.join(fSort(numList, 0)))
	print("Greatest To Lowest: " + ','.join(fSort(numList, 1)))

	input("Press Enter to close.")


def fGreat(nList): # Find the greatest number in the list
	biggest = nList[0]
	for i in nList:
		if i > biggest:
			biggest = i
	return biggest

def fLow(nList): # Find the lowest number in the list
	lowest = nList[0]
	for i in nList:
		if i < lowest:
			lowest = i
	return lowest

def fMean(nList):
	total = 0
	for i in nList:
		total += int(i)
	total = (total / len(nList))
	return total

def fMedian(nList):
	nLen = len(nList) # Get length of list

	if (nLen % 2) != 0:
		nMid = (nLen / 2) # Middle Number In List
		nTotal = nList[int(nMid)]
		return nTotal
	else:
		nMid = (nLen / 2) # Middle Number In List
		nMid1 = (round(nMid) - 1) # Get Middle Left
		nBreak = (int(nList[int(nMid)]) + int(nList[int(nMid1)]))
		nTotal = (nBreak / 2)
		return nTotal

def fSort(nList, sortMethod):
	if sortMethod == 0:
		for number in range(len(nList) - 1):
			for j in range(len(nList) - 1 - number):
				if nList[j] > nList[j+1]:
					nList[j], nList[j+1] = nList[j+1], nList[j]
		return nList
	elif sortMethod == 1:
		for number in range(len(nList) - 1):
			for j in range(len(nList) - 1 - number):
				if nList[j] < nList[j+1]:
					nList[j], nList[j+1] = nList[j+1], nList[j]
		return nList
	else:
		return "[Error] Sort Method False"

if __name__ == "__main__":
	Direction()