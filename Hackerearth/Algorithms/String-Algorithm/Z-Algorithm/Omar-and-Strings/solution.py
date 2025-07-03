def is_palindrome(x, start, length):
    offset = start
    end_offset = start + length - 1
    for _ in range(length // 2):
        if x[offset] != x[end_offset]:
            return False
        offset += 1
        end_offset -= 1
    return True


def get_palindromic_suffix(x):
    for idx in range(len(x)):
        if is_palindrome(x, idx, len(x) - idx):
            return x[idx:]
    return ""


def get_palindromic_prefix(x):
    for idx in reversed(range(len(x))):
        if is_palindrome(x, 0, idx + 1):
            return x[:idx + 1]
    return ""


def z_function(str1, str2):
    z_text = str1 + '$' + str2
    z_array = [0] * len(z_text)
    left = -1
    right = -1
    for idx in range(1, len(z_text)):
        if idx > right:
            count = 0
            while idx + count < len(z_text) and z_text[idx + count] == z_text[count]:
                count += 1
            z_array[idx] = count
            if count > 1:
                left = idx
                right = left + count - 1
        elif left < idx <= right:
            j = idx - left
            if z_array[j] < right - idx + 1:
                z_array[idx] = z_array[j]
            else:
                left = idx
                count = right - left + 1
                while idx + count < len(z_text) and z_text[idx + count] == z_text[count]:
                    count += 1
                z_array[idx] = count
                right = left + count - 1
    return z_array[len(str1) + 1:]


s = input().strip()
omeric = get_palindromic_suffix(s) + get_palindromic_prefix(s)
z = z_function(omeric, omeric)
counts = [0] * (len(omeric) + 1)
for i in z:
    counts[i] += 1
for i in reversed(range(len(counts) - 1)):
    counts[i] += counts[i + 1]
print(omeric)
print(' '.join(str(x) for x in counts[1:]))
