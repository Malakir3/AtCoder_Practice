# C - Don’t be cycle
# 具体例を紙に書きだしてuniteメソッドの動作をイメージ
from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self,x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
    def unite(self,x,y):
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
            

  #  def same(self, x, y):
  #       """
  #       同じグループに属するか判定

  #       Parameters
  #       ---------------------
  #       x : int
  #           判定したノード
  #       y : int
  #           判定したノード

  #       Returns
  #       ---------------------
  #       ans : bool
  #           同じグループに属しているか
  #       """
  #       return self.find(x) == self.find(y)

  #   def size(self, x):
  #       """
  #       木のサイズを計算

  #       Parameters
  #       ---------------------
  #       x : int
  #           計算したい木のノード

  #       Returns
  #       ---------------------
  #       size : int
  #           木のサイズ
  #       """
  #       return -self.root[self.find(x)]

  #   def roots(self):
  #       """
  #       根のノードを取得

  #       Returns
  #       ---------------------
  #       roots : list
  #           根のノード
  #       """
  #       return [i for i, x in enumerate(self.root) if x < 0]

  #   def group_size(self):
  #       """
  #       グループ数を取得

  #       Returns
  #       ---------------------
  #       size : int
  #           グループ数
  #       """
  #       return len(self.roots())

  #   def group_members(self):
  #       """
  #       全てのグループごとのノードを取得

  #       Returns
  #       ---------------------
  #       group_members : defaultdict
  #           根をキーとしたノードのリスト
  #       """
  #       group_members = defaultdict(list)
  #       for member in range(self.n):
  #           group_members[self.find(member)].append(member)
  #       return group_members