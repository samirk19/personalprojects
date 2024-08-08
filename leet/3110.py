s = "hello"
sum = 0
for x in range(len(s)-1):
    print(f'|{ord(s[x])} - {ord(s[x+1])}|')
    sum += abs(ord(s[x]) - ord(s[x+1]))
    print(sum)