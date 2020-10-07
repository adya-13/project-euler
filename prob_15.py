Link: https://projecteuler.net/problem=15


ls = []
for i in range(500):
    ls.append(list([0]*500));
for i in range(500):
    ls[0][i] = 1;
    ls[i][0] = 1;
for i in range(1,500):
    for j in range(1,500):
        ls[i][j] = ls[i][j-1]+ls[i-1][j]


n,m = 20,20
print(ls[n][m])
