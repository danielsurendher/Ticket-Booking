from atexit import register
from datetime import datetime
import random
import string
import time
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="railway"
)

cur = con.cursor()
def add_train():
        
        tname = input("Train Name: ")
        destination = input("Destination: ")
        total_seats = int(input("Total Seats: "))
        
        sql = """
        INSERT INTO trains
        (NAME, DESTINATION,total_seats,available_seats)
        VALUES (%s,%s,%s,%s)
        """

        val = (tname,destination,total_seats,total_seats)

        cur.execute(sql, val)
        con.commit()
        
        print("-"*5,"Train Added Successfully","-"*5)

def delete_train():
        tno = int(input("Enter Train Number: "))

        cur.execute(
                "DELETE FROM trains WHERE TNO=%s",
                (tno,)
        )

        con.commit()

        print("-"*5,"Train Deleted Successfully","-"*5)
def view_trains():
        cur.execute("SELECT * FROM trains")
        rows = cur.fetchall()

        print("-"*10,"Train Details","-"*10)
       
        print(f"{'TNO':<5}{'NAME':<20}{'DESTINATION':<20}{'TOTAL SEATS':<15}{'AVAILABLE SEATS':<15}")
        print("-" * 80)
        for row in rows:
                print(f"{row[0]:<5}{row[1]:<20}{row[2]:<20}{row[3]:<15}{row[4]:<15}")
       

def update_train():
        tno = int(input("Enter Train Number: "))
        name = input("Train Name: ")
        destination = input("Destination: ")

        sql = """
        UPDATE trains
        SET NAME=%s, DESTINATION=%s
        WHERE TNO=%s
        """

        val = (name, destination, tno)

        cur.execute(sql, val)

        con.commit()

        print("-"*5,"Train Updated Successfully","-"*5)
