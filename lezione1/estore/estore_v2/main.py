from costumer import *
from storeItem import *
from store_inventory import StoreInventory
from store import Store
from ui import *
import os
import time

users = createUsers() # dizionario di tutti gli utenti registrati

i1 = GenericItem(111, 9.99)
i2 = NormalItem(222, 19.99, "Laptop", "A high-performance laptop for work and gaming.")
i3 = ForeignItem(333, 29.99, "Smartphone", "A sleek smartphone with advanced features.", "China")
i4 = GenericItem(444, 4.99)


store_inventory1 = StoreInventory()

store_inventory1.addItem(i1)
store_inventory1.addItem(i2)
store_inventory1.addItem(i3)
store_inventory1.addItem(i4)

store = Store(store_inventory1, 1000)

letto = " "

userLogin = ""

os.system('clear')

while(letto != '3'):
    #Caso nessun utente registrato
    if(os.path.getsize("users.txt") == 0):
        os.system('clear')
        print("------Menu Register------\n")
        nome = input("Insert your username: ")
        password = input("Chose a password : ")
        saldo = input("Insert your initial balance: ")
        c1 = GenericCostumer(nome, password, float(saldo))
        users[nome] = c1
        with open("users.txt", "a", encoding='utf-8') as f:
            f.write(nome + "," + password + ","+saldo+"\n")

    
    print("------Menu Login------\n")
    letto = input("1. Login\n2. Register\n3. exit\n4. Users\n---> ")

    #Login
    if(letto=='1'):
        while(1):
            nome = input("Insert your username: ")
            if(nome not in users):
                print("\nUser does not exist! Register before\n")
                time.sleep(2)
                os.system('clear')
                break
            else:  
                while(1):
                    password = input("Insert your password: ")
                    if(users[nome].checkPassword(password)):
                        print("\nLogin successful!\n")
                        userLogin = nome
                        # Menu dello store
                        while(letto!= '6'):
                            print(f"Benvenuto {userLogin}\n-------MENU-------\n 1. Display Store Inventory\n 2. Buy Item by ID\n 3. Find Item by ID\n 4. Visualizza Saldo\n 5. Ricarica saldo \n6. Exit\n")
                            letto = input("---> ")

                            if(letto== '1'):
                                os.system('clear')
                                store.displayInventory()
                                print("\n\n")
                                            
                            elif(letto == '2'):
                                buy = input("Insert the ID : ")
                                os.system('clear')
                                buyItemById(int(buy), users[userLogin], store_inventory1, store)
                                            
                            elif (letto == '3'):
                                find = input("Insert the ID : ")
                                os.system('clear')
                                findItemById(store_inventory1, int(find))
                            elif(letto == '4'):
                                os.system('clear')
                                print("\n-> Your current balance is: ", users[userLogin].saldoAttuale(), "\n")  
                            elif(letto == '5'):
                                os.system('clear')
                                ricarica = input("Insert the amount to recharge: ")
                                users[userLogin].incrementaSaldo(float(ricarica))
                                with open("users.txt", "w", encoding='utf-8') as f:
                                    for user in users.values():
                                        f.write(user.__str__() + "\n")
                                print("\n-> Your new balance is: ", users[userLogin].saldoAttuale(), "\n") 
                            
                            elif(letto == '6'):
                                break
                        userLogin = ""
                        os.system('clear')
                        break    
                    else:
                        print("\nWrong password, try again.\n")
                            
            break

    #Register
    elif(letto=='2'):
        os.system('clear')
        print("------Menu Register------\n")
        nome = ''
        while(1):
            nome = input("Insert your username: ")
            if(nome in users):
                print("\nUsername already exists, try another one.\n")
            else:  break
        time.sleep(1)
        password = input("Chose a password : ")
        saldo = input("Insert your initial balance: ")
        c1 = GenericCostumer(nome, password, saldo)
        users[nome] = c1
        with open("users.txt", "a", encoding='utf-8') as f:
            f.write(nome + "," + password + "," + saldo +"\n")
    
    elif(letto=='4'):
        os.system('clear')
        print("------Users------\n")
        for user in users.values():
            print(user)
        print("\n\n")
    


            
           