class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const clonedGraph = new Map<_Node, _Node>();
  const queue: _Node[] = [node];
  clonedGraph.set(node, new _Node(node.val, []));

  while (queue.length) {
    const curr = queue.shift()!;

    for (const neighbor of curr.neighbors) {
      if (!clonedGraph.has(neighbor)) {
        clonedGraph.set(neighbor, new _Node(neighbor.val, []));
        queue.push(neighbor);
      }
      clonedGraph.get(curr)!.neighbors.push(clonedGraph.get(neighbor)!);
    }
  }

  return clonedGraph.get(node) || null;
}
