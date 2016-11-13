import time
from huffman import *

def time_encode_decode(text):

    # encode
    t0 = time.time()
    code_M = huffman_code(data)
    encoded_M = huffman_encode(data)
    t1=time.time()

    # decode
    decoded = huffman_decode(code_M,encoded_M)
    t2 = time.time()

    # (encode, decode, length of text)
    return (t1-t0, t2-t1, len(data))


def time_trials():
    with open('megandiss', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return time_encode_decode(data)
