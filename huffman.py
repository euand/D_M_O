# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:04:17 2016

@author: euan
"""
###########################
# TASK 1
###########################

#First create a tree object

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)   
 
Hamlet = u'O all you host of heaven! O earth! What else? And shall I couple hell? Oh, fie! Hold, hold, my heart, And you, my sinews, grow not instant old, But bear me stiffly up. Remember thee! Ay, thou poor ghost, whiles memory holds a seat In this distracted globe. Remember thee! Yea, from the table of my memory I’ll wipe away all trivial fond records, All saws of books, all forms, all pressures past That youth and observation copied there, And thy commandment all alone shall live Within the book and volume of my brain, Unmixed with baser matter. Yes, by heaven! O most pernicious woman! O villain, villain, smiling, damned villain! My tables! Meet it is I set it down That one may smile, and smile, and be a  villain. At least I’m sure it may be so in Denmark. So, uncle, there you are. Now to my word.'.lower()
Goethe = u'Habe nun, ach! Philosophie, Juristerei und Medizin, Und leider auch Theologie Durchaus studiert, mit heissem Bemühn. Da steh ich nun, ich armer Tor! Und bin so klug als wie zuvor; Heisse Magister, heisse Doktor gar Und ziehe schon an die zehen Jahr Herauf, herab und quer und krumm Meine Schüler an der Nase herum Und sehe, dass wir nichts wissen können! Das will mir schier das Herz verbrennen. Zwar bin ich gescheiter als all die Laffen, Doktoren, Magister, Schreiber und Pfaffen; Mich plagen keine Skrupel noch Zweifel, Fürchte mich weder vor Hölle noch Teufel Dafür ist mir auch alle Freud entrissen, Bilde mir nicht ein, was Rechts zu wissen, Bilde mir nicht ein, ich könnte was lehren, Die Menschen zu bessern und zu bekehren. Auch hab ich weder Gut noch Geld, Noch Ehr und Herrlichkeit der Welt; Es möchte kein Hund so länger leben! Drum hab ich mich der Magie ergeben, Ob mir durch Geistes Kraft und Mund Nicht manch Geheimnis würde kund; Dass ich nicht mehr mit saurem Schweiss Zu sagen brauche, was ich nicht weiss; Dass ich erkenne, was die Welt Im Innersten zusammenhält, Schau alle Wirkenskraft und Samen, Und tu nicht mehr in Worten kramen.'.lower()

'''  Now define a function that returns a list of leaf nodes corresponding to 
 each letter in the text that is to be coded
 '''
    
def alph_count(text):
    alph = set(text)
    count = []
    for i in alph:
        count.append([i,text.count(i)])
    count = sorted(count, key=lambda x: x[1])
    count = list(map(Tree,count))
    return count
    
'''
The function Huffman_Tree is essentially a greedy algorithm that creates 
a parent node for the two least likely nodes in the sorted list of nodes
'''
A = alph_count('THis is an example')
A[0].cargo[1]

def Huffman_Tree(A):
    while len(A)>1:
        node = Tree(cargo=('Node', A[0].cargo[1]+A[1].cargo[1]),left=A[0],right=A[1])
        A=A[2:]  
        A.append(node)
        A.sort(key=lambda x: x.cargo[1])
    return A[0]
    
Huffman_Tree(alph_count(Hamlet)).cargo

'''
Will now use breadth first search to assign a code to each node of the 
Huffman Tree
'''

def Huffman_Code(text):
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
            code.append([A[i][1],A[i][0].cargo[0]])
    return code

code = Huffman_Code(Hamlet)
print code

def Huffman_Encode(text):
    code = Huffman_Code(text)
    code = {d[1]: d[0] for d in code}
    codedtext = ''
    for i in range(len(text)):
        codedtext = codedtext+code[text[i]]
    return codedtext
    
###########################
# TASK 2
###########################
    
code_H = Huffman_Code(Hamlet)
codedtext_H = Huffman_Encode(Hamlet)

code_G = Huffman_Code(Goethe)
codedtext_G = Huffman_Encode(Goethe)

print code_G
print codedtext_G

def huffman_decode(code, text):
    if type(code) != dict:
        code = {d[0]: d[1] for d in code}
    codewords = dict.keys(code)
    A=''
    s = len(min(codewords, key=len))
    i = s
    while len(text) > 0:
        if text[0:i] in codewords:
            A = A + code[text[0:i]]
            text = text[i:]
            i = s
        else:
            i=i+1
    return A
    
huffman_decode(code_H,codedtext_H)

huffman_decode(code_G,codedtext_G)

with open('megandiss', 'r') as myfile:
    data=myfile.read().replace('\n', '')

import time

t0 = time.time()

code_M = Huffman_Code(data)
encoded_M = Huffman_Encode(data)

t1=time.time()

decoded = huffman_decode(code_M,encoded_M)

t2 = time.time()

print t1-t0
 
print t2-t1

len(data)
