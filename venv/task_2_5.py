line1 = '0123456789'
s5 = line1[::2]
print(s5)

str2 = ''
for i in range(0, len(line1), 2):
    str2 += line1[i]
assert str2 == s5
