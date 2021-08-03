
n=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	

l=len(stages)

print(l)    #총원

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




print(dic_percent)