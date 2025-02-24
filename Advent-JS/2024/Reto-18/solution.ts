function findInAgenda(
  agenda: string,
  phone: string
): { name: string; address: string } | null {
  const data: { name: string; address: string }[] = [];

  for (const entry of agenda.split("\n")) {
    const matchedPhone = /\+[-\d]+/.exec(entry)?.[0];
    const nameMatch = /<([^>]+)>/.exec(entry);

    if (!nameMatch) continue;
    const [, name] = nameMatch;

    if (!matchedPhone?.includes(phone)) continue;
    const address = entry.replace(matchedPhone, "").replace(`<${name}>`, "");

    data.push({
      address: address.trim(),
      name: name.trim(),
    });
  }

  return data.length === 1 ? data[0] : null;
}

export { findInAgenda };
