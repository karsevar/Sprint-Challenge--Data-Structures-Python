import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# For my machine this naive solution runs at 9.84 seconds. The 
# following solution can be described as a O(n * m) solution because of 
# the nested for loops and that in the worst case the algorithm will 
# have to look through the length of each array to find a match 
# or not find a match. The formal run time complexity of this algorithm 
# can be defined as 0(n^2) since both names_1 and names_2 are fairly similar 
# and have similar length.

# The O(n log(n)) solution for this problem would be using a binary tree 
# in place of the nested for loops. Though in the worst case this solution 
# will have a time complexity of O(n * n) since it's efficiency is dependent on 
# how balanced the binary tree is (namely the value of the root node).

# first build out a binary search tree with the methods contains and 
# insert.

class BinarySearchTree:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value) 
        else:
            if self.right is None:
                self.right = BinarySearchTree(value) 
            else: 
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True 
        else:
            if target < self.value:
                if self.left is None:
                    return False 
                else:
                    return self.left.contains(target) 
            else:
                if self.right is None:
                    return False 
                else:
                    return self.right.contains(target)

# first initialize the BinarySearchTree with the first value in 
# either name_1 or name_2 

# write a for loop that will populate the names within the binary search 
# tree structure.

name_tree = BinarySearchTree(names_1[0])
for name in range(1, len(names_1)):
    name_tree.insert(names_1[name])

# write an additional for loop that will loop through the names in 
# names_2 and check if there are any matches in the binary tree 
    # if name_tree.contains(name) returns True 
        # append the name in duplicates
    # else do nothing 

# This solution decreased the search time from 9.84 seconds to only 
# 0.197 which means that this solution is exponentially better than 
# the naive solution.
 
for name in names_2:
    if name_tree.contains(name) == True:
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
