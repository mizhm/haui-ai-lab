tree = {
    "A": ["B", "C", "D"],
    "B": ["M", "N"],
    "C": ["L"],
    "D": ["O", "P"],
    "M": ["X", "Y"],
    "N": ["U", "V"],
    "O": ["I", "J"],
    "Y": ["R", "S"],
    "V": ["G", "H"]
}


def bfs(start, tree, goal):
  parents = {}
  toVisit = [start]
  discovered = set({start})
  while toVisit:
    vertex = toVisit.pop(0)
    if goal == vertex:
      path = []
      while vertex != start:
        path.insert(0, vertex)
        vertex = parents[vertex]
      path.insert(0, vertex)
      return path
    if vertex in tree:
      for node in tree[vertex]:
        if node not in discovered:
          toVisit.append(node)
          discovered.add(node)
          parents[node] = vertex


if __name__ == "__main__":
  print(bfs("A", tree, "N"))
