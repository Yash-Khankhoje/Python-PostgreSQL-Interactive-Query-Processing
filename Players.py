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
                cur.execute("CREATE TABLE players(id SERIAL PRIMARY KEY, name VARCHAR(255), points INT)")

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
                    Points = int(input("points = "))
                    Query = "INSERT INTO players(name,points) VALUES(" + "'" + Name + "'" + "," + str(Points) + ")"
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
                        cur.execute("DROP TABLE IF EXISTS players.")

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
                    print("If you want to drop the row by using points then type[POINTS/Points/points]")
                    print("If you want to drop all rows except a perticular points then type [POINTSEXCET/PointsExcept/pointsexcept]")
                    print("If you want to delete all the rows having points less than a perticular points then type[POINTSLESS/PointsLess/pointsless]")
                    print("If you want to delete all the rows having points greater than a perticular points then type[POINTSGREAT/PointsGreat/pointsgreat]")
                    print("If you want to drop rows in range of points then tupe[POINTSRANGE/PointsRange/pointsrange]")
                    print("If you want to drop rows which are not in the range of points then tupe[POINTSERANGEEXCEPT/PointsRangeExcept/pointsrangeexcept]")
                    print("If you want to exit from this function then please type exit[EXIT/Exit/exit")
                    print("Enter your option : ")
                    RowDelOpt = str(input())
                    if RowDelOpt.lower() == "id":
                        while True:
                            try:
                                with con:
                                    #cur = con.cursor()
                                    cur = con.cursor()

                                    pid = str(input("id = "))
                                    cur.execute("DELETE from players WHERE id={0}".format(pid))
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
                                    pid = str(input("id = "))
                                    cur.execute("DELETE  from players WHERE id != {0}".format(pid))
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
                                    pname = str(input("name = "))
                                    cur.execute("DELETE  from players WHERE name ={0}".format(pname))
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
                                    pname = str(input("name = "))
                                    cur.execute("DELETE  from players WHERE name !={0}".format(pname))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "points":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("DELETE  from players WHERE points = {0}".format(ppoints))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "pointsexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("DELETE  from players WHERE points !={0}".format(ppoints))
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
                                    pid = str(input("id = "))
                                    cur.execute("DELETE  from players WHERE id <{0}".format(pid))
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
                                    pid = str(input("id = "))
                                    cur.execute("DELETE  from players WHERE id >{0}".format(pid))
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
                                    cur.execute("DELETE  from players WHERE id between {0} and {1}".format(idlow, idhigh))
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
                                    cur.execute("DELETE  from players WHERE id not between {0} and {1}".format(idlow, idhigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowDelOpt.lower() == "pointsless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("DELETE  from players WHERE points <{0}".format(ppoints))
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
                                    uprice = str(input("points = "))
                                    cur.execute("DELETE  from cars WHERE points > {0}".format(uprice))
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
                                    pointslow = str(input("base points = "))
                                    pointshigh = str(input("upper points = "))
                                    cur.execute("DELETE  from players WHERE points between {0} and {1}".format(pointslow, pointshigh))
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
                                    pointselow = str(input("base points = "))
                                    pointshigh = str(input("upper points = "))
                                    cur.execute("DELETE  from players WHERE points not between {0} and {1}".format(pointslow, pointshigh))
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
            print("If you wnt to select entire table then type [SELECTTABLE/SelectTable/selecttable]")
            print("If you want to select any row of the table then type[selectROW/selectRow/selectrow]\n")

            print("Please enter your choice.")
            SelectOption = str(input())
            if SelectOption.lower() == "selecttable":
                try:
                    with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM TABLE IF EXISTS players.")

                except:
                    print("Error:The table does not exist.")

            elif SelectOption.lower() == "selectrow":
                while True:
                    print("If you want to select the row by using i'd then type [ID/Id/id]")
                    print("If you want to select all rows except a perticular i'd then type [IDEXCET/IdExcept/idexcept]")
                    print("If you want to select all the rows having id less than a perticular id then type[IDLESS/IdLess/idless]")
                    print("If you want to select all the rows having id greater than a perticular id then type[IDGREAT/IdGreat/idgreat]")
                    print("If you want to select rows in range of id then tupe[IDRANGE/IdRange/idrange]")
                    print("If you want to select rows which are not in the range of id then tupe[IDRANGEEXCEPT/IdRangeExcept/idrangeexcept]")
                    print("If you want to select the row by using name then type[NAME/Name/name]")
                    print("If you want to select all rows except a perticular name then type [NAMEEXCET/NameExcept/nameexcept]")
                    print("If you want to select the row by using points then type[POINTS/Points/points]")
                    print("If you want to select all rows except a perticular points then type [POINTSEXCET/PointsExcept/pointsexcept]")
                    print("If you want to select all the rows having points less than a perticular points then type[POINTSLESS/PointsLess/pointsless]")
                    print("If you want to select all the rows having points greater than a perticular points then type[POINTSGREAT/PointsGreat/pointsgreat]")
                    print("If you want to select rows in range of points then tupe[POINTSRANGE/PointsRange/pointsrange]")
                    print("If you want to select rows which are not in the range of points then tupe[POINTSERANGEEXCEPT/PointsRangeExcept/pointsrangeexcept]")
                    print("If you want to exit from this function then please type exit[EXIT/Exit/exit")
                    print("Enter your option : ")
                    RowSelOpt = str(input())
                    if RowSelOpt.lower() == "id":
                        while True:
                            try:
                                with con:
                                    # cur = con.cursor()
                                    cur = con.cursor()

                                    pid = str(input("id = "))
                                    cur.execute("Select * from players WHERE id={0}".format(pid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "idexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pid = str(input("id = "))
                                    cur.execute("Select * from players WHERE id != {0}".format(pid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "name":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pname = str(input("name = "))
                                    cur.execute("Select * from players WHERE name ={0}".format(pname))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "nameexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pname = str(input("name = "))
                                    cur.execute("Select * from players WHERE name !={0}".format(pname))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "points":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("Select * from players WHERE points = {0}".format(ppoints))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "pointsexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("Select * from players WHERE points !={0}".format(ppoints))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "idless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pid = str(input("id = "))
                                    cur.execute("Select * from players WHERE id <{0}".format(pid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "idgreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pid = str(input("id = "))
                                    cur.execute("Select * from players WHERE id >{0}".format(pid))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "idrange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("low id = "))
                                    idhigh = str(input("Upper id = "))
                                    cur.execute("Select * from players WHERE id between {0} and {1}".format(idlow, idhigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "idrangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    idlow = str(input("low id = "))
                                    idhigh = str(input("upper id = "))
                                    cur.execute("Select * from players WHERE id not between {0} and {1}".format(idlow, idhigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "pointsless":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    ppoints = str(input("points = "))
                                    cur.execute("Select * from players WHERE points <{0}".format(ppoints))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "pricegreat":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    uprice = str(input("points = "))
                                    cur.execute("Select * from cars WHERE points > {0}".format(uprice))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "pricerange":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pointslow = str(input("base points = "))
                                    pointshigh = str(input("upper points = "))
                                    cur.execute("Select * from players WHERE points between {0} and {1}".format(pointslow,
                                                                                                       pointshigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

                    if RowSelOpt.lower() == "pricerangeexcept":
                        while True:
                            try:
                                with con:
                                    cur = con.cursor()
                                    pointselow = str(input("base points = "))
                                    pointshigh = str(input("upper points = "))
                                    cur.execute("Select * from players WHERE points not between {0} and {1}".format(pointslow,
                                                                                                           pointshigh))
                                    InnerOption = str(input("Do you want to continue ?:[yes/no]"))
                                    if InnerOption.lower() == "no" or InnerOption.lower() != "yes":
                                        break

                            except:
                                print("Error occeared...")

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
                    ppoints = int(input("points = "))
                    pname= str(input("name = "))
                    cur.execute("UPDATE players SET points=%s WHERE name=%s", (ppoints, pname))
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