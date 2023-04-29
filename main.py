# C - Don’t be cycle
from collections import defaultdict
# ランクの考え方
# ランクの等しい木同士を連結するときに限り、1が加算される
# 各木の根に対して、木のランクを保持させる。
# 木を連結するときには、新たな木の根となるほうのみランクを更新する。
class UnionFind():
    # 初期化
    def __init__(self,n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    # 根のインデックスを検索
    def find(self,x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    # ノードの結合        
    def unite(self,x,y):
        # ここで求めるx,yは、根のノード番号となる。（経路圧縮による効果）
        # つまり、この処理以降ではroot[x]やroot[y]は必ず負の値になる
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    # 同じグループか判定                
    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    # 木のサイズを計算
    def size(self,x):
        return -self.root[self.find(x)]

    # 根のノードだけを抽出したリストを取得
    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]
    
    # グループ数を取得
    def group_size(self):
        return len(self.roots())
    
    # 各グループのノードを取得
    def group_members(self):
        # 根をキーとしたノードのリスト
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

# メイン処理
n,m = map(int, input().split())
uf = UnionFind(n)
ans = 0

for _ in range(m):
    a,b = map(int, input().split())
    if uf.same(a-1,b-1):
        ans += 1

    uf.unite(a-1,b-1)

print(ans)