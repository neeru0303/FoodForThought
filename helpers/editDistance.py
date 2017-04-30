import sys
def editDistance(str1,str2,m,n):
	if len(str1)==0:
		return len(str2)
	if len(str2)==0:
		return len(str1)
	if str1[m-1]==str2[n-1]:
		return editDistance(str1[:m-1],str2[:n-1],m-1,n-1)
	else: 
		return 1+ min(editDistance(str1[:m],str2[:n-1],m,n-1),
					editDistance(str1[:m-1],str2[:n-1],m-1,n-1),
					editDistance(str1[:m-1],str2[:n],m-1,n),
					)

str1 = sys.argv[1]
str2 = sys.argv[2]

print editDistance(str1,str2,len(str1),len(str2))