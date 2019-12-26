from bloomfilter import BloomFilter

#File to test the bloom filter

n = 4804 #no of items to add to list. Make sure to set it properly
p = 0.1 #false positive probability
 
bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))
 
# words to be added
lines = open("test.txt").read().split('\n')
for line in lines:
    bloomf.add(line)
    
# words to check

print ("Checking for 'Up'")
print (bloomf.check("Up"))

print ("Checking for 'Itchy Butt'")
print (bloomf.check("Itchy Butt"))
