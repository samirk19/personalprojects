import re

a =  "01/01/2024"
b =  "It is Wednesday 12/06/2023."  
c =  "The secret of life is 42 as of 10pm on 1978"
d =  "The model should be 25/25/2000 cm."
e =  "[06/10/2020]: Invalid login. Killbots dispatched."
f =  "The time is 11:11:1111"

regex = "(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(19|20)\d{2}"

li = []
li.append(a)
li.append(b)
li.append(c)
li.append(d)
li.append(e)
li.append(f)
for x in range(0, len(li)):
    check = re.search(regex, li[x])
    if (check != None):
        print(li[x], "match")
    else:
        print(li[x], "reject")