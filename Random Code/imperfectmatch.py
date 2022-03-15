def anagram(a,b):    
    if (sorted(a)==sorted(b)) and a!=b:
        return True
    else:
        return False

n = int(input())
stringWord = []
res = set()
for i in range(n):
    stringWord.append(input())
for i in range(n):
    for j in range(i+1,n):
        if anagram(stringWord[i],stringWord[j]):
            temp = (stringWord[i],stringWord[j])
            res.add(tuple(sorted(temp)))
print(len(res))
#ps : not sure about the time complexity :kekhands: