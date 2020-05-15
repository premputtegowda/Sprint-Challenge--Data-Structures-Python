import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure



class BST:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
    
        if self.value is None:
            self.value = value
            print(self.value)
        elif value < self.value:

            if self.left is None:
                self.left = BST(value)
            else:
             self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if self.value == target:
            duplicates.append(target)
        if target < self.value:
            if self.left is None:
                return None
            else:
                return self.left.contains(target)
        else:
       
            if self.right is None:
                return None
            else:
                return self.right.contains(target)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
bstree = BST()

for name_1 in names_1:
    bstree.insert(name_1)

for name_2 in names_2:
    bstree.contains(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
l1= set(names_1)
l2=set(names_2)
l2.intersection_update(l1)
duplicates = list(l2)