# Library
books={"SG Gupta":8,"RP Jain":5,"TH Cormen":13,"HC Verma":0,"Galvin":10,"KH Rosen":6,"Let's C":17,"Python":5,"BB Singh":4}
def display():
    print("The available books are: ")
    available=[i for i in books if books[i]>0]
    print(available)

def issue():
    book=input("Enter the book name: ")
    if book in books and books[book]>0:
        books[book]-=1
        print(book,"issued successfully")
    else:
        print("The entered books is not available")

def returnn():
    book=input("Enter the book name to return: ")
    books[book]+=1
    print(book,"returned successfully")

def help():
    print(''' Choose the function:
            1. Display available books
            2. Issue a book
            3. Return a book
            Enter any other key for help menu
            Enter q to exit
            ''')

if __name__=='__main__':
    help()
    while True:
        key=str(input("Enter your choice: "))
        if key=='1':
            display()
        elif key=='2':
            issue()
        elif key=='3':
            returnn()
        elif key in 'Qq':
            print("ThankYou")
            break
        else:
            help()
