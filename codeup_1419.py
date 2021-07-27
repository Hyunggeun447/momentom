#re의 사용법

import re

n=input()
s='love'

x=re.findall(s,n)
print(len(x))