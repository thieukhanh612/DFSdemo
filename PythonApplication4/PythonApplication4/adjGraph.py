

import sys
import os
import unittest

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
  
        
    def addVertex(self,key):

        if key not in self.vertices:
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key)
            self.vertices[key] = newVertex
            return newVertex
        else:
            return self.vertices[key]

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
  
                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.pred = None
     
    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
   
    def setPred(self,p):
        self.pred = p

  
    def getPred(self):
        return self.pred
        
   
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
 
                
    def __str__(self):
        return str(self.id) + ":color " + self.color +"]\n"
    
    def getId(self):
        return self.id

