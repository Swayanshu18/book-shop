import pickle

import os

def write_file():

                f= open("book shop.dat","wb")

                ch='y'

                while ch =='y':

                                l={}

                                booknumber=int(input("bno"))

                                bookname=input("enter name")

                                price=int(input("enter price"))

                                qty=int(input("enter quantity"))

                                t=(booknumber,bookname,price,qty)

                                pickle .dump(t,f)

                                k=input("Do you want to continue further ?y/n:")

                f.close()

 

def read_file():

    file=open("book shop.dat","rb")

    try:

        while True:

            l1={}

            l1=pickle.load(file)

            print(l1)

    except EOFError:

        pass

    file.close() 

 

def sort_file():

    file=open("book shop.dat","rb")

    l1=[]

    try:

        while True:

            rec={}

            rec=pickle.load(file)

            l1.append(rec)

    except EOFError:

        pass

    file.close()

    print(l1)

    for i in range(0,len(l1)):

        for j in range(0,len(l1)-i-1):

            if l1[j]['price']>l1[j+1]['price']:

                l1[j],l1[j+1]=l1[j+1],l1[j]

    print(l1)

    file=open("book shop.dat","wb")

    for i in l1:

        pickle.dump(i,file)

    file.close()

def search_file():

    rec={}

    f = open('book shop.dat','rb')

    flag = False

    r=int(input("Enter booknumber to be searched"))

    while True:

        try:

            rec = pickle.load(f)

            if rec['booknumber'] == r:

                print('Book number:',rec['booknumber'])

                print('Name:',rec['bookname'])

                print('quantity:',rec['qty'])

                print('price:',rec['price'])

                flag = True

        except EOFError:

            break

    if flag == False:

        print('No Records found')

    f.close()


 

def update_file():

    f=open('book shop.dat','rb+')

    flag=False

    p=0

    rec={}

    r=int(input("book number to search"))

    m=int(input("enter price to update"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['book number']:

                rec['price']=m

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

                                   
def del_file():

    f=open('book shop.dat','rb')

    f1=open('temp.dat','wb')

    flag=False

    p=0

    rec={}

    r=int(input("enter book number to search"))

    try:

        while True:

            rec=pickle.load(f)

            if r== rec['booknumber']:

                flag=True

            else:

                pickle.dump(rec,f1)

    except EOFError:

           pass

    f.close()

    f1.close()

    if flag==True:

        print("Record deleted")

    else:

        print("Record not found")

    os.remove("book shop.dat")

    os.rename("temp.dat","book shop.dat")

 


 

def sor1_file():

    file=open("book shop.dat","rb")

    l1=[]

    try:

        while True:

            rec={}

            rec=pickle.load(file)

            l1.append(rec)

    except EOFError:

        pass

    file.close()

    print(l1)

    for i in range(0,len(l1)):

        for j in range(0,len(l1)-i-1):

            if l1[j]['booknumber']>l1[j+1]['booknumber']:

                l1[j],l1[j+1]=l1[j+1],l1[j]

    print(l1)

    file=open("book shop.dat","wb")

    for i in l1:

        pickle.dump(i,file)

    file.close()

 

def updat1_file():

    f=open('book shop.dat','rb+')

    flag=False

    p=0

    rec={}

    r=int(input("enter book  number to search"))

    m=int(input("enter quantity to purchased"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['booknumber']:

                rec['qty']=rec['qty']+m

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

 

 

def updat2_file():

    f=open('book shop.dat','rb+')

    flag=False

    x=0

    p=0

    rec={}

    r=int(input("enter book number to search"))

    m=int(input("enter quantity to sold"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['itemno']:

                rec['qty']=rec['qty']-m

                x=x+m*rec['price']

                print("total price",x)

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

 


 

#main prog

ch= 0

while ch!=10:

    print("File Handling ")

    print("1. Create file")

    print("2. Show file")

    print("3. Search file")

    print("4. Update file for price ")

    print("5. Sort file to sort by price")

    print("6.Delete record")

    print("7.sor1 record for sort by book number ")

    print("8.updat1record for buying book")

    print("9.update2record for selling book ")

    print("10. Exit")

    ch=int(input("Enter Choice(1-10)"))

    if ch==1:

          write_file()

    elif ch==2:

          read_file()

    elif ch==3:

          search_file()

    elif ch==4:

          update_file()

    elif ch==5:

          sort_file()

    elif ch==6:

          del_file()

    elif ch==7:

          sor1_file()

    elif ch==8:

          updat1_file()

    elif ch==9:

          updat2_file()

 

    elif ch==10:

          print("Quitting")

else:

          print("Invalid Choice")
