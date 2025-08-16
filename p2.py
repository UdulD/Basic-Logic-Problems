n=str(input('enter a number'))
count=0
l=['0','1','2','3','4','5','6','7','8','9']
for i in range(len(n)):
    if n[i] in l:
        count=count+1
print(count)
