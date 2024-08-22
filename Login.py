import _pickle
import os
import time
import calendar
import pickle

#from Book_Maker_file_1 import *



ACCOUNT_FILE = "accounts.pkl"
aNone="BAD"
def read_account_file(filename):
    try:
      with open(filename, 'rb') as file:
        return pickle.load(file)
    except _pickle.UnpicklingError:
      return {}
    except FileNotFoundError:
      return {}
def read_write_fun(filename):
  try:
    with open(filename, 'rb') as file:
      return pickle.load(file)
  except FileNotFoundError:
    return {None}

def write_account_file(filename, accounts):
    with open(filename, 'wb') as file:
        pickle.dump(accounts, file)
def write(filename, accounts):
  with open(filename, 'wb') as file:
      pickle.dump(accounts, file)
accounts=read_account_file(ACCOUNT_FILE)
#let's debug
#while username in accounts:
#print (accounts)
#for elem in accounts:

#  print(name = elem, password =accounts[elem])




what_to_do = input('Make a new account, login, or delete? (N/L/D)')
time.sleep(2)
os.system('clear')
if what_to_do.lower() == 'n':
  print("You want to make a new account.")
  time.sleep(2)
  os.system('clear')
  username = input("What is your username?")
  if username in accounts:
    while username in accounts:
      print("That username is already taken. Abort!")
      time.sleep(2)
      os.system('clear')
  password = input("What is your password?")
  accounts[username] = password

elif what_to_do.lower() == 'l':
  print("You're trying to login.")
  username = input("What is your username?")
  print(f'you entered {username}')

  if username in accounts:
    password = input("What is your password1?")
    print(f'you entered {password}')
    print(f'correct password is {accounts[username]}')
    print(password)
    if password == accounts[username]:
      print("You are logged in!")
    else:
      print("Wrong password!")
      os.system('clear')
      exit()
  else:
    print("HACKER LOGGING IN!")
    print(accounts)
    os.system('clear')
    exit()
    #tries=tries+1
if what_to_do.lower()=='d':
  print("You want to delete an account.")
  username=input("what is the account name?")
  if username in accounts:
    password = input("What is your password?")
    if password not in accounts:
      print("Wrong password! Abort!")
      exit()
    else:
      del accounts[username]
      print("Account deleted!")
      exit()



print('Welcome,')
print('saving...')
inp= input("press any key to exit")
os.system('clear')
write_account_file(ACCOUNT_FILE, accounts)
print(accounts)
