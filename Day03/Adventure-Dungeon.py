# Adventure Dungeon
print('''
 _________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \   
  |                            _-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \

 ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'----SSt
     ``----....(','
            _,'>'
            )/
            `'
''')
print("Welcome to DUNGEON.")
print("Your mission is to find the treasure.")

enter = input("Would you like to enter the dungeon or go back ? \"y\" or \"n\" ")

if enter.lower() == 'y':
    go_to_room = int(input("You see two rooms in front of you which one to enter ? '1'or '2' "))

    if go_to_room == 1:
        print("You won there it is the treasure")

    elif go_to_room == 2:
        print("A monster in this room and the door is closed GG !")

    else:
        print("Wrong choice!")

else:
    print("You saved your life this time !!")
