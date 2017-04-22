class BST:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if not self.left and not self.right:  # leaf node
            return str(self.data)
        else:
            left_str = str(self.left) if self.left else "_"
            right_str = str(self.right) if self.right else "_"
            return "(" + left_str + " " + str(self.data) + " " + right_str + ")"

    # Inserts a new leaf node containing x as its data into this BST
    # Note: If the BST already contains x, do nothing
    def insert(self, x):
        if self.data < x:
            if not self.right:
                self.right = BST(x)
            else:
                self.right.insert(x)
        elif self.data > x:
            if not self.left:
                self.left = BST(x)
            else:
                self.left.insert(x)
        else:
            print 'equal'


test_bst = BST(8,
               BST(3,
                   BST(1),
                   BST(6,
                       BST(4),
                       BST(7))),
               BST(10,
                   None,
                   BST(14,
                       BST(13),
                       None)))

print "test_bst = " + str(test_bst)
# test_bst = ((1 3 (4 6 7)) 8 (_ 10 (13 14 _)))

test_bst.insert(9)
print "test_bst after insert(9) = " + str(test_bst)
# test_bst after insert(9) = ((1 3 (4 6 7)) 8 (9 10 (13 14 _)))

test_bst.insert(6)
print "test_bst after insert(6) = " + str(test_bst)
# test_bst after insert(6) = ((1 3 (4 6 7)) 8 (9 10 (13 14 _)))

test_bst.insert(0)
print "test_bst after insert(0) = " + str(test_bst)
# test_bst after insert(0) = (((0 1 _) 3 (4 6 7)) 8 (9 10 (13 14 _)))
