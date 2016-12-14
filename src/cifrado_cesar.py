#!/usr/bin/python

class cifrado_cesar(object):

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


    

    def reversar(self, mirror):

        normal = []

        i = len(mirror)

        while i:
            i-= 1

            normal.append(mirror[i])

        return ''.join(normal)




        
