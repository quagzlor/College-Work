print "Enter the integer"
n=input()

print "Enter the set as a single line, separated by spaces"
xset=input().split()

xset.sort()

xrev=list(reversed(xset))

for i in range n:
	print xrev[i],
