#!/usr/bin/python

from sys import exit
from cifrados import *

def menu_entrada():
    print '------Welcome to de-cifer-machine!!------\n'
    print '--what did you want to do?(choise a option)'
    print '-(1) descifer cesar'
    print '-(2) cifer in cesar'
    print '-(3) show all options of a descifer in cesar'
    print '-(4) show all options of a cifer in cesar'
    print '-(5) reverse text'
    print '-(6) change the letters in the word'
    print '-(7) exit'

    option = int(input('> '))

    if option <= 7 or option >= 1:
        clase = cifrado_cesar()

        if option == 1:
            palabra_cifrada = raw_input("> Introduce the cifer word: ")
            cantidad_a_mover = int(input("> Tell me the number of characters: "))

            print '> ' + clase.cifrador_en_cesar(palabra_cifrada, cantidad_a_mover)

            loop()

        if option == 2:
            palabra_cifrada = raw_input("> Introduce the word that do you want to cifer: ")
            cantidad_a_mover = int(input("> Tell me the number of characters: "))

            print '> ' + clase.cifrador_en_cesar(palabra_cifrada, cantidad_a_mover)

            loop()
            
        if option == 3:
            palabra_cifrada = raw_input("> Introduce the word that do you want to cifer: ")

            for i in range(0, 26):
                print '> ' + clase.cifrador_en_cesar(palabra_cifrada, i)
            loop()
            
        if option == 4:
            palabra_cifrada = raw_input("> Introduce the word that do you want to decifer: ")
            for i in range(0, 26):
                print '> ' + clase.cifrador_en_cesar(palabra_cifrada, i)
            loop()
        
                
        if option == 5:
            mirror = raw_input("> Introduce the word do you want to reverse: ")
            print '> ' + clase.reversar(mirror)
            loop()


        if option == 6:
            print '-to view all comands whrite: comands()-'
            cadena_para_cambiar = raw_input("> Introduce the word do you want to change the letters: ")
            clase.cambio_letras(cadena_para_cambiar)
            loop()
            
        if option == 7:
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
