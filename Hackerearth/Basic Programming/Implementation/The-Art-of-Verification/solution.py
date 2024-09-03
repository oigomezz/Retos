NOT_FOUND = "Not Found"

s = input()
un_index = s.find('username')
pwd_index = s.find('pwd')
pr_index = s.find('profile')
role_index = s.find('role')
key_index = s.find('key')

un = s[un_index + 9:pwd_index - 1] if un_index != -1 else NOT_FOUND
pwd = s[pwd_index + 4:pr_index - 1] if pwd_index != -1 else NOT_FOUND
pr = s[pr_index + 8:role_index - 1] if pr_index != -1 else NOT_FOUND
r = s[role_index + 5:key_index - 1] if role_index != -1 else NOT_FOUND
key = s[key_index + 4:] if key_index != -1 else NOT_FOUND

print("username:", un)
print("pwd:", pwd)
print("profile:", pr)
print("role:", r)
print("key:", key)
