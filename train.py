"""
welcome message
print quota names & select
enter source to destonation place and search for trains
print list of trains
"""




quota="""
1.GENERAL
2.TATKAL
3.LADIES
"""


import time
import datetime
import random

print(25*"*","welcome to IRCTC",25*"*")
print("Book  your train tickets:")
print(25*"=",25*"=")
# option=input("for Quota names press yes:")
# if option=="yes":
#     print(quota)
# select=input("select your quota:")
select1=input("source and destination press yes:")
option1=input("from:")
if option1=="yes":
    print("enter source:")
# select2=input("enter source and destination press yes")
option2=input("To:")
if option2=="yes":
    print("enter destination:")
list_of_trains="""
chennai_express:12345,
tirupathi_express:45678,
eastcoast:9876,
venkatadri_express:45321,
janmabhumi:45678,
vandhebharat:23456
"""
print("search for trains:")
print(25*"=",25*"=")
print(list_of_trains)
train=input("choose your train:")
passenger=int(input("enter number of passengers:"))
option=input("for Quota names press yes:")
if option=="yes":
    print(quota)
select=input("select your quota:")
seat=input("select_seat_type:")
print("for ticket conformation plz enter your details")
name=input("enter your name:")
gender=input("enter your gender:")
age=input("enter your age:")
phone=input("enter your pnone number:")
ticketrate={"chennai_express":'240',"tirupasthi_express":'500',"eastcoast":'630',"venkatadri_express":"450","janmabumi":'480',"vandhebharat":'1100'}
if train in ticketrate:
    print("ticket_rate:",ticketrate[train])
    print("totalprice:",int(ticketrate[train])*passenger)
user_date=int(input("enter your reservation date:"))
print("  ")
date=datetime.datetime(2023,2,user_date)
print("your reservation date:",date)
print("your ticket was  reserved:",datetime.datetime.now())
user_date=int(input("enter your reservation date:"))
inp=input("generating the ticket.........")
if inp=="yes":
    pass
print(50*"*","HAPPY JOURNEY",50*"*")
print(50*"  ","PNRNO",random.randint(11111,1000000))  
print(60*"*",60*"*")
print("name:",name,30*" ")
# print("train:",train,30*" ")
# print(40*" ","train",train)

# print(50*" ","passenger:",passenger)
print("train:",train,30*" ",10*" ","passenger:",passenger,10*" ","datetime:",datetime)
# print(50*" ","passenger:",passenger)


              












