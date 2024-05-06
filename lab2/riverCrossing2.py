from collections import namedtuple
from enum import Enum


class Bank(Enum):
  A = 0
  B = 1


State = namedtuple("State", ["LocationA", "LocationB"])
Info = namedtuple("Info", ["bank", "priest", "evil", "boat"])

startState = State(Info(Bank.A, 3, 3, True), Info(Bank.B, 0, 0, False))
endState = State(Info(Bank.A, 0, 0, False), Info(Bank.B, 3, 3, True))


def isValid(state):
  for v in state._asdict().values():
    if v.priest > 0 and v.priest < v.evil:
      return False
  return True


def getPossibleNodes(state):
  nodes = []
  locationA = state.LocationA
  locationB = state.LocationB
  fromLocation = locationA if locationA.boat == True else locationB
  toLocation = locationB if fromLocation == locationA else locationA
  stateSpace = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]
  for p, e in stateSpace:
    if fromLocation.priest >= p and fromLocation.evil >= e:
      newLocationA = Info(fromLocation.bank, fromLocation.priest - p, fromLocation.evil - e, False)
      newLocationB = Info(toLocation.bank, toLocation.priest + p, toLocation.evil + e, True)

      newState = State(newLocationA, newLocationB) if fromLocation.bank == Bank.A else State(newLocationB, newLocationA)
      nodes.append(newState)
  return nodes


def dfs(start, end):
  parents = dict()
  toVisit = [start]
  discovered = set({start})
  while toVisit:
    vertex = toVisit.pop()
    if end == vertex:
      path = []
      while vertex != start:
        path.insert(0, vertex)
        vertex = parents[vertex]
      path.insert(0, vertex)
      return path

    possibleNodes = getPossibleNodes(vertex)
    for node in possibleNodes:
      if isValid(node) and node not in discovered:
        toVisit.append(node)
        parents[node] = vertex
        discovered.add(node)


for state in dfs(startState, endState):
  a, b = state._asdict().values()
  boat = "🛶 ______________" if a.boat else "______________ 🛶"
  print(f"{a.priest} priest {a.evil} evil {boat} {b.priest} priest {b.evil} evil")
