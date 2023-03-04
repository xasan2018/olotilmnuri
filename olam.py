import requests
from pprint import pprint as print
from main import rasm


parol='3004959'
son=20
if (parol=='3004959'):
    url=f"http://127.0.0.1:8000/{parol}?q={son}"
else:
    url='None'

response=requests.get(url)
print((response.status_code))
x=response.json()['q']
y=x*x
print(f"{son} ning kvadratining kvadrati {y}ga teng")


######################## RASM NOMINI KIRITING #########

img = "1.jpg"

###############################



print(rasm(img))