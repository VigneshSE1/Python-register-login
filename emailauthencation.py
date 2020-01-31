import re

username_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
password_regex = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

database={}
my_dict={}
updated_dict={}

def username_check():
    username = input("Enter Username\n")
    if(re.search(username_regex,username)):
        return username
    else:
        print("Enter valid username")
        username_check()

def password_check():
    password = input("Enter Password\n")
    if(re.findall(password_regex,password)):
        return password
    else:
        print("Enter valid password")
        password_check()

def sign_up(name_data,password_data):
    database[name_data]=password_data
    f = open("dictfile.txt","r")
    readfile = f.read()
    edited = str(readfile)
    edited = edited.strip("{")
    edited = edited.strip("}")

    aftersplit = edited.split(",")
    #print(aftersplit)
    for i in aftersplit:
        l,m  = i.strip().split(":")
        my_dict[l.strip()] = m.strip()

    for s, t in my_dict.items():
        updated_dict[s.strip("'")] = t.strip("'")

    updated_dict.update(database)

    f = open("dictfile.txt", "w")
    result = str(updated_dict)
    f.write(result)
    f.close()

def log_in(name_data,password_data):
    database[name_data]=password_data
    f = open("dictfile.txt", "r")
    readfile = f.read()
    edited = str(readfile)
    edited = edited.strip("{")
    edited = edited.strip("}")

    aftersplit = edited.split(",")
    # print(aftersplit)
    for i in aftersplit:
        l, m = i.strip().split(":")
        my_dict[l.strip()] = m.strip()

    for s, t in my_dict.items():
        updated_dict[s.strip("'")] = t.strip("'")

    if(database.items()<=updated_dict.items()):
        print("Access Granted")
    else:
        print("Create Account")


select = input(" Enter S for SIGN UP / L for LOGIN \n")
if (select == 's'or select =='S'):
    name_data = username_check()
    password_data = password_check()
    sign_up(name_data,password_data)

    #print(name_data)
    #print(password_data)
    #print("signup")
elif(select == 'l' or select == 'L'):
    name_data = username_check()
    password_data = password_check()
    log_in(name_data,password_data)
   #print("Login")
else:
    print("Enter vaild option")

