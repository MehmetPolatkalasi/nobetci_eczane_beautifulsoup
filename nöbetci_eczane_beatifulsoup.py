from re import M
import requests
from bs4 import BeautifulSoup
import datetime

x = datetime.datetime.now()
day = str(x.day)
month = str(x.strftime("%m"))
year = str(x.year)

url = "https://www.aeo.org.tr/NobetModulu/Nobet?NobetTarihiAsString="+ day +"."+ month +"."+ year + "&IlceKey=00000000-0000-0000-0000-000000000000"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")




eczane = soup.find_all("li",{"class":"list-group-item col-md-4"})
file = open("pharmacy.txt","w")
count = 1

for i in eczane:
    
    i = i.text.strip()
    i = i.replace("\n","-")
    

    file.writelines("{} - {}*\n".format(count,i))
    count +=1

file.close()
    

