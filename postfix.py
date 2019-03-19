def calc(x):

    '''
    >>> calc("1 2 + 4 * 3 +")
    15
    >>> calc("1 2 3 * + 2 -")
    5
    '''
    x=x.split()

    g=[]

    for i in range(len(x)):
        if x[i].isdigit():
            g.append(x[i])
        elif x[i]=='+':
            k=int(g.pop())+int(g.pop())
            g.append(k)
        elif x[i]=='*':
            k=int(g.pop())*int(g.pop())
            g.append(k)
        elif x[i]=='-':
            v=g.pop()
            k=int(g.pop())-int(v)
            g.append(k)
        elif x[i]=='/':
            v=g.pop()
            k=int(g.pop())/int(v)
            g.append(k)
    return(int(g[0]))

'''print(calc("1 2 3 * + 2 -"))'''

import doctest
doctest.testmod()
