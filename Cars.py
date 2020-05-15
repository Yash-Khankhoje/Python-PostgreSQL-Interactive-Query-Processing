##############################################################
# Importing required libraries.
##############################################################
import sys
import psycopg2
import psycopg2.extras

##############################################################
# User data declearation.
##############################################################
UserName = str(input("Please enter the user name      : "))
DataBase = str(input("Please enter the database name  : "))
Password = str(input("Please enter your password      : "))
con = None

try:
    #########################################################
    # User authentication.
    #########################################################
    con = psycopg2.connect(user=UserName, database=DataBase, password=Password)


    #########################################################
    # Function to create table.
    #########################################################
    def CreateTable():
        try:
            with con:
                cur = con.cursor()

                # cur.execute("DROP TABLE IF EXISTS cars")
                cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")

        except:
            print("Error : The table already exists...")


    ##########################################################
    # Function to insert data into the table.
    ##########################################################
    def Insertion():
        try:
            while True:
                with con:
                    cur = con.cursor()
                    Name = str(input("name = "))
                    Price = int(input("Price = "))
                    Query = "INSERT INTO cars(name,price) VALUES(" + "'" + Name + "'" + "," + str(Price) + ")"
                    cur.execute(Query)
                    print("Row added successfully.")
                    print("\nDo you want to insert one more row ? [yes/no]\t")
                    InsertionOption = str(input())
                    if InsertionOption.lower() == "no" or InsertionOption.lower() != "yes":
                        break

        except:
            print("Error:Unexpected error occeared while inserting the row... ")


    ##########################################################
    # Function to perform deletetion operation
    ##########################################################
    def Deletion():
        while True:
            print("If you wnt to drop entire table then type [DROPTABLE/DropTable/droptable]")
            print("If you want to drop any row of the table then type[DROPROW/DropRow/droprow]\n")

            print("Please enter your choice.")
            DeleteOption = str(input())
            if DeleteOption.lower() == "droptable":
                try:
                    with con:
                        cur = con.cursor()
                        cur.execute("DROP TABLE IF EXISTS cars.")

                except:
                    print("Error:The table does not exist.")

            elif DeleteOption.lower() == "droprow":
                while True:
                    print("If you want to drop the row by using i'd then type [ID/Id/id]")
                    print("If you want to drop all rows except a perticular i'd then type [IDEXCET/IdExcept/idexcept]")
                    print("If you want to delete all the rows having id less than a perticular id then type[IDLESS/IdLess/idless]")
                    print("If you want to delete all the rows having id greater than a perticular id then type[IDGREAT/IdGreat/idgreat]")
                    print("If you want to drop rows in range of id then tupe[IDRANGE/IdRange/idrange]")
                    print("If you want to drop rows which are not in the range of id then tupe[IDRANGEEXCEPT/IdRangeExcept/idrangeexcept]")
                    print("If you want to drop the row by using name then type[NAME/Name/name]")
                    print("If you want to drop all rows except a perticular name then type [NAMEEXCET/NameExcept/nameexcept]")
                    print("If you want to drop the row by using price then type[PRICE/Price/price]")
                    print("If you want to drop all rows except a perticular price then type [PRICEEXCET/PriceExcept/priceexcept]")
                    print("If you want to delete all the rows having price less than a perticular price then type[PRICELESS/PriceLess/priceless]")
                    print("If you want to delete all the rows having price greater than a perticular price then type[PRICEGREAT/PriceGreat/pricegreat]")
                    print("If you want to drop rows in range of price then tupe[PRICERANGE/PriceRange/pricerange]")
                    print("If you want to drop rows which are not in the range of price then tupe[PRICERANGEEXCEPT/PriceRangeExcept/pricerangeexcept]")

                    print("Enter your option : ")
                    RowDelOpt = str(input())
                    if RowDelOpt.lower() == "id":
                        while True:
                            try:
                                with con:
                                    #cur = con.cursor()
                                    cur = con.cursor()

                                    uid = str(input("id = "))
                                    cur.execute("DELETE from cars WHERE id={0}".format(uid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "idexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("DELETE  from cars WHERE id != {0}".format(uid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "name":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uname = str(input("name = "))
                                    cur.execute("DELETE  from cars WHERE name ={0}".format(uname))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "nameexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uname = str(input("name = "))
                                    cur.execute("DELETE  from cars WHERE name !={0}".format(uname))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "price":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    cprice = str(input("price = "))
                                    cur.execute("DELETE  from cars WHERE price = {0}".format(cprice))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "priceexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    cprice = str(input("price = "))
                                    cur.execute("DELETE  from cars WHERE price !={0}".format(cprice))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "idless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("DELETE  from cars WHERE id <{0}".format(uid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "idgreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input())
                                    cur.execute("DELETE  from cars WHERE id >{0}".format(uid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "idrange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("low id = "))
                                    idhigh = str(input("Upper id = "))
                                    cur.execute("DELETE  from cars WHERE id between {0} and {1}".format(idlow, idhigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "idrangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("low id = "))
                                    idhigh = str(input("upper id = "))
                                    cur.execute("DELETE  from cars WHERE id not between {0} and {1}".format(idlow, idhigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "priceless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uprice = str(input("price = "))
                                    cur.execute("DELETE  from cars WHERE price <{0}".format(uprice))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "pricegreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uprice = str(input("price"))
                                    cur.execute("DELETE  from cars WHERE price > {0}".format(uprice))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "pricerange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pricelow = str(input("base price = "))
                                    pricehigh = str(input("upper price = "))
                                    cur.execute("DELETE  from cars WHERE price between {0} and {1}".format(pricelow, pricehigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "pricerangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pricelow = str(input("base price = "))
                                    pricehigh = str(input("upper price = "))
                                    cur.execute("DELETE  from cars WHERE price not between {0} and {1}".format(pricelow, pricehigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

            else:
                break


    ##########################################################
    # Select query function
    ##########################################################
    def Selection():
        while True:
            print("If you wnt to read entire table then type [SELECTALL/SelectAll/selectall]")
            print("If you want to select perticular row of the table then type[SELECTROW/SelectRow/selectrow]\n")

            print("Please enter your choice.")
            SelectOption = str(input())
            if SelectOption.lower() == "selectall":
                try:
                    with con:
                        cur = con.cursor()
                        cur.execute("Select * from cars")

                        rows = cur.fetchall()

                        for row in rows:
                            print(f"{row[0]} {row[1]} {row[2]}")

                except:
                    print("Error:The table does not exist.")

            elif SelectOption.lower() == "selectrow":
                while True:
                    print("If you want to read the row by using i'd then type [ID/Id/id]")
                    print("If you want to read all rows except a perticular i'd then type [IDEXCET/IdExcept/idexcept]")
                    print("If you want to read all the rows having id less than a perticular id then type[IDLESS/IdLess/idless]")
                    print("If you want to read all the rows having id greater than a perticular id then type[IDGREAT/IdGreat/idgreat]")
                    print("If you want to read rows in range of id then tupe[IDRANGE/IdRange/idrange]")
                    print("If you want to read rows which are not in the range of id then tupe[IDRANGEEXCEPT/IdRangeExcept/idrangeexcept]")
                    print("If you want to read the row by using name then type[NAME/Name/name]")
                    print("If you want to read all rows except a perticular name then type [NAMEEXCET/NameExcept/nameexcept]")
                    print("If you want to read the row by using price then type[PRICE/Price/price]")
                    print("If you want to read all rows except a perticular price then type [PRICEEXCET/PriceExcept/priceexcept]")
                    print("If you want to read all the rows having price less than a perticular price then type[PRICELESS/PriceLess/priceless]")
                    print("If you want to read all the rows having price greater than a perticular price then type[PRICEGREAT/PriceGreat/pricegreat]")
                    print("If you want to read rows in range of price then tupe[PRICERANGE/PriceRange/pricerange]")
                    print("If you want to read rows which are not in the range of price then tupe[PRICERANGEEXCEPT/PriceRangeExcept/pricerangeexcept]")

                    print("Enter your option : ")
                    RowSelectOpt = str(input())
                    if RowSelectOpt.lower() == "id":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("SELECT * from cars WHERE id={0}".format(uid))
                                    rows = cur.fetchone()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "idexcept":
                        while True:
                            try:

                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("SELECT * from cars WHERE id != {0}".format(uid))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "name":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uname = str(input("name = "))
                                    cur.execute("SELECT * from cars WHERE name = {0}".format(uname))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "nameexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uname = str(input("name = "))
                                    cur.execute("SELECT * from cars WHERE name !={0}".format(uname))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "price":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    cprice = str(input("price = "))
                                    cur.execute("SELECT * from cars WHERE price ={0}".format(cprice))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "priceexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    cprice = str(input("price = "))
                                    cur.execute("SELECT * from cars WHERE price != {0}".format(cprice))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "idless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("SELECT * from cars WHERE id <{0}".format(uid))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "idgreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uid = str(input("id = "))
                                    cur.execute("SELECT * from cars WHERE uid > {0}".format(uid))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "idrange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("base id = "))
                                    idhigh = str(input("upper id = "))
                                    cur.execute("SELECT * from cars WHERE id between {0} and {1}".format(idlow, idhigh))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "idrangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("base id ="))
                                    idhigh = str(input("upper id = "))
                                    cur.execute("SELECT * from cars WHERE id not between {0} and {1}".format(idlow, idhigh))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "priceless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uprice = str(input("price = "))
                                    cur.execute("SELECT * from cars WHERE price < {0}".format(uprice))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "pricegreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uprice = str(input("price = "))
                                    cur.execute("SELECT * from cars WHERE price > {0}".format(uprice))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "pricerange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pricelow = str(input("base price = "))
                                    pricehigh = str(input("upper price = "))
                                    cur.execute("SELECT * from cars WHERE price between {0} and {1}".format(pricelow, pricehigh))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    if RowSelectOpt.lower() == "pricerangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pricelow = str(input("low price = "))
                                    pricehigh = str(input("high price = "))
                                    cur.execute("SELECT * from cars WHERE price not between {0} and {1}".format(pricelow, pricehigh))
                                    rows = cur.fetchall()
                                    for row in rows:
                                        print(f"{row[0]} {row[1]} {row[2]}")
                                    print("Job done")
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break


                            except:
                                print("Error occeared...")

                    else:
                        break

            else:
                break



    ##########################################################
    # Updation Function
    ##########################################################
    def Updation():
        try:
            while True:
                with con:
                    cur = con.cursor()
                    uPrice = int(input("price = "))
                    cName = str(input("name = "))
                    cur.execute("UPDATE cars SET price=%s WHERE name=%s", (uPrice, cName))
                    print(f"Number of rows updated: {cur.rowcount}")
                    InsertionOption = str(input("Do you want to Update anything else ? [yes/no]"))
                    if InsertionOption.lower() == "no" or InsertionOption.lower() != "yes":
                        break
        except:
            print("Error: Data not updated...")





############################################################
# Except block.
############################################################
except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

############################################################
# Finally block.
############################################################
finally:
    if con:
        con.close()