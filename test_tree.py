from tree2.TreeElement import TreeElement
from tree2.BinTree import BinTree
import string
from pprint import pprint

data = [ 100, 50, 150, 25, 10, 200, 300 ];

print("Creating a tree of these values: ", 
	   ",".join(map(str,data)))

T = BinTree()
for i in data:
	el = TreeElement(i, "payload-" + str(i))
	T.insert_element(T.tree, el)
	
print("Tree after inserts")
print(str(T))

el = TreeElement(25, "payload-" + str(25))

print("Deleting node " + str(el))
T.delete_element(T.tree, el)
print("Tree after delete")
print(str(T))


el = TreeElement(150, "payload-" + str(150))

print("Deleting node " + str(el))
T.delete_element(T.tree, el)
print("Tree after delete")
print(str(T))

vals = T.depth_traversal(T.tree)
print("Values in Depth Traversal: " + (",".join(map(str, vals))) + "\n")
# pprint(vals)

vals = T.breadth_traversal(T.tree)
print("Values in Breadth Traversal: " + (",".join(map(str, vals))) + "\n")
# pprint(vals)

