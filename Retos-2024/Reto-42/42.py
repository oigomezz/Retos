def ohm(v=None, r=None, i=None):

    if v is not None and r is not None and i is None:
        if r != 0:
            return f"I = {(v / r):,.2f}"
    elif v is not None and i is not None and r is None:
        if i != 0:
            return f"R = {(v / i):,.2f}"
    elif r is not None and i is not None and v is None:
        return f"V = {(r * i):,.2f}"

    return "Invalid values"


print(ohm())
print(ohm(v=5.0))
print(ohm(v=5.0, r=4.0))
print(ohm(v=5.0, i=4.0))
print(ohm(r=5.0, i=4.0))
print(ohm(v=5.125, r=4.0))
print(ohm(v=5.0, i=4.125))
print(ohm(r=5.0, i=4.125))
print(ohm(v=5.0, r=0.0))
print(ohm(v=5.0, i=0.0))
print(ohm(r=5.0, i=0.0))
print(ohm(v=5.0, r=4.0, i=3.0))
