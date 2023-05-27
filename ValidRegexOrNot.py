import re

T = int(input())
S = []
for i in range(T):
    C = input()
    S.append(C)

for pattern in S:
    try:
        re.compile(pattern)
        print('True')
    except re.error:
        print('False')
