a = int(input())
arr = []
ch = []
for i in range(0, a):
    b = str(input())
    arr.append(b)
    for letter in b:
        ch.append(letter)

ch = list(set(ch))

ch_size = len(ch)

for j in range(0, ch_size):
    for k in range(0, ch_size):
        if (ch[j]<ch[k]):
            swap = ch[j]
            ch[j] = ch[k]
            ch[k] = swap

print(ch)