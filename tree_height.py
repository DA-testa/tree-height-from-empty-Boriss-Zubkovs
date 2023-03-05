# python3

import sys
import threading
import numpy
 

def compute_h(d, parents):
    root = 0
    pos = [[]for _ in range(d)]
    for i in range(d):
        if parents[i] == -1:
            root = i
        else:
            pos[parents[i]].append(i)    

    def max_h(f):
        height = 1
        if not pos[f]:
            return height
        else:
            for children in pos[f]:
                height = max(height, max_h(children))
            return height+1
        return max_h(root)
    
def main():
    text = input("Enter F or I:")
    if "I" in text:
        n = int(input())
        parents = list(map(int,input().split()))
    elif "F" in text:
        filename = input()
    else:
        print("Error: wrong name of file")    
        return
    
        




    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))