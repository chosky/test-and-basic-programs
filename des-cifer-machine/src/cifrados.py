class cifrado_cesar(object):

    #metodo para cifrar y des-cifrar en cesar
    def cifrador_en_cesar(self, palabra_cifrada, cantidad_a_mover):

        palabra_sin_cifrar = ''
        palabra_cifrada = palabra_cifrada.lower()
        
        for i in range(len(palabra_cifrada)):

            if ord(palabra_cifrada[i]) == 40:
                i += 1
                continue

            if ord(palabra_cifrada[i]) > 122 or ord(palabra_cifrada[i]) < 97:
                palabra_sin_cifrar += palabra_cifrada[i]
                
            
            if (ord(palabra_cifrada[i]) + cantidad_a_mover) >= 122:
                
                resta = (ord(palabra_cifrada[i]) + cantidad_a_mover) - 122
                suma = 97 + resta
            
                palabra_sin_cifrar += chr(suma)

                continue

        
            palabra_sin_cifrar += chr(ord(palabra_cifrada[i]) + cantidad_a_mover)
        
        return palabra_sin_cifrar


    
    #Metodo para revertir una palabra
    def reversar(self, mirror):
        normal = []

        i = len(mirror)

        while i:
            i -= 1

            normal.append(mirror[i])

        return ''.join(normal)



    #Metodo de cambio de letras en una cadena
    def cambio_letras(self, cadena_para_cambiar):
        cadena_para_cambiar_original = cadena_para_cambiar
        cadena_cambiada = ''
        comands = ['exit', 'show', 'reverse', 'reset']

        #meter al ciclo
        letra_index = raw_input('> What letter do you want to change?: ')
        letra_a_cambiar = raw_input('> Change' + letra_index + ' for?: ')


        #cambiar ciclo para que trabaje con caracteres (excepcion con string)
        while letra_index != 'exit' or letra_a_cambiar != 'exit':
            if letra_a_cambiar == 'comands' or letra_index == 'comands':
                print '--comands--'
                print 'exit: to exit'
                print 'show: to show original word'
                print 'reverse: to reverse the last change'
                print 'reset: to reset the word to the original state'

            if letra_a_cambiar in comands or letra_index in comands:
                letra_index = letra_a_cambiar

                if letra_index == 'exit':
                    print 'llamar al metodo loop del main'
                    #exit()

                if letra_index == 'show':
                    print cadena_para_cambiar_original

                if letra_index == 'reverse':
                    print 'falta'

                if letra_index == 'reset':
                    cadena_para_cambiar = cadena_para_cambiar_original
                    print cadena_para_cambiar


            print '> original word:\n' + cadena_para_cambair_original
            print '> word with changes:\n ' + cadena_cambiada
