# Biconnected Components

Before Biconnected Components, let's first try to understand what a Biconnected Graph is and how to check if a given graph is Biconnected or not.

A graph is said to be Biconnected if:

1. It is connected, i.e. it is possible to reach every vertex from every other vertex, by a simple path.
2. Even after removing any vertex the graph remains connected.

Now what to look for in a graph to check if it's Biconnected. By now it is said that a graph is Biconnected if it has no vertex such that its removal increases the number of connected components in the graph. And if there exists such a vertex then it is not Biconnected. A vertex whose removal increases the number of connected components is called an Articulation Point.

So simply check if the given graph has any articulation point or not. If it has no articulation point then it is Biconnected otherwise not. Here's the pseudo code:

```python
time = 0
def isBiconnected(vertex, adj[][], low[], disc[], parent[], visited[], V):
    disc[vertex]=low[vertex]=time+1
    time = time + 1
    visited[vertex]=true
    child = 0
    for i = 0 to V:
        if adj[vertex][i] == true:
            if visited[i] == false:
                child = child + 1
                parent[i] = vertex
                result = isBiconnected(i, adj, low, disc, visited, V, time)
                if result == false:
                    return false
                low[vertex] = minimum(low[vertex], low[i])
                if parent[vertex] == nil AND child > 1:
                    return false
                if parent[vertex] != nil AND low[i] >= disc[vertex]:
                    return false
            else if parent[vertex] != i:
                low[vertex] = minimum(disc[i], low[vertex])
    return true
```

The code above is exactly same as that for Articulation Point with one difference that it returns false as soon as it finds an Articulation Point.

Biconnected components in a graph can be determined by using the previous algorithm with a slight modification. And that modification is to maintain a Stack of edges. Keep adding edges to the stack in the order they are visited and when an articulation point is detected i.e. say a vertex u has a child v such that no vertex in the subtree rooted at v has a back edge (low[v] >= disc[u]) then pop and print all the edges in the stack till the u-v is found, as all those edges including the edge u-v will form one biconnected component.

```python
time = 0
def DFS(vertex, adj[][], low[], disc[], parent[], visited[], V, stack):
    disc[vertex]=low[vertex]=time+1
    time = time + 1
    visited[vertex]=true
    child = 0
    for i = 0 to V:
        if adj[vertex][i] == true:
            if visited[i] == false:
                child = child + 1
                push edge(u,v) to stack
                parent[i] = vertex
                DFS(i, adj, low, disc, visited, V, time, stack)
                low[vertex] = minimum(low[vertex], low[i])
                if parent[vertex] == nil AND child > 1:
                    while last element of stack != (u,v):
                        print last element of stack
                        pop from stack
                    print last element of stack
                    pop from stack
                if parent[vertex] != nil AND low[i] >= disc[vertex]:
                    while last element of stack != (u,v):
                        print last element of stack
                        pop from stack
                    print last element of stack
                    pop from stack
            else if parent[vertex] != i AND disc[i] < low[vertex]:
                low[vertex] = disc[i]
                push edge(u,v) to stack

def biconnected_components(adj[][], V):
    for i = 0 to V:
        if visited[i] == false:
            DFS(i, adj, low, disc, parent, visited, V, time, stack)
            while stack is not empty:
                print last element of stack
                pop from stack
```

**Time complexity** of the algorithm is same as that of DFS. If V is the number of vertices and E is the number of edges then complexity is O(V + E).
