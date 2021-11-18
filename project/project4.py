import websocket
import json
import pandas as pd
import mplfinance as mpf
import matplotlib.animation as animation
import dateutil.parser
import datetime
import threading
import time
from datetime import date, datetime, timedelta

menuList = ["1", "2", "3", "4", "5", "6"]
currencyList = ["BTC", "ETH", "XRP", "BNB", "FTM", "SOL", "VET"]
menu = "1"
userList = []
loginStatus = False
line1 = "="*85


def header(text):
    print(f"{text.center(70)}")
    print(line1)


def register():
    header("REGISTER")
    username = input("Enter username : ")
    password = input("Enter password : ")
    userList.append({
        "username": username,
        "password": password
    })
    print("Register Success!!!")


def login():
    header("LOGIN")
    username = input("Enter username : ")
    password = input("Enter password : ")
    checkUsername = [i for i, key in enumerate(
        userList) if username in key.values()]
    checkPassword = [i for i, key in enumerate(
        userList) if password in key.values()]
    if len(checkUsername) and len(checkPassword) != 0:
        print("Login Success!!!")
        loginStatus = True
    else:
        print("Invalid Username or Password...")
        loginStatus = False

    return loginStatus


def viewCurrencyList():
    for i in currencyList:
        print("%-9s%-10s%s" % ("|", i, "|"))


def liveGraph():
    print("HI")


def byPass():
    loginStatus = True
    return loginStatus


while menu in menuList:
    print(line1)
    print("1.Register | 2. Login | 3.Interesting currency | 4.View currency live price | 5.Exit ")
    print(line1)
    menu = input("Enter you menu : ")
    print(line1)

    if menu == "1":
        register()
    if menu == "2":
        loginStatus = login()

    # Check Login Status
    if menu == "3" and loginStatus == False:
        print("Login Please...")
    elif menu == "3" and loginStatus == True:
        viewCurrencyList()

    # Check Login Status
    if menu == "4" and loginStatus == False:
        print("Login Please...")
    elif menu == "4" and loginStatus == True:
        liveGraph()

    if menu == "6":
        loginStatus = byPass()
