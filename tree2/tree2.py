# What does a tree look like?
# [ Node, [ Left ], [ Right ] ]
		
class BinTree:
	def __init__(self):
		self.tree = self.createTree()
		
	def create_tree(self):
		return [];
	
	def get_node(self, tree):
		return tree[0]
		
	def set_node(self, tree, el):
		tree[0] = el
	
	def set_left_element(self, tree, el):
		if (len(tree) < 1):
			tree[1] = self.create_tree()
			
		tree[1][0] = el
			
		return tree
		
	def get_left_element(self, tree):
		if (len(tree) > 1):
			return tree[1][0]
		return None
		
	def set_right_element(self, tree, el):
		if (len(tree) < 2):
			tree[2] = self.create_tree()
		tree[2][0] = el
	
	def get_right_element(self, tree):
		if (len(tree) > 2):
			return tree[2][0]
		return None
		
	def destroy_tree(self):
		self.tree = createTree();
	
	def is_empty(self, tree):
		return len(tree) < 1
	
	def is_full(self, tree):
		return False 
		
	def size(self, tree):
		# Must walk the tree and count
		count = 0;
		
		# Count the direct child nodes here
		count += len(tree)
		
		# Get the counts of all left children
		left = self.get_left_element(tree)
		if (left <> None):
			 count += self.size(left)
			 
		# Get the counts of all right children
		right = self.get_right_element(tree)
		if (right <> None):
			count += self.size(right)
			
		return count
	
	def find_element_by_key(self, tree, key):
		if (self.size(tree) == 0):
			return None		
		
		if (node.key == key):
			return node
		
		left = self.get_left_element(tree)
		if (left <> None):
			return self.find_element_by_key(left, key)
		
		right = self.get_right_element(tree)
		if (right <> None):
			return self.find_element_by_key(right, key)
			
		return None
		
	def insert_element(self, tree, el):
		if (self.is_empty(tree)):
			self.set_node(tree, el)
		
		root = self.get_node(tree)
		cmp = root.compare(el)
		if (cmp == 1) :
			return self.insert_element(self.get_left_element(root), el)
		elif (cmp == -1) :
			return 	self.insert_element(self.get_right_element(root), el)
		else :
			# Could raise a duplicate key error, but let's silently ignore
			pass
		
		return tree	
		
	def delete_element(self, tree, el):
		if (self.is_empty(tree)):
			return None
		
		root = self.get_node(tree)
		cmp = root.compare(el)
		
		if (cmp == 0):
			return self.delete_node(root)
			
		if (cmp == 1):
			return self.delete_element(self.get_left_element(root), el)
		
		if (cmp == -1):
			return self.delete_element(self.get_right_element(root), el)	
			
		return None

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
		
		# No children
		if (self.size(tree) == 1):
			tree.pop();
			return tree;
			
		left = self.get_left_element(tree)
		right = self.get_right_element(tree)
		
		# Only one child	
		if (left == None or right == None):
			if (left) :
				self.set_node(tree, left)
				return tree
			else :
				self.set_node(tree, right)
				return tree
				
		# Two children
		# Replace target node with the node with largest value on the Left side
		# which is then removed
		node = self.pop_max_node(self.get_left_element(tree))
		self.set_node(node)	
	
	def pop_max_node(self, tree):
		if (self.size(tree) == 0):
			return
		
		right = self.get_right_element(tree)
		if (self.size(right) == 1):
			tree.pop()
			return right
		else:
			return self.pop_max_node(self.get_right_element(tree))
		
