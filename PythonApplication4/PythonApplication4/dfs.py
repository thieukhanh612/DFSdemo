
import pylab as pl
from matplotlib.pyplot import pause
import networkx as nx
from Graph import Graph, Vertex

pl.ion()

G = nx.DiGraph()
node_number = 0
node_colors = []
vertices = []
edges = []
parents = {}
node_color= {}

# Draw Graph 
def draw_graph(graph, node_size):
    global G
    global node_colors, node_color
    global vertices, edges
    
    # Turn graph to edge list
    for v,e in graph.items():
        k = [v]*len(e)
        edges.extend(zip(k, e))
    vertices = set([k1 for k1, k2 in edges] + [k2 for k1, k2 in edges])
    
    nx.set_edge_attributes(G, 'name', vertices)

    # add vertices
    for vertice in vertices:
        G.add_node(vertice)
    
    # add edges
    for edge in edges:
        G.add_edge(edge[0], edge[1], arrows=True)
    node_color = {x:"white" for x in vertices}
    
    for v,c in node_color.items():
        node_colors.append(c)
    
    # draw graph
    layout = nx.shell_layout(G)
    nx.draw(G, layout, with_labels=True,node_size = 800, node_color=node_colors)
                               
    # show graph
    pl.show()
    pause(5)

# Depth First Search 
def dfs(g):
    global parents

    for u in g.getVertices():
        if g.getVertex(u).getColor() == 'white':
            print ("Start with vertice:" + str(u))
            dfs_visit(g, g.getVertex(u))

def dfs_visit(g, u):
    global parents
    print (" Checking vertice:" + str( u.getId()))
    u.setColor('gray')
    change_node_color('gray', u.getId())
     
    for v in u.getConnections():
        print ("From " +str(u.getId())+" go to " + str(v.getId()))
        if v.getColor() == 'gray':
            print ("Back vertice: "+str(v.getId())+ " Parent: " + str(v.getParent()))           
        if v.getColor() == 'white':
            parents[v.getId()] = u.getId()
            v.setParent(u)
            dfs_visit(g, v)
    
    print (parents) 
    u.setColor('black')
    change_node_color('black', u.getId())

    
# Change color function
def change_node_color(c, node):
    global node_color
    global node_colors
    
    node_colors = []

    # Color the visited node
    node_color[node]=c

    for k,v in node_color.items():
        node_colors.append(v)
    
    pos = nx.shell_layout(G)
    nx.draw(G, pos,node_size = 600, node_color = node_colors )
    pl.draw()
    pause(2)
            

         


# 1. Declare the graph


graph = {1: [2, 8],
        2: [1, 8, 3],
        3: [2, 4, 6, 9],
        4: [3, 5, 6],
        5: [4, 6],
        6: [3, 5, 7, 4],
        7: [6, 8, 9],
        8: [1, 2, 7, 9],
        9: [3, 7, 8]}

# 1. Create graph
graphl = Graph()

for k,v in graph.items():
    graphl.addVertex(k)
    for i in v:
        graphl.addEdge(k, i)

# 2. Draw the graph
draw_graph(graph, len(edges) )

# 3. Run the algorithm
dfs(graphl)

pause(60)
