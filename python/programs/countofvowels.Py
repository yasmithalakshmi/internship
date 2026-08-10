word=str(input("enter a word:"))
vowels='aeiouAEIOU'
list1=[]
count=0
for i in word:
    if i in vowels:
        count+=1
        list1.append(i)
print(count)
print(list1)