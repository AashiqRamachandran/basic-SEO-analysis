import requests
from bs4 import BeautifulSoup

websitename=input("Enter the website name: ")
x=int(input("\n\nconfirm website name?\n 1=yes 0=no\n"))

if(x==1):
  html_doc=requests.get(websitename).text
  string=input("\n\nEnter word you wish to search for: ")
  x=html_doc.count(string)
  print("\n\nOccourances of",string,"as an entire word are: ",x)
  print("\n\nPlease note that this does not contain places where",string,"may come in between other words")

elif(x==0):
  websitename=input("\n\nRe-Enter website name: ")
  html_doc=requests.get(websitename).text
  string=input("\n\nEnter word you wish to search for: ")
  x=html_doc.count(string)
  print("\n\nOccourances of ",string,"as an entire word are: ",x)
  print("\n\nPlease note that this does not include places where",string,"may come inbetween other words")

else:
  print("\n\nEnter valid option")

