print "Input your sentence"
inputword = raw_input().split
isword = []
pos = []

for (i in range len(inputword)):
	check = False
	for (j in range len(isword)):
		if inputword[i]==isword[j]:
			check=True
	if check !=True:
		isword[i]=inputword[i]
		pos[i]=[i]

for (i in range len(isword)):
	print isword[i],pos[i]
