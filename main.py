import math, queue
from collections import Counter

class TreeNode(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def __lt__(self, other):
        return (self.data < other.data)

    def children(self):
        return ((self.left, self.right))


def get_frequencies(fname):
    f = open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return (dict(C.most_common()))

#TODO
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    for c in f.keys():
        p.put(TreeNode(None, None, (f[c], c)))
    while (p.qsize() > 1):
        a = p.get()
        b = p.get()
        c = a.data[0] + b.data[0]
        p.put(TreeNode(a, b, (c, "")))
    # return root of the tree
    return p.get()

  
#TODO
def get_code(node, prefix="", code={}):
  
  if node.left is not None:
    pre_l = prefix + '0'
    get_code(node.left, pre_l)
    
  if node.right is not None:
    pre_r = prefix + '1'
    get_code(node.right, pre_r)

  if node.right is None and node.left is None:
    code[node.data[1]] = prefix
  return code


#TODO
def fixed_length_cost(f):
    a = get_frequencies(f)
    len_a = len(a.keys())
    c_char = math.ceil(math.log2(len_a))
    return c_char * sum(a.values())

  
#TODO
def huffman_cost(C, f):
    h_cost = 0
    for character in f:
      b_len = len(C[character])
      freq = f[character] 
      
      h_cost = h_cost + (b_len * freq)
    return h_cost

#alice29.txt
f = get_frequencies('alice29.txt')
print(f)
print("Fixed-length cost:  %d" % fixed_length_cost('alice29.txt'))
T = make_huffman_tree(f)
C = get_code(T)
print(C)
print("Huffman cost:  %d" % huffman_cost(C, f))


"""
#asyoulik.txt
f = get_frequencies('asyoulik.txt')
print(f)
print("Fixed-length cost:  %d" % fixed_length_cost('asyoulik.txt'))
T = make_huffman_tree(f)
C = get_code(T)
print(C)
print("Huffman cost:  %d" % huffman_cost(C, f))
"""

"""
#f1.txt
f = get_frequencies('f1.txt')
print(f)
print("Fixed-length cost:  %d" % fixed_length_cost('f1.txt'))
T = make_huffman_tree(f)
C = get_code(T)
print(C)
print("Huffman cost:  %d" % huffman_cost(C, f))
"""

"""
#grammar.lsp
f = get_frequencies('grammar.lsp')
print(f)
print("Fixed-length cost:  %d" % fixed_length_cost('grammar.lsp'))
T = make_huffman_tree(f)
C = get_code(T)
print(C)
print("Huffman cost:  %d" % huffman_cost(C, f))
"""

"""
#fields.c
f = get_frequencies('fields.c')
print(f)
print("Fixed-length cost:  %d" % fixed_length_cost('fields.c'))
T = make_huffman_tree(f)
C = get_code(T)
print(C)
print("Huffman cost:  %d" % huffman_cost(C, f))
"""