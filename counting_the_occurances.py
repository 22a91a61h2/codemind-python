test_str = input()
ch=input()
count = 0
for i in test_str:
    if i == ch:
        count = count + 1
if(count>0):
    print(str(count))
else:
    print("-1")