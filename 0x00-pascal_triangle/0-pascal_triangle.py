#!/usr/bin/env python3

"""a function to create pascal's triangle"""

def pascal_triangle(n):

	elist=[]
	
	if n <= 0:
		return []
	else:
		for i in range(n):
			temp_list = []
			for j in range(i+1):
				if j==0 or j==i:
					temp_list.append(1)
				else:
					temp_list.append(elist[i-1][j-1] + elist[i-1][j])
			elist.append(temp_list)

		for x in elist:
			print("[{}]".format(",".join([str(x) for x in row])))
