import psycopg2
import psycopg2.extras
import sys
import Players as T6
import Cars as T8

while True:
    try:
        print("If you want to work on \"cars\" table then please type[CARSTABLE/CarsTable/carstable]")
        print("If you want to work on \"players\" table then please type[PLAYERSTABLE/PlayersTable/playerstable]")
        print("If you want to exit then please press [EXIT/Exit/exit/BREAK/Break/break]")
        Option = str(input("Please input your opion"))
        if Option.lower() == "cars":
            while True:
                #############################################################
                # Operations List
                #############################################################
                print("\n")
                print("If you want to create a new table then please type [CREATE/Create/create] ")
                print("If you want to insert data into your table then please type [INSERT/Insert/insert]")
                print("If you want to fire select query then type [SELECT/Select/select]")
                print("If you want to update data of your table then please type[UPDATE/Update/update]")
                print("If you want to delete the table then please press[DELETE/Delete/delete")
                print("If you want to exit then please type[EXIT/Exit/exit]\n")

                print("Please enter your option[Create/Insert/Select/Update/Delete/Exit] :\t")
                Option1 = str(input())
                if Option1.lower() == "create":
                    T8.CreateTable()

                elif Option1.lower() == "insert":
                    T8.Insertion()

                elif Option1.lower() == "delete":
                    T8.Deletion()

                elif Option1.lower() == "select":
                    T8.Selection()

                elif Option1.lower() == "update":
                    T8.Updation()

                elif Option1.lower() == "exit":
                    sys.exit()

        elif Option.lower() == "players":
            while True:
                #############################################################
                # Operations List
                #############################################################
                print("\n")
                print("If you want to create a new table then please type [CREATE/Create/create] ")
                print("If you want to insert data into your table then please type [INSERT/Insert/insert]")
                print("If you want to fire select query then type [SELECT/Select/select]")
                print("If you want to update data of your table then please type[UPDATE/Update/update]")
                print("If you want to delete the table then please press[DELETE/Delete/delete")
                print("If you want to exit then please type[EXIT/Exit/exit]\n")

                print("Please enter your option[Create/Insert/Select/Update/Delete/Exit] :\t")
                Option1 = str(input())
                if Option1.lower() == "create":
                    T6.CreateTable()

                elif Option1.lower() == "insert":
                    T6.Insertion()

                elif Option1.lower() == "delete":
                    T6.Deletion()

                elif Option1.lower() == "select":
                    T6.Selection()

                elif Option1.lower() == "update":
                    T6.Updation()

                elif Option1.lower() == "exit":
                    sys.exit()

        else:
            break


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
        print("Thank you...")