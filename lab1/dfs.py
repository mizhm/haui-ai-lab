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


def dfs(start, tree, goal):
  parents = {}
  to_visit = [start]
  discovered = set({start})
  while to_visit:
    print(to_visit)
    vertex = to_visit.pop()
    if goal == vertex:
      path = []
      while vertex != start:
        path.insert(0, vertex)
        vertex = parents[vertex]
      path.insert(0, vertex)
      return path
    if vertex in tree:
      for node in tree[vertex][::-1]:
        if node not in discovered:
          to_visit.append(node)
          discovered.add(node)
          parents[node] = vertex


if __name__ == "__main__":
  print(dfs("A", tree, "R"))
