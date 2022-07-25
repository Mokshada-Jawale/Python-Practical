import mysql.connector
from tabulate import tabulate
from datetime import date

def DisplayAll():
    cur.execute("select * from students;")
    a = cur.fetchall()
    li = []
    cur.execute("desc students")
    aa = cur.fetchall()
    for i in aa:
        li.append(i[0])
    print(tabulate(a,headers=li))

def DisplayNameAge():
    cur.execute("select First_name,Middle_name,last_name,DOB from students;")
    x = cur.fetchall()
    today = date.today()
    li=[]
    for i in x:
        age = today-i[-1]
        #print(age.days//365)
        li.append((i[0]+" "+i[1]+" "+i[2],age.days//365))
    print(tabulate(li,headers=["NAME","AGE"]))

def AddRecord():
    prn=input("Enter the PRN: ")
    Fname = input("Enter First name: ").upper()
    Mname = input("Enter Middle name: ").upper()
    Lname = input("Enter Last name: ").upper()
    add = input("Enter Address: ").upper()
    mobile = input("Enter Mobile Number: ")
    email = input("Enter email id: ").lower()
    dob = input("Enter date of birth(yyyy-mm-dd): ")

    add = "insert into students values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prn,Fname,Mname,Lname,add,mobile,email,dob)
    cur.execute(add)
    x = cur.fetchall()
    mycon.commit()
    print("Record Added Successfully")
    print("New data is: ")
    DisplayAll()

def DeleteUser():
    prn = input("Enter the Prn whose record is to be Deleted: ")
    d = "Delete from students where prn ="+prn
    cur.execute(d)
    mycon.commit()
    print("Record deleted Successfully")
    print("Remaining data is: ")
    DisplayAll()

def UpdateNumEmail():
    prn = input("Enter the Prn whose record is to be Updated: ")
    mob = input('Enter New Mobile Num: ')
    email = input('Enter New Email: ')
    u = "update students set Mobile_num='{}',Email='{}' where prn='{}'".format(mob,email,prn)
    cur.execute(u)
    mycon.commit()
    print("Database updated successfully")
    up = "select * from students where prn="+prn
    cur.execute(up)
    y = cur.fetchall()
    print(y)
    DisplayAll()

def AddCGPA(flag):
    if flag:
        query = "ALTER TABLE STUDENTS ADD COLUMN CGPA FLOAT"
        cur.execute(query)
        mycon.commit()
        print("\n CGPA field added successfully...\n")
        cur.execute("SELECT PRN FROM STUDENTS")
        x = cur.fetchall()
        for i in x:
            prn = i[0]
            print("Enter the CGPA of PRN ", prn, end=': ')
            cgpa = float(input())
            query = "UPDATE STUDENTS SET CGPA='{}' WHERE PRN='{}'".format(cgpa, prn)
            cur.execute(query)
            mycon.commit()
        return False
    else:
        print("The field CGPA already exists.")
        return True

def functions():
    print('''
            1. Display the database
            2. Display name and age of all students
            3. Add record 
            4. Delete a record
            5. Update email and Phone number
            6. Add column CGPA
            Enter any other key to exit
    ''')

if __name__ == "__main__":
    print("Welcome to DBATU Second year Computer Engineering Department")
    print("--" * 30)
    mycon = mysql.connector.connect(host="localhost", user="root", password="mokshada", database="dbatu_secondyear")
    cur = mycon.cursor()
    global flag
    flag = False
    try:
        cur.execute("ALTER TABLE STUDENTS DROP COLUMN CGPA")
    except:
        pass
    flag = True
    if mycon.is_connected():
        functions()
        while True:
            opt = input("Select your choice(h for help): ")
            if opt == '1':
                DisplayAll()
            elif opt == '2':
                DisplayNameAge()
            elif opt == '3':
                AddRecord()
            elif opt == '4':
                DeleteUser()
            elif opt == '5':
                UpdateNumEmail()
            elif opt == '6':
                flag = AddCGPA(flag)
            elif opt in 'hH':
                functions()
            else:
                break
    else:
        print("Unable to connect to MySQL")


#print(mycon.is_connected())
#DisplayAll()
#AddRecord()
#DeleteUser()
#UpdateNumEmail()




