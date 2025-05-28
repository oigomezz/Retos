function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const merged = mergeArrays(nums1, nums2);
  const mid = Math.floor(merged.length / 2);
  return merged.length % 2 === 0
    ? (merged[mid - 1] + merged[mid]) / 2
    : merged[mid];
}

function mergeArrays(arr1: number[], arr2: number[]): number[] {
  const merged: number[] = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      merged.push(arr1[i]);
      i++;
    } else {
      merged.push(arr2[j]);
      j++;
    }
  }

  // Append any remaining elements from either array
  return merged.concat(arr1.slice(i)).concat(arr2.slice(j));
}
