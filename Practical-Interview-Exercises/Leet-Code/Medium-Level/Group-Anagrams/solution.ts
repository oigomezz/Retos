function groupAnagrams(strs: string[]): string[][] {
  const map: Map<string, string[]> = new Map();
  for (const str of strs) {
    const key = [...str].sort((a, b) => a.localeCompare(b)).join("");
    if (!map.has(key)) map.set(key, []);
    map.get(key)!.push(str);
  }
  return Array.from(map.values());
}
