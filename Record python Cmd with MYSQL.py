#=======================================================================================================
#created on 17-08-2020

#created by    Rohit Kumar Prajapati


#modules required

#  1)  mysql.connector    -  For connection between python and mysql
#  2)  Tabulate           -  For table formate of data presentation
#  3)  email_validator    -  For email validation



#ID - auto increment primary key
#UID - user input ID (its simailar to ID that provided by any company and organisation(User ID no))
#FirstName -First Name
#LastName - Last Name
#Age  - Age
#Email- Email
#reg_date = data entry/registration date

#mysql database name- "pythondata"
#Table creation query #Table name "User"

#  #CREATE TABLE User (
#  #ID INT(6) AUTO_INCREMENT PRIMARY KEY,
#  #UID int(4) NOT NULL,
#  #FirstName VARCHAR(30) NOT NULL,
#  #LastName VARCHAR(30) NOT NULL,
#  #Age int(3),
#  #Email VARCHAR(50),
#  #Reg_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);


# user record using cmd python


##############################NOTE#################################################################################################

#   It can store duplicate data if found any solution for that please update me Thank you !
#####################################################################################################################################




import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from email_validator import validate_email, EmailNotValidError


   
#===================================================================Connection======================================================
try:
    connection = mysql.connector.connect(host='localhost',database='pythondata',user='root',password='Root@123')
    print("DB is Connected !\n")
        

    if connection.is_connected():
        db_Info = connection.get_server_info()
        #print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()         #connected to db
        cursor.execute("select database();") #using cursor run cmd of mysql
        DB = cursor.fetchone()           #stored data in cursor is stored in DB
        #print("You're connected to database: ", DB)

except Error as e:
    print("Connection failed !", e)

#===================================================User Input ==================================================================
def main():

    a=int(input("Please select the action you want to perform :\n\n 1. View All Records \n 2. Insert Data \n 3. Delete Data \n 4. Search Data \n 5. Update the Data \n\n Enter Value Here : "))
    if(a==1):
        cursor.execute("select * from User")
        rec=cursor.fetchall()
        
        print(tabulate(rec, headers=['ID', 'UID','First_Name','Last_Name','Age','Email','Register_Date'], tablefmt='psql'))
        main()

#================================insert====================================================================

    elif(a==2):
        try:
            UID=int(input("Enter UID of User : "))
            fname=input("Enter First Name : ")
            lname=input("Enter Last Name : ")
            age=int(input("Enter Age : "))
            if (age<10):
                print("Age is  below 10 year! Registration Not Required ! \n")
                main()
            email=input("Enter Valid Email : ")
            
            valid = validate_email(email) #validate using email_validator module

                # Update with the normalized form.
            email = valid.email
               
            print("\n")
        except EmailNotValidError as e:
            print("Please Enter Valid Details !!\n")
            print(str(e),"\n\n")
            main()
            
        print("Please check entered information is correct or Not \n\n","UID        : ",UID,"\n First Name : ",fname,"\n","Last Name  : ",lname,"\n","Age        : ",age,"\n","Email      : ",email,"\n")
        
        Yes_no=input("Yes / No : ").lower()
        if (Yes_no=="yes") or (Yes_no=="y"):
            try:
                cursor.execute("INSERT INTO User (UID,FirstName,LastName,Age,Email) VALUES (%s,%s,%s,%s,%s)",(UID,fname,lname,age,email))
                connection.commit()
                print("Record inserted successfully !")
                main()
            except:
                connection.rollback()
                print("Something went wrong !")
                main()
        else:
            print("Please Fill the details Again !\n")
            main()


#=====================================Delete====================================================

    elif(a==3):
        try:
            delete=int(input("Enter UID to delete the record :"))
            cursor.execute("select * from User where UID = %s",(delete,))
            del_rec=cursor.fetchall()
            #print(del_rec)
            print(tabulate(del_rec, headers=['ID', 'UID','First_Name','Last_Name','Age','Email','Register_Date'], tablefmt='psql'))
            dec=input("Are sure you want to delete this record ! (yes/no) : ").lower()
            if(dec=="yes"):
                try:
                    cursor.execute("Delete from User where UID = %s",(delete,))
                    connection.commit()
                    print("Record Deleted Successfully !")
                    main()
                except:
                    connection.rollback()
                    print("Something went wrong couldn't perform delete operation !")
                    main()
        except:
            print("Something went wrong couldn't perform delete operation !")
            main()

#==========================================Search=====================================================================

    elif(a==4):
        try:
            sel=int(input(" Enter UID to search perticular record : "))
            
            cursor.execute("select * from User where UID = %s",(sel,))
            
            #checking record exixts or not

            data="error"   #assigning data
            rec=cursor.fetchall()
            
            for i in rec:
                data=i        #if record is present it will updated "data"
            if data=="error": #if not then data="error"
                print ("It Does not Exist")
            else :            #otherwise data is present it will display the data
                print("Here is the Details of searched record !\n")
                #print data in tabular format
                print(tabulate(rec, headers=['ID', 'UID','First_Name','Last_Name','Age','Email','Register_Date'], tablefmt='psql')) #works only fetchall
                main()
            
                # print(rec1)
                # for row in rec1:      #other way  # work on fetchone
                #     print("ID         = ", row[0])
                #     print("UID        = ", row[1])
                #     print("FirstName  = ", row[2])
                #     print("LastName   = ", row[3])
                #     print("Age        = ", row[4])
                #     print("Email      = ", row[5])
                #     print("Reg_Date   = ", row[6],"\n")
        except:
            print("Something went wrong Unable to search ! Enter valid input !\n")     
            main()

#=======================================================Update=============================================================

    elif(a==5):
        try:
            upd=int(input("Enter UID to Update the record :"))
            cursor.execute("select * from User where UID = %s",(upd,))
            upd_rec=cursor.fetchall()
            #print(del_rec)
            print(tabulate(upd_rec, headers=['ID', 'UID','First_Name','Last_Name','Age','Email','Register_Date'], tablefmt='psql'))
            dec=input("Are sure you want to Update this record ! (yes/no) : ").lower()
            if(dec=="yes"):
                try:
                    try:
                        print("!!! Please Enter values for all the field !!!\n")
                        UID1=int(input("Update UID of User : "))
                        fname1=input("Update First Name : ")
                        lname1=input("Update Last Name : ")
                        age1=int(input("Update Age : "))
                        if (age1<10):
                            print("Age is  below 10 year! Registration Not Required ! ")
                            main()

                        email1=input("Update Email : ")
                        valid = validate_email(email1)  # validate using email_validator

                        # Update with the normalized form.
                        email1 = valid.email
               
                        print("\n")
                    except EmailNotValidError as e:
                        print("Please Enter Valid Details !!\n")
                        print(str(e),"\n\n")
                        main()
                    
                    cursor.execute("Update User set UID = %s,FirstName=%s,LastName=%s,Age=%s,Email=%s where UID = %s",(UID1,fname1,lname1,age1,email1,upd))
                    connection.commit()
                    print("Record Updated Successfully !")
                    cursor.execute("select * from User where UID = %s",(upd,))
                    upd_rec=cursor.fetchall()
                    #print(del_rec)
                    print(tabulate(upd_rec, headers=['ID', 'UID','First_Name','Last_Name','Age','Email','Register_Date'], tablefmt='psql'))
                    main()
                except:
                    connection.rollback()
                    print("Something went wrong couldn't perform delete operation !")
                    main()
        except:
            print("Something went wrong couldn't perform Update operation !")
        print("Aborted !")
        main()
    else:
        print("Please enter valid input !")
        main()

    
    connection.close()  
main()