def add_passenger():  
       
        cur.execute("SELECT * FROM trains")
        rows = cur.fetchall()

        print("-"*10,"Train Details","-"*10)
        print("-" * 80)
        print(f"{'TNO':<5}{'NAME':<20}{'DESTINATION':<20}{'TOTAL SEATS':<15}{'AVAILABLE SEATS':<15}")
        for row in rows:
                print(f"{row[0]:<5}{row[1]:<20}{row[2]:<20}{row[3]:<15}{row[4]:<15}")
       
        pnr_no = random.randint(1000000000, 9999999999)
        ticket_no = random.randint(10000, 99999)
        seat_no = random.randint(1, 100)
        name = input("Passenger Name: ")
        age = Age()
        gender = input("Gender: ")
        source = input("Source: ")
        destination = input("Destination: ")
        train = input("Train Name: ")
        MOBILE= input("Contact.NO (+91): ")
        
        if len(MOBILE)== 10 :
                if MOBILE[0] in ("6","7","8","9") and MOBILE[1] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[2] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[3] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[4] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[5] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[6] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[7] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[8] in ("0","1","2","3","4","5","6","7","8","9") and MOBILE[9] in ("0","1","2","3","4","5","6","7","8","9") and len(MOBILE)== 10:
                        print("Valid")
                        
                else:
                        print("Invalid : Only Numbers and Should be the valid Phone number.....!")
                
        else:
                print("Invalid : Should Contain Ten Digits..!")
                return
        aadhar=input("Enter Aadhar Number: ")
        
        if aadhar.isdigit() and len(aadhar) == 12:
                print("Valid")  
                print("\n")
                

        
        else:
                print("Invalid : Enter the Correct Aadhaar Number...!")
                return
        

        while True:
                booking_time = input("Enter Journey Date & Time (YYYY-MM-DD HH:MM): ")

                try:
                        journey_dt = datetime.strptime(booking_time, "%Y-%m-%d %H:%M")

                        if journey_dt < datetime.now():
                                print("Past date/time is not allowed!")
                        else:
                                break

                except ValueError:
                        print("Invalid format. Use YYYY-MM-DD HH:MM")

        amount = 0
        print("Pick Your Payment options")
        print("1. Gpay")
        print("2. phonepe")
        print("3. Paytm")
        payment_choice = int(input("Enter Choice: "))
        if payment_choice == 1:
                print("You have selected Gpay")
                amount = int(input("Enter Amount: "))
        elif payment_choice == 2:
                print("You have selected phonepe")      
                amount = int(input("Enter Amount: "))
        elif payment_choice == 3:
                print("You have selected Paytm")
                amount = int(input("Enter Amount: "))
        else:
                print("Invalid Choice")
                return
                       
        sql = """
        INSERT INTO tickets
        (ticket_no,pnr_no,passenger_name, age, gender, source, destination, train_name,seat_no,pay_option,amount,booking_datetime,MOBILE,aadhar)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        val = (ticket_no,pnr_no,name, age, gender, source, destination, train, seat_no,payment_choice,amount,booking_time,MOBILE,aadhar)

        cur.execute(sql, val)
        con.commit()

        print("-"*5,"Ticket Booked Successfully","-"*5)
        print("-"*5,"Ticket Number:", ticket_no,"-"*5)
        print("-"*5,"PNR Number:", pnr_no,"-"*5)
        cur.execute(
                """UPDATE trains SET available_seats = available_seats - 1 WHERE NAME=%s""",
    (train,)
)
        con.commit()
        cur.execute(
                "SELECT available_seats FROM trains WHERE NAME=%s",
                (train,)
                )
        row = cur.fetchone()
        if row is None:
            print("Train Not Found")
            return
def view_tickets():

        cur.execute("SELECT * FROM tickets")
        rows = cur.fetchall()

        print("-"*63,"Ticket Details","-"*63)
        print(f"{'TICKET NO':<10}{'NAME':<15}{'AGE':<5}{'GENDER':<10}{'SOURCE':<10}{'DESTINATION':<20}{'TRAIN':<20}{'PNR NO':<15}{'SEAT NO':<10}{'PAYMENT OPTION':<20}{'AMOUNT':<10}{'BOOKING TIME':<20}")
        print("-" * 144)
        for row in rows:
                print(f"{row[0]:<10}{row[1]:<15}{row[2]:<5}{row[3]:<10}{row[4]:<10}{row[5]:<20}{row[6]:<20}{str(row[7]):<15}{row[8]:<15}{row[9]:<15}{row[10]:<10}{str(row[11]):<20}")

def cancel_ticket():
    tno = int(input("Enter Ticket Number: "))

    
    cur.execute(
        "SELECT train_name FROM tickets WHERE ticket_no=%s",
        (tno,)
    )

    row = cur.fetchone()

    if row is None:
        print("Ticket Not Found")
        return

    train_name = row[0]

    
    cur.execute(
        "DELETE FROM tickets WHERE ticket_no=%s",
        (tno,)
    )

    
    cur.execute(
        """
        UPDATE trains
        SET available_seats = available_seats + 1
        WHERE NAME=%s
        """,
        (train_name,)
    )

    con.commit()

    print("Ticket Cancelled Successfully")

def check_pnr():
    pnr = int(input("Enter PNR Number: "))

    cur.execute(
        "SELECT * FROM tickets WHERE pnr_no=%s",
        (pnr,)
    )

    row = cur.fetchone()

    if row:
        print(row)
    else:
        print("PNR Not Found")
     
      
def enter():
        print("="*10,"Welcome to Railway Ticket Booking System","="*10)
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter Choice: "))
        if choice == 1:
                if register():
                        return True
                else:
                        return False
        elif choice == 2:
                if login():
                        return True
                else:
                        return False
        elif choice == 3:
                exit()
                return False
        else:
                print("Invalid Choice")
                return False
def Age():
    AGE=(input("Age:"))
    if AGE.isdigit():
        AGE = int(AGE)
        if 1<= AGE <= 116:
            print("Valid Age:",AGE)
            print("\n")
            return AGE
        else:
            print("Invalid Age: Please enter a correct age between 1 and 150.")
            Age()
    else:
        print("Invalid Input: Please enter a valid numeric age.")
        Age()

def captcha():
        print("\nPlease Verify You're Not A Robot\n")
        for x in range(1,4):
                characters = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
        captcha = characters
        print("Captcha= ",captcha)
        CAP1= input("Type Down The Captcha:")
        if CAP1 == captcha :
            print("Verified: Valid Captcha")
            print("\n")
            main()
        else :
            print("Invalid Captcha..Retry")
        print("Maximum Number of Tries Over.....!")
        print("Wait For 10 Seconds....!")
        for x in range(10,0,-1):
          print(x,end=" ")
        x+=1 
        time.sleep(1)
        print("\n")
        print("Now you can Retry....!")
        for x in range(1,4):
          characters = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
        captcha = characters
        print("Captcha= ",captcha)
        CAP1= input("Type Down The Captcha:")
        if CAP1 == captcha :
            print("Verified: Valid Captcha")
            print("\n")
            main()
        else :
            print("Invalid Captcha..Retry")
        print("Maximum Number of Tries Over.....!")
        print("Wait For 20 Seconds....!")
        for x in range(10,0,-1):
           print(x,end=" ")
        x+=1 
        time.sleep(1)
        print("\n")
        print("Now you can Retry for Three times more....!")
        for x in range(1,4):
           characters = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
        captcha = characters
        print("Captcha= ",captcha)
        CAP1= input("Type Down The Captcha:")
        if CAP1 == captcha :
            print("Verified: Valid Captcha")
            print("\n")
            main()
        else :
                print("Invalid Captcha..Retry")
        print("Maximum Number of Tries Over.....!")
        print("Now you cannot Retry You're not Verified....!")
        
def register():
        print("="*10,"Register a new account","="*10,"\n\n")
        username = input("Username: ")
        password = input("Password: ")
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        row = cur.fetchone()

        if row:
                print("Username already exists")
        else:
        
                cur.execute(       "INSERT INTO users(username,password) VALUES(%s,%s)",
                (username,password)
    )
        con.commit()
        print("Registration Successful\n")
        login()
def login():
        print("="*10,"Login to your account","="*10,"\n\n")
        username = input("Username: ")
        password = input("Password: ")

        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        val = (username, password)

        cur.execute(sql, val)

        row = cur.fetchone()

        if row:
                print("Login Successful")
                captcha()
                return True
        
        else:
                print("Invalid Username or Password")
                login()
                return False
                
def exit():
        print("Do you want to exit or continue?")
        print("1. Exit")
        print("2. Continue")
        choice = int(input("Enter Choice: "))
        if choice == 1:
                print("Thank You for using Railway Ticket Booking System")
                con.close()
        elif choice == 2:
                enter()
        print("Thank You for using Railway Ticket Booking System")
        con.close()

def main():
 
    while True:
        print("="*10,"ADDING TRAINS","="*10)
        print("1. Add Train")
        print("2. View Trains")
        print("3. Update Train")
        print("4. Delete Train")

        print("="*10,"RAILWAY TICKET BOOKING","="*10)
        print("5. Book Ticket")
        print("6. View Tickets")
        print("7. Cancel Ticket")
        print("8. Check PNR")
        print("9. Exit")

       
        choice = int(input("Enter Choice: "))
        if choice == 1:
                add_train()
        elif choice == 2:
                view_trains()
        elif choice == 3:
                update_train()
        elif choice == 4:
                delete_train()
        elif choice == 5:
                add_passenger()
         
        elif choice == 6:
                view_tickets()
        elif choice == 7:
                cancel_ticket()
        elif choice == 8:
                check_pnr()
        elif choice == 9:
                exit()
                
                break
        else:
                print("Invalid Choice")    
                break 
 
enter()