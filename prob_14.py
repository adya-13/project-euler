'''
Author : Shubhanshu Jain;
'''

#Problem link: https://projecteuler.net/problem=14


def solve():
    ls = [-1]*1000001
    ls[1],ls[0] = 1,1;
    for i in range(2,1000000):
        x = i;
        c = 0;
        while(True):
            if x<i:
                ls[i] = ls[x]+c;
                break;
            if(x%2==0):
                x = x//2;
            else:
                x = x*3+1;
            c+=1;
            
    m = max(ls)
    print(ls.index(m))


solve()

