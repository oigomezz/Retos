def is_balanced(expression):
    symbols = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for char in expression:
        symbol = char
        contains_key = symbol in symbols

        if contains_key or symbol in symbols.values():
            if contains_key:
                stack.append(symbol)
            elif not stack or symbol != symbols[stack.pop()]:
                return False

    return not stack


print(is_balanced("{a + b [c] * (2x2)}}}}"))
print(is_balanced("{ [ a * ( c + d ) ] - 5 }"))
print(is_balanced("{ a * ( c + d ) ] - 5 }"))
print(is_balanced("{a^4 + (((ax4)}"))
print(is_balanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(is_balanced("{{{{{{(}}}}}}"))
print(is_balanced("(a"))
