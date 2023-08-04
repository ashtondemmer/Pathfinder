
endX = 10
endY = 10
startNode = (0,0)
currentNode = startNode
endNode = (endX, endY)
openList = [startNode]
neighborNodes = []
closedList = []

def updatePath():
    #Increment path by 1 (change color to green)
    return 0


def getManhattanDistance(x, y):
    h = (abs(x - endX)) + (abs(y - endY))
    return h

def expandNeighborNodes():
    #clear openList and replace with neighbors of current node
    neighborNodes = []
    neighborNodes.append({'X': })



def findPath():
    expandNeighborNodes(currentNode)
    while currentNode is not endNode:
        closedList.append(currentNode)
        expandNeighborNodes(currentNode)




