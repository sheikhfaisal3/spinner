# luck spin

import random
import time
names =  []

loop = True
user = input("Enter names (once you finish type done): ")
while loop:
    if user == "done".lower():
        k = ""
        for name in names:
            k = name + "," + k
        print()
        print("Name of the players are :",k)
      
        loop = False
        for i in range (len(names)):
            print()
            ask = input("press S for spin: ").upper()
            if ask == "S":
                random_n = random.choice(names)
                names.remove(random_n)
                print("spinning...........")
                print()
                time.sleep(3)
                print(random_n," has been eliminated")
                k = ""
                for name in names:
                    k = name + "," + k
                print("Remaining players are :",k)
                print()
                if len(names) == 1:
                    print(name,"is winner")
                    print("Congrats ", name,"You have won this lucky spin game")
                    break
    else:
        names.append(user)
        user = input("Enter names (once you finish type done): ")
        






        

        
            


    

