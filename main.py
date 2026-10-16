from itertools import permutations

count = 0

for x in range(int('100', 16), int('1000', 16)):
    print(x)
    s16 = hex(x)[2:].upper()

    if list(s16) == sorted(s16, reverse=True):
        if '111111' in bin(x)[2:]:

            flag = True
            for k in permutations(s16):
                sk = ''.join(k)
                if '111111' not in bin(int(sk, 16))[2:]:
                    flag = False
                    break

            if flag:
                count += 1

print(count)