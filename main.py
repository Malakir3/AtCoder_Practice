# https://atcoder.jp/contests/atc001/tasks/unionfind_a
# B - Union Find 

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x            
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self,x,y):
        return self.find(x) == self.find(y)
    
n,q = map(int, input().split())
uf = UnionFind(n)

ans = []
for _ in range(q):
    p,a,b = map(int,input().split())
    if p == 0:
        uf.unite(a,b)
    elif p == 1:
        if uf.same(a,b) == True:
            ans.append('Yes')
        else:
            ans.append('No')

for _ in ans:
    print(_)
