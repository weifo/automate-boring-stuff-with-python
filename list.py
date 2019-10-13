def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# 2 return a string of list value
def outstr(l):
    out=''
    # for v in l:
    #     out+=str(v)
    #     out+=', '
    temp=[str(v) for v in l]
    return ', '.join(temp)

test=['apple',12,'is',11.0,True,('one','two','three')]

print(outstr(test))

# 3 print a grid vertically
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''
output:

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''
def _paint(g):
    w,h=len(g[0]),len(g)
    for j in range(w):
        for i in range(h):
            if i==h-1:
                print(g[i][j],end='\n')
            else:
                print(g[i][j],end='')


def paint(g):
    w,h=len(g[0]),len(g)
    afterlist=['']*w
    for i in range(h):
        for j in range(w):
            afterlist[j]+=g[i][j]
    print(*afterlist,sep='\n')
    return afterlist

_paint(grid)

def paint1(g):
    import numpy as np
    raw=np.array(g)
    t=list(raw.T)
    t=[''.join(v) for v in t]
    print(*t,sep='\n')

def paint2(g):
    # out=list(zip(*g))
    out=map(''.join,zip(*g))
    print(*out,sep='\n')

# paint2(grid)
