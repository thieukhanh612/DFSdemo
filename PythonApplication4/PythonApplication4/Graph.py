
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,id):
        if id not in self.vertices:
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(id)
            self.vertices[id] = newVertex
            return newVertex
        else:
            return self.vertices[id]

    def getVertex(self,id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def addEdge(self,vertice1,vertice2,cost=0):
            if vertice1 not in self.vertices:
                nv = self.addVertex(vertice1)
            if vertice2 not in self.vertices:
                nv = self.addVertex(vertice2)
            self.vertices[vertice1].addNeighbor(self.vertices[vertice2],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
  
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.parent = None
     
    def addNeighbor(self,nbr,cost=0):
        self.connectedTo[nbr] = cost
        
    def setColor(self,color):
        self.color = color
        
    def setParent(self,p):
        self.parent = p

    def getParent(self):
        return self.parent
       
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
           
    def __str__(self):
        return str(self.id) + ":color " + self.color +"]\n"
    
    def getId(self):
        return self.id

