
sen=input()
sen=sen.lower()
print(sen.count("c"))

count=0
for i in range (0,len(sen)):
  if sen[i:i+2] == 'cc':
    count+=1

print(count)