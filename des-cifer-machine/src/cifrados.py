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
        return mirror[::-1]
        #algoritm
        """normal = []
        i = len(mirror)

        while i:
            i -= 1
            normal.append(mirror[i])

        return ''.join(normal)"""



    #Metodo de cambio de letras en una cadena
    def cambio_letras(self, cadena_para_cambiar):
        cadena_para_cambiar_original = cadena_para_cambiar
        cadena_cambiada = ''
        comands = ['exit()', 'show_original()', 'show_change()', 'reverse()', 'reset()']

        while True:
                        
            letra_index = raw_input('> What letter do you want to change?: ')
            letra_a_cambiar = raw_input('> Change ' + letra_index + ' for?: ')

            
            if len(letra_a_cambiar) == 1 and len(letra_index) == 1:
                cadena_cambiada = cadena_para_cambiar
                print '> original word:\n' + cadena_para_cambiar_original
                cadena_para_cambiar = cadena_para_cambiar.replace(letra_index, letra_a_cambiar)
                print '> word with changes:\n ' + cadena_para_cambiar
                

            if letra_a_cambiar == 'comands()' or letra_index == 'comands()':
                print '--comands--'
                print 'exit():          to exit'
                print 'show_original(): to show original word'
                print 'show_change():   to show change word'
                print 'reverse():       to reverse the last change'
                print 'reset():         to reset the word to the original state'
                continue

            if (len(letra_index) > 1 and letra_index in comands) or (len(letra_a_cambiar) > 1 and letra_a_cambiar in comands):
                letra_index = letra_a_cambiar

                if letra_index == 'exit()':
                    return 

                if letra_index == 'show_original()':
                    print cadena_para_cambiar_original

                if letra_index == 'show_change()':
                    print cadena_para_cambiar

                if letra_index == 'reverse()':#Construir el metodo (pensarle mas) No funcina
                    cadena_para_cambiar = cadena_cambiada
                    print cadena_para_cambiar

                if letra_index == 'reset()':
                    cadena_para_cambiar = cadena_para_cambiar_original
                    print cadena_para_cambiar
                    continue
                    
            elif len(letra_a_cambiar) > 1 and letra_a_cambiar not in comands or len(letra_index) > 1 and letra_index not in comands:
                print '> That character doesn\'t exist for me.'
