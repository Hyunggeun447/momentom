
# for + enumerate, 2개변수 for문


sen=input()

word='t'
list=[]
for pos,char in enumerate(sen):
  if(char == word):
    list.append(pos)

for i in range(0,len(list)):
  print(list[i]+1)

