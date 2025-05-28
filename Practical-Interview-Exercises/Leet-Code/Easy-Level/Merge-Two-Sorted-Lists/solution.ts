class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  if (!list1) return list2;
  if (!list2) return list1;

  let mergedHead: ListNode | null = null;
  let mergedTail: ListNode | null = null;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      if (!mergedHead) {
        mergedHead = list1;
        mergedTail = list1;
      } else {
        mergedTail.next = list1;
        mergedTail = mergedTail.next;
      }
      list1 = list1.next;
    } else {
      if (!mergedHead) {
        mergedHead = list2;
        mergedTail = list2;
      } else {
        mergedTail.next = list2;
        mergedTail = mergedTail.next;
      }
      list2 = list2.next;
    }
  }

  // Append any remaining elements from either list
  mergedTail.next = list1 ? list1 : list2;

  return mergedHead;
}
