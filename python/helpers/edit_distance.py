import sys


def editDistance(str1,str,m,n):
	d = [[0 for i in range(n+1)] for j in range(m+1)]
	print m,n
	print d
	for i in range(m+1):
		d[i][0]=i
	for j in range(n+1):
		d[0][j]=j

	for i in range(m+1):
		for j in range(n+1):
			print d[i][j],i,j
			if str1[i-1]==str2[j-1] :
				d[i][j]=d[i-1][j-1]
			else:
				d[i][j]= 1 + min(d[i][j-1],d[i-1][j-1],d[i-1][j])
	return d[m][n]

"""
def editDistance(str1,str2,m,n):
	print str1,str2,m,n
	if d.get((str1,str2),None) is not None:
		return d[(str1,str2)]
	if m==0:
		d[(str1,str2)] = n
		return n
	if n==0:
		d[(str1,str2)] = m
		return m
	if str1[m-1]==str2[n-1]:
		return editDistance(str1[:m-1],str2[:n-1],m-1,n-1)
	else: 
		return 1+ min(editDistance(str1[:m],str2[:n-1],m,n-1),
					editDistance(str1[:m-1],str2[:n-1],m-1,n-1),
					editDistance(str1[:m-1],str2[:n],m-1,n),
					)

"""



str1 = sys.argv[1]
str2 = sys.argv[2]


print editDistance(str1,str2,len(str1),len(str2))