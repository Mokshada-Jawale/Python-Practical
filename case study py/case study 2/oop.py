from sys import stdin
from datetime import date
def inlist(): return list(map(int, stdin.readline().strip().split()))

class person:
    def __init__(self,name,dob,dept):
        self.name=name
        self.dob=dob
        self.dept=dept

class employee(person):
    tot_sal = 0
    def __init__(self,name,dob,dept,id,sal):
        self.empID=id
        self.salary=sal
        person.__init__(self,name,dob,dept)

class student(person):
    def __init__(self,name,dob,dept,prn,yr,cgpa):
        self.prn=prn
        self.year=yr
        self.cgpa=cgpa
        person.__init__(self,name,dob,dept)
    def dispInfo(self):
        x="Name: {}\nDate-of-Birth: {}\nDepartment: {}\nPRN: {}\nYear: {}\nCGPA: {}".format(self.name,self.dob,self.dept,self.prn,self.year,self.cgpa)
        print(x)
    deptAvg={}
    def calAvgCgpa(self):
        if i.dept in self.deptAvg:
            self.deptAvg[i.dept][0]+=i.cgpa
            self.deptAvg[i.dept][1]+=1

        else:
            self.deptAvg[i.dept]=[i.cgpa,1]

class lab_asst(employee):
    def __init__(self,name,dob,dept,empid,sal,labs):
        self.labs=labs
        employee.__init__(self,name,dob,dept,empid,sal)
    def dispInfo(self):
        x="Name: {}\nDate-of-Birth: {}\nDepartment: {}\nEmployee ID: {}\nSalary: {}\nLabs: {}".format(self.name,self.dob,self.dept,self.empID,self.salary,', '.join(map(str, self.labs)))
        print(x)

class faculty(employee):
    def __init__(self,name,dob,dept,eid,sal,subjects,res,quali):
        self.subjects=subjects
        self.researches=res
        self.qualification=quali
        employee.__init__(self,name,dob,dept,eid,sal)

    def dispInfo(self):
        x="Name: {}\nDate-of-Birth: {}\nDepartment: {}\nEmployee ID: {}\nSalary: {}\nSubject: {}\nNumber of research papers: {}\nQualification: {}".format(self.name,self.dob,self.dept,self.empID,self.salary,self.subjects,self.researches,self.qualification)
        print(x)

def dispAll(faculties, assistants, students):
    print("-" * 5, "Displaying all data", "-" * 5)
    print("--------------------Data of faculty--------------------")
    for i in faculties:
        i.dispInfo()
        print()
    print("--------------------Data of Lab Assistants--------------------")
    for i in assistants:
        i.dispInfo()
        print()
    print("--------------------Student data--------------------")
    for i in students:
        i.dispInfo()
        print()

def help():
    print('''
            1. Display all data
            2. Delete a data
            3. Display total salary of all employees.
            4. Find average CGPA of students Department wise
            Enter x for exit''')


if __name__=="__main__":
    asst1=lab_asst("Sagar",date(1992,7,23),"Computer","e001",50000,["b1","b2"])
    asst2=lab_asst("Mandar",date(1995,11,26),"IT","e002",50000,["b3","b2"])
    fac1=faculty("XYZ",date(1985,11,18),"Computer","e003",100000,"DLDM",1,"M.Tech")
    fac2=faculty("PQR",date(1981,2,28),"IT","e004",120000,"DAA",2,"M.E.")
    fac3=faculty("LMN",date(1986,6,22),"IT","e005",80000,"Electronics",2,"M.Tech")
    fac4=faculty("ABC",date(1979,3,10),"Computer","e006",150000,"Python",4,"PhD")
    stud1=student("Mokshada",date(2002,11,26),"Computer","2030331245023",2,9.83)
    stud2=student("Hemangi",date(2002,4,29),"Computer","2030331245019",2,9.62)
    stud3=student("Devyani",date(2002,2,5),"IT","2030331246008",2,8.15)
    stud4=student("Manasi",date(2002,5,20),"Computer","2030331245029",2,8.1)
    stud5=student("Sanskruti",date(2002,7,24),"IT","2030331246032",2,8.75)
    assistants=[asst1,asst2]
    faculties=[fac1,fac2,fac3,fac4]
    students=[stud1,stud2,stud3,stud4,stud5]
    help()
    while True:
        choice=input("Enter your choice: ")
        if choice=='1':
            dispAll(faculties,assistants,students)
        elif choice=='2':
            x = input("Enter whose data do you want to delete(1. Student 2. Employee): ")
            if x == '1':
                id = input("Enter PRN: ")
                for i in students:
                    if i.prn == id:
                        students.remove(i)
                        del i
                        break
                else:
                    print("PRN not found..")
            elif x == '2':
                id = input("Enter Employee ID: ")
                for i in faculties+assistants:
                    if i.empID == id:
                        try:
                            assistants.remove(i)
                            del i
                        except:
                            faculties.remove(i)
                            del i
                        break
                else:
                    print("Employee ID not found..")
            else:
                print("Invalid Input")
        elif choice=='3':
            tot_sal=sum([i.salary for i in assistants+faculties])
            print("Total salary of all employees is ",tot_sal)
        elif choice=='4':
            for i in students:
                i.calAvgCgpa()
            print("The department wise average CGPA are: ")
            for i in student.deptAvg:
                print(i,':',student.deptAvg[i][0]/student.deptAvg[i][1])

        elif choice in 'xX':
            break
        else:
            help()