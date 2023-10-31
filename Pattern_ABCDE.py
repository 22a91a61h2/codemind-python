size=int(input())
for i in range(size):
    for j in range(i+1):
        print(chr(65 + i), end="")
    print()