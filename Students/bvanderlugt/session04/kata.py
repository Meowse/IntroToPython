
# read in towswift
import re

def parse_book(book = 'tomswift.txt'):
    f = open(book, 'r')
    f_full = f.read()
    header_size = f_full.index("Chapter 1") - 1
    f.seek(0)
    f_header = f.read(header_size)
    f_rest = f.read()
    f.close()

    t = f_rest.lower()

    x = re.sub("[^a-z '\n]","",t)
    x_sub_n = " ".join(x.split("\n"))
    x_split = x_sub_n.split()

    text = x_split
    
    return text



def trigram(sample = True):
    '''
     We have 
    '''
    text = parse_book()
    xx = []
    value = []
    for i in range(len(text)-1):
        xx.append([text[i:i+2]])
        value.append([text[i+3]])          
    trigram = dict(zip(xx, value))
    return trigram[1:1000]
