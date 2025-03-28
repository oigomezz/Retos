function fixPackages(packages: string): string {
  const pattern = /\([^()]*\)/;
  do {
    packages = packages.replace(pattern, (match) =>
      [...match.slice(1, -1)].reverse().join("")
    );
  } while (pattern.test(packages));

  return packages;
}

export default fixPackages;
