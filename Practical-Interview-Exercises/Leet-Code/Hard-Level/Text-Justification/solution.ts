function fullJustify(words: string[], maxWidth: number): string[] {
    const result: string[] = [];
    let currentLine: string[] = [];
    let currentLength = 0;

    for (const word of words) {
        if (currentLength + word.length + currentLine.length > maxWidth) {
            // Justify the current line
            result.push(justifyLine(currentLine, currentLength, maxWidth));
            currentLine = [];
            currentLength = 0;
        }
        currentLine.push(word);
        currentLength += word.length;
    }

    // Handle the last line
    if (currentLine.length > 0) {
        result.push(currentLine.join(' ') + ' '.repeat(maxWidth - (currentLength + currentLine.length - 1)));
    }

    return result;
};

function justifyLine(line: string[], lineLength: number, maxWidth: number): string {
    const spacesNeeded = maxWidth - lineLength;
    const gaps = line.length - 1;

    if (gaps === 0) {
        return line[0] + ' '.repeat(spacesNeeded);
    }

    const spaceBetweenWords = Math.floor(spacesNeeded / gaps);
    const extraSpaces = spacesNeeded % gaps;

    let justifiedLine = '';
    for (let i = 0; i < line.length; i++) {
        justifiedLine += line[i];
        if (i < line.length - 1) {
            justifiedLine += ' '.repeat(spaceBetweenWords + (i < extraSpaces ? 1 : 0));
        }
    }

    return justifiedLine;
}
