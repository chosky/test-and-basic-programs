from sys import exit
from cifrado_cesar import *

def menu_entrada():
    print '------Welcome to de-cifer-machine!!------\n'
    print '--what did you want to do?(choise a option)'
    print '-(1) descifer cesar'
    print '-(2) cifer in cesar'
    print '-(3) show all options of a descifer in cesar'
    print '-(4) show all options of a cifer in cesar'
    print '-(5) reverse text'
    print '-(6) exit'

    option = int(input('> '))

    if option <= 6 or option >= 1:
    
        if option == 1:
            palabra_cifrada = raw_input("> Introduce the cifer word: ")
            cantidad_a_mover = int(input("> Tell me the number of characters: "))

            clase = cifrado_cesar()
            print '> ' + clase.cifrador_en_cesar(palabra_cifrada, cantidad_a_mover)

            loop()

        if option == 2:
            palabra_cifrada = raw_input("> Introduce the word that do you want to cifer: ")
            cantidad_a_mover = int(input("> Tell me the number of characters: "))

            clase = cifrado_cesar()
            print '> ' + clase.cifrador_en_cesar(palabra_cifrada, cantidad_a_mover)

            loop()
            
        if option == 3:
            palabra_cifrada = raw_input("> Introduce the word that do you want to cifer: ")

            clase = cifrado_cesar()
            for i in range(0, 26):
                print '> ' + clase.cifrador_en_cesar(palabra_cifrada, i)

            loop()
            
        if option == 4:
            palabra_cifrada = raw_input("> Introduce the word that do you want to decifer: ")

            clase = cifrado_cesar()
            for i in range(0, 26):
                print '> ' + clase.cifrador_en_cesar(palabra_cifrada, i)

            loop()
        
                
        if option == 5:
            mirror = raw_input("> Introduce the word do you want to reverse: ")
            clase = cifrado_cesar()

            print '> ' + clase.reversar(mirror)

            loop()
                
        if option == 6:
            exit()
                
    else:
        print '> that number doesn\'t a option.'
        menu_entrada()




def loop():
    print '\n'
    print '----What did you want to do?-----'
    print '-(1) Go to menu'
    print '-(2) Exit'

    option = int(input('> '))

    if option < 2 or option > 1:
        if option == 1:
            menu_entrada()

        if option == 2:
            exit()
            
    else:
        print '> that number doesn\'t a option.'
        loop()



    
menu_entrada()    
