class _Node {
  val: number;
  next: _Node | null;
  random: _Node | null;

  constructor(val?: number, next?: _Node, random?: _Node) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}

function copyRandomList(head: _Node | null): _Node | null {
  const hashMap = new Map<_Node, _Node>();
  let cur = head;

  while (cur) {
    hashMap.set(cur, new _Node(cur.val));
    cur = cur.next;
  }

  cur = head;

  while (cur) {
    const copy = hashMap.get(cur);
    if (copy) {
      copy.next = cur.next ? hashMap.get(cur.next) : null;
      copy.random = cur.random ? hashMap.get(cur.random) : null;
    }
    cur = cur.next;
  }

  return hashMap.get(head) || null;
}
