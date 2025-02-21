function decodeFilename(filename: string): string {
  const match = /(?<=\d+_)[\w-]+\.\w+/.exec(filename);
  return match ? match[0] : "";
}
export default decodeFilename;
