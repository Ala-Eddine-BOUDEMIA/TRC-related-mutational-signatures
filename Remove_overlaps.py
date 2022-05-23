def remove_overlaps(ranges):
	
	for s in ranges.keys():	
		for k in ranges[s].keys():
			i = 0
			while i < len(ranges[s][k]) - 1:
				if min(ranges[s][k][i][1], ranges[s][k][i + 1][1]) \
				>= max(ranges[s][k][i][0], ranges[s][k][i + 1][0]):
					ranges[s][k][i] = [
						min(ranges[s][k][i][0], ranges[s][k][i + 1][0]), 
						max(ranges[s][k][i][1], ranges[s][k][i + 1][1])]
					ranges[s][k].pop(i + 1)
				else:
					i += 1
	return ranges