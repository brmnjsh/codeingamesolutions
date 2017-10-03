import sys
import math

# MIME Type
# https://www.codingame.com/ide/puzzle/mime-type

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
items = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    items[ext.lower()] = mt

print(items, file=sys.stderr)

for i in range(q):
    fname = input()  # One file name per line.
    ext = fname.split('.')
    ext = list(filter(None, ext))
    if len(ext) != 0:
        ext = ext[-1]
    else:
        ext = ''
    
    print("fname ", fname, "ext ", ext, file=sys.stderr)
    print("ext ", ext, file=sys.stderr)
    
    if ext.lower() in items:
        if fname[-1] == '.' or fname is ext:
            #print("fname: |",fname,"| ext: ", ext, ' UNKNOWN')
            print('UNKNOWN')
            #print("====================================================")
        else:
            #print("fname: |",fname,"| ext: ", ext, ' item: ', items[ext.lower()])
            print(items[ext.lower()])
            #print("====================================================")
    else:
        #print("fname: |",fname,"| ext: ", ext, ' UNKNOWN')
        print('UNKNOWN')
        #print("====================================================")