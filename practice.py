
n=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	

l=len(stages)



dic={}
for i in range(1,n+2):
  dic[i]=0

for i in stages:  #각 스테이지 인원
  dic[i]+=1

dic_total={0:0}
for i in range(1,n+2):
  dic_total[i]=dic_total[i-1]+dic[i]

dic_percent={}

for i in range(1,n+2):
  dic_percent[i]="{:.2f}".format(dic[i]/(l-dic_total[i-1]))

del dic_percent[n+1]


dic_percent=sorted(dic_percent.items(), key=lambda x: x[1],reverse=True)



answer=[]
for i in range(0,n):
  answer.append(dic_percent[i][0])

print(answer)