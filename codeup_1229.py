height,weight=map(float, input().split())

if height<150:
  avr_weight=height-100
elif 150<=height<160:
  avr_weight=(height-150)/2 +50
elif height>=160:
  avr_weight=(height-100)*0.9

obesity=(weight-avr_weight)*100/avr_weight


if obesity>20:
  print("비만")

elif obesity>10:
  print("과체중")

else:
  print("정상")