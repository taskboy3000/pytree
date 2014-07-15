# Binary Search Tree operations
# Joe Johnston <jjohn@taskboy.com>
#
# What does a tree look like?
# [ Node, [ Left ], [ Right ] ]
from tree2.TreeElement import TreeElement

class BinTree:
	def __init__(self):
		self.tree = self.create_tree()
		
	def create_tree(self):
		return [];
	
	def get_node(self, tree):
		return tree[0]
		
	def set_node(self, tree, el):
		if (len(tree) == 0):
			tree.append(el)
		else:
			tree[0] = el
	
	def set_left_element(self, tree, el):
		if (len(tree) < 1):
			tree[1] = self.create_tree()
			
		tree[1][0] = el
			
		return tree
		
	def get_left(self, tree):
		if (len(tree) > 1):
			return tree[1]
		return None
		
	def set_left(self, parent, tree):	
		if (parent != None):
			parent[1] = tree
		
	def set_right_element(self, tree, el):
		if (tree != None and len(tree) < 2):
			tree[2] = self.create_tree()
		tree[2][0] = el
	
	def get_right(self, tree):
		if (tree != None and len(tree) > 2):
			return tree[2]
		return None
		
	def set_right(self, parent, tree):
		if (parent != None):
			parent[2] = tree
		
	def destroy_tree(self):
		self.tree = createTree();
	
	def is_empty(self, tree):
		if tree == None:
			return True 
		return len(tree) < 1
	
	def is_full(self, tree):
		return False 
		
	def size(self, tree):
		# Must walk the tree and count
		count = 0;
		
		if (tree == None):
			return 0
			
		# Count the direct child nodes here	
		count += len(tree)
		
		# Get the counts of all left children
		left = self.get_left(tree)
		if (left != None):
			 count += self.size(left)
			 
		# Get the counts of all right children
		right = self.get_right(tree)
		if (right != None):
			count += self.size(right)
			
		return count
	
	def find_element_by_key(self, tree, key):
		if (self.size(tree) == 0):
			return None		
		
		if (node.key == key):
			return node
		
		left = self.get_left(tree)
		if (left != None):
			return self.find_element_by_key(left, key)
		
		right = self.get_right(tree)
		if (right != None):
			return self.find_element_by_key(right, key)
			
		return None
		
	def insert_element(self, tree, el):
		if (tree == None):
			self.tree = self.create_tree()
			
		if (self.size(tree) == 0):
			self.set_node(tree, el)
			tree.append([]) # Left child
			tree.append([]) # Right child
			return tree
			
		root = self.get_node(tree)
		cmp = root.compare(el)
		
		if (cmp == 1) :
			tree[1] = self.insert_element(self.get_left(tree), el)
		elif (cmp == -1) :
			tree[2] = self.insert_element(self.get_right(tree), el)
		else :
			# Could raise a duplicate key error, but let's silently ignore
			pass
		
		return tree	
		
	def delete_element(self, tree, el):
		if (tree == None):
			return None
			
		if (self.is_empty(tree)):
			return None
		
		root = self.get_node(tree)
		cmp = root.compare(el)
		
		if (cmp == 0):
			return self.delete_node(tree)
			
		if (cmp == 1):
			new_tree = self.delete_element(self.get_left(tree), el)
			self.set_left(tree, new_tree)
		
		if (cmp == -1):
			new_tree = self.delete_element(self.get_right(tree), el)	
			self.set_right(tree, new_tree)
			
		return tree

# Visualizing delete_node:
#   Given this tree:
#    [ 
#	   node100, 
#	       [ node50, 
#			  [ node30,
# 				[ node10,
#					[ node20,
#                       [ node25 ]
#                   ],
#               ],
#				[ node40,
#                    [ node45 ]			  
#			    ]
#			  [ node80,
#				 [ node70,
#				 	[ node60 ],
#				 ],
#				 [ node90 ]
#			  ]			
#		   ], 
#		   [ node200,
#				[ node150 ],
#				[ node300 ],
# 		   ],
#	 ]
					
	def delete_node(self, tree):
		if (self.is_empty(tree)):
			return
		
		#print("Delete_node tree:\n" + self.repr_tree(tree) + "\n")
		
		# No children
		if (self.size(tree) == 1):
			tree.pop();
			return tree;
			
		left = self.get_left(tree)
		right = self.get_right(tree)
		
		# Only one child	
		if (self.size(left) == 0 or self.size(right) == 0):
			if (left) :
				#print("Replacing with " + self.repr_tree(left) + "\n")
				tree[0], tree[1], tree[2] = left[0], left[1], left[2]
				return tree
			else :
				#print("Replacing with " + self.repr_tree(right) + "\n")
				tree[0], tree[1], tree[2] = right[0], right[1], right[2]
				# self.set_node(tree, right)
				return tree
				
		# Two children
		# Replace target node with the node with largest value on the Left side
		# which is then removed
		node = self.pop_max_node(self.get_left(tree))
		if (node != None):
			self.set_node(node)	
		else:
			print("WARN: No replacement node found\n")
	
	def pop_max_node(self, tree):
		if (tree == None):
			return;
			
		if (self.size(tree) == 0):
			return
		
		right = self.get_right(tree)
		if (self.size(right) == 1):
			victim = tree.pop()
			#print("Removing " + str(victim) + "\n")
			#print("Returning " + str(right) + "\n")
			return right
		else:
			return self.pop_max_node(self.get_right(tree))
	
	def breadth_traversal(self, tree):
		if (tree == None):
			return;
			
		if (self.size(tree) == 0):
			return;
			
		visit = [ tree ]
		values = [];
		
		while True:
			if (len(visit) == 0):
				break
				
			this_tree = visit.pop(0)
			root = self.get_node(this_tree)
			values.append(root.value)
			
			left = self.get_left(this_tree)
			right = self.get_right(this_tree)

			if (self.size(left) > 0):
				visit.append(left)

			if (self.size(right) > 0):
				visit.append(right)						
			
		return values 			
		
	def depth_traversal(self, tree):
		if (tree == None):
			return
			
		vals = []
		for n in tree:
			if (isinstance(n, TreeElement)):
				vals.append(n.value)
				
		left = self.get_left(tree)
		right = self.get_right(tree)
		
		if (self.size(left) > 0):
			for i in self.depth_traversal(left):
				vals.append(i)
			
		if (self.size(right) > 0):
			for i in self.depth_traversal(right):
				vals.append(i)
				
		return vals
								
			
	def repr_tree(self, tree, level=0):
	
		if (tree == None):
			return "";
			
		s = "" 
		
		if (len(tree) > 0 and tree[0] != None):
			# s = "Level: " + str(level) + " "
			s = s + (" " * level)
			s = s + "[" + str(tree[0]) + "," + "\n"
			
		if (len(tree) > 1 and tree[1] != None):
			l = self.repr_tree(tree[1], level + 2)
			if (l):
				s = s +  l 
			else:
				s = s + (" " * (level + 1)) + "L:NIL,\n"

		if (len(tree) and tree[2] != None):
			r = self.repr_tree(tree[2], level + 2) 
			if (r):
				s = s  + r 			
			else:
				s = s + (" " * (level + 1)) + "R:NIL\n"
		
		if (len(tree) and tree[0] != None):
			s = s + (" " * level) +  "],\n"
		
		return s
			
	def __str__(self):
		return self.repr_tree(self.tree)
		