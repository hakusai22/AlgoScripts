'''
Author: hakusai
Date: 2023-05-17 01:04:55
LastEditTime: 2023-05-17 01:05:04
Description: 
'''
class UnionFindGraph:
    """并查集维护无向图每个连通块的边数和顶点数"""

    __slots__ = ("_parent", "n", "part", "vertex", "edge")

    def __init__(self, n: int):
        self._parent = list(range(n))
        self.n = n
        self.part = n
        self.vertex = [1] * n  # 每个联通块的顶点数
        self.edge = [0] * n  # 每个联通块的边数

    def find(self, x: int) -> int:
        while x != self._parent[x]:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            self.edge[rootX] += 1
            return False
        if self.vertex[rootX] > self.vertex[rootY]:
            rootX, rootY = rootY, rootX
        self._parent[rootX] = rootY
        self.vertex[rootY] += self.vertex[rootX]
        self.edge[rootY] += self.edge[rootX] + 1
        self.part -= 1
        return True

    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def getGroups(self) -> DefaultDict[int, List[int]]:
        groups = defaultdict(list)
        for key in range(self.n):
            root = self.find(key)
            groups[root].append(key)
        return groups

    def getRoots(self) -> List[int]:
        return list(set(self.find(i) for i in range(self.n)))

    def __repr__(self) -> str:
        return "\n".join(f"{root}: {member}" for root, member in self.getGroups().items())

    def __len__(self) -> int:
        return self.part
