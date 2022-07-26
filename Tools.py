import os
import pandas as pd

from os import path

def create_folder(output_folder):

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	return output_folder

def binary_search(ranges, item, k):
	
	low = 0
	high = len(ranges[k]) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = ranges[k][mid]
		if item in range(guess[0], guess[1]+1):
			return True, guess
		elif guess[0] > item:
			high = mid - 1
		else:
			low = mid + 1
	return False, None

def extract_ranges(df):
	
	ranges = {"chr1":[], "chr2":[], "chr3":[], "chr4":[], "chr5":[], "chr6":[], 
		"chr7":[], "chr8":[], "chr9":[], "chr10":[], "chr11":[], "chr12":[], 
		"chr13":[], "chr14":[], "chr15":[], "chr16":[], "chr17":[], "chr18":[], 
		"chr19":[], "chr20":[], "chr21":[], "chr22":[], "chrX":[], "chrY":[]}

	for i in df.index:
		chr_ = df.at[i, "Chr"]

		if chr_ in ranges.keys():
			start_pos = df.at[i, "Start"]
			end_pos = df.at[i, "End"]
			ranges[chr_].append([start_pos, end_pos])

	for k in ranges.keys():
		ranges[k].sort(key=lambda x:x[-1])

	return ranges

def extract_ranges_stranded(df):
	
	ranges = {"chr1":[], "chr2":[], "chr3":[], "chr4":[], "chr5":[], "chr6":[], 
		"chr7":[], "chr8":[], "chr9":[], "chr10":[], "chr11":[], "chr12":[], 
		"chr13":[], "chr14":[], "chr15":[], "chr16":[], "chr17":[], "chr18":[], 
		"chr19":[], "chr20":[], "chr21":[], "chr22":[], "chrX":[], "chrY":[]}

	for i in df.index:
		chr_ = df.at[i, "Chr"]

		if chr_ in ranges.keys():
			start_pos = df.at[i, "Start"]
			end_pos = df.at[i, "End"]
			strand = df.at[i, "Strand"]
			ranges[chr_].append([start_pos, end_pos, strand])

	for k in ranges.keys():
		ranges[k].sort(key=lambda x:x[1])

	return ranges

def remove_overlaps(ranges):
	
	for k in ranges.keys():
		i = 0
		while i < len(ranges[k]) - 1:
			if min(ranges[k][i][1], ranges[k][i + 1][1]) \
			>= max(ranges[k][i][0], ranges[k][i + 1][0]):
				ranges[k][i] = [
					min(ranges[k][i][0], ranges[k][i + 1][0]), 
					max(ranges[k][i][1], ranges[k][i + 1][1])]
				ranges[k].pop(i + 1)
			else:
				i += 1
	return ranges