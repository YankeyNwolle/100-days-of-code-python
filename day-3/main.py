print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("BIENVENUE A Treasure Island.")
print("Ta mission est de trouver le tresor") 

first_step = input("Tape gauche ou Droite \n gauche/droite").lower()

# les conditions 

if first_step == "droite":
    print('''                      -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
  ''')
    print("Sonic a pris le trésor tu perds cette manche !!!.")

elif first_step == "gauche":
    print("Bien joué vous avez atteint les 1/3 du trésor 🎉")

    second_step = input("Tape manger ou dormir \n manger/dormir : ").lower()
    if second_step == "dormir":
        print("vous perdez cette manche !!!!")
    elif second_step == "manger":
        print("Bien joué vous avez terminez les 2/3 du trésor 🎉")
    else:
        print("veuillez entrez le bon mot  🌚")
        second_step = input("Tape manger ou dormir \n manger/dormir : ").lower()


    third_step = int(input("Tape entre 1 ou 2 \n 1/2"))
    if third_step == 1:
        print("vous perdez cette manche !!!")
    elif third_step == 2:
        print("Bravo vous avez remporté le trésor 🚀")
    else:
        print("veuillez entrez le bon chiffre 🦥")
        third_step = int(input("Tape entre 1 ou 2 \n 1/2"))


else:
    print("veuillez entrez le bon mot 🌚")
    first_step = input("Tape gauche ou Droite \n gauche/droite").lower()


    

