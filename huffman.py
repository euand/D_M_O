"""
Created on Tue Nov  8 18:04:17 2016

@author: euan
"""

from collections import deque

###########################
# TASK 1
###########################

class Tree:
    def __init__(self, freq, char = None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left  = left
        self.right = right


def alph_count(text):
    """ Counts letters in text.

    Returns a list of leaf nodes corresponding to each letter in
    the text that is to be coded
    """

    alph = set(text)
    count = [ (char, text.count(char)) for char in alph ]
    count = sorted(count, key=lambda x: x[1])
    return [Tree(f, char) for char,f in count]


def Huffman_Tree(A):
    """ Creates a Huffman Tree from a given text.

    The function Huffman_Tree is a greedy algorithm that creates a parent
    node for the two least likely nodes in the sorted list of nodes
    """

    while len(A)>1:
        left, right = A[:2]
        frequency = left.freq + right.freq
        A = A[2:]
        A.append(Tree(frequency, left = left, right = right))
        A.sort(key=lambda x: x.freq)
    return A[0]


def huffman_code(text):
    """ Generates the 'encoding' for a text.

    Uses breadth first search to assign a code to each node of the
    Huffman Tree
    """
    A = alph_count(text)
    A = [(Huffman_Tree(A),'')]
    for node, enc in A:
        if node.left:
            A.append((node.left, enc + '0'))
        if node.right:
            A.append((node.right, enc + '1'))
    return [(enc, node.char) for node, enc in A if node.char]


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
