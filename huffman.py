"""
Created on Tue Nov  8 18:04:17 2016

@author: euan
"""
###########################
# TASK 1
###########################

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def alph_count(text):
    """ Counts letters in text.

    Returns a list of leaf nodes corresponding to each letter in
    the text that is to be coded
    """

    alph = set(text)
    count = [ (i, text.count(i)) for i in alph ]
    count = sorted(count, key=lambda x: x[1])
    return map(Tree,count)


def Huffman_Tree(A):
    """ Creates a Huffman Tree from a given text.

    The function Huffman_Tree is essentially a greedy algorithm that creates
    a parent node for the two least likely nodes in the sorted list of nodes
    """

    while len(A)>1:
        node = Tree(cargo=('Node', A[0].cargo[1]+A[1].cargo[1]),left=A[0],right=A[1])
        A=A[2:]
        A.append(node)
        A.sort(key=lambda x: x.cargo[1])
    return A[0]


def huffman_code(text):
    """ Generates the 'encoding' for a text.

    Uses breadth first search to assign a code to each node of the
    Huffman Tree
    """
    A = alph_count(text)
    A = [[Huffman_Tree(A),'']]
    for i in A:
        if i[0].left != None:
            lchild = [i[0].left,i[1]+'0']
            A.append(lchild)
        if i[0].right != None:
            rchild = [i[0].right,i[1]+'1']
            A.append(rchild)
    code=[]
    for i in range(len(A)):
        if A[i][0].cargo[0] != 'Node':
            code.append((A[i][1],A[i][0].cargo[0]))
    return code


def huffman_encode(encoding, text):
    """ Encodes a text in binary.

    Takes a given encoding and the text, looks up the encoding
    for each letter, and returns the resulting encoded text
    """

    code = {letter:coding for coding,letter in encoding}
    return ''.join( code[letter] for letter in text )


###########################
# TASK 2
###########################

def huffman_decode(encoding, text):
    """ Decodes an encodes string with a given encoding.

    Looks for encodings one bit at a time.
    """
    code = {coding:letter for coding,letter in encoding}
    codewords = dict.keys(code)
    s = len(min(codewords, key=len))
    A=''
    i = s
    while len(text) > 0:
        try:
            A = A + code[text[0:i]]
            text = text[i:]
            i = s
        except KeyError:
            i = i+1
    return A
