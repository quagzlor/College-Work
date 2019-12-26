import math
import mmh3
from bitarray import bitarray

#Done by Divij and Jyotica
#Used https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/ as a guide
 
class BloomFilter(object):
 
    def __init__(self, items_count,fp_prob):

        # Intended probability in decimal for the calculations
        self.fp_prob = fp_prob
 
        # Size of bit array
        self.size = self.get_size(items_count,fp_prob)
 
        # Number of hash functions
        self.hash_count = self.get_hash_count(self.size,items_count)
 
        # Bit array of given size
        self.bit_array = bitarray(self.size)
 
        # iSet bitarray to 0
        self.bit_array.setall(0)
 
    def add(self, item):
        #function to add an item to filter
        digests = []
        for i in range(self.hash_count):
            # 'i' works as a seed for the hash function
            
            digest = mmh3.hash(item,i) % self.size
            digests.append(digest)
 
            # Set the bit True in bit_array
            self.bit_array[digest] = True
 
    def check(self, item):
        
        #Check for existence of an item in filter
        
        for i in range(self.hash_count):
            digest = mmh3.hash(item,i) % self.size
            if self.bit_array[digest] == False:
 
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return "Not present"
        return "Probably present"
 
    @classmethod
    def get_size(self,n,p):
        # m = -(n * lg(p)) / (lg(2)^2)
        #Uses above to get the size of the bitarray
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
 
    @classmethod
    def get_hash_count(self, m, n):
        # k = (m/n) * lg(2)
        # Uses the above to get optimum number of hashes

        k = (m/n) * math.log(2)
        return int(k)
