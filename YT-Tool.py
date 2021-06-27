################################################################
#                                                              #
#                        [Creditos ]                           #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Craka Squad            #
#                                                              #
################################################################

# CodedByxNetting
# CrakaSquad

import pytube
import os
import sys

os.system('color 4')
print('''

    ▓██   ██▓▄▄▄█████▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
     ▒██  ██▒▓  ██▒ ▓▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
      ▒██ ██░▒ ▓██░ ▒░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
      ░ ▐██▓░░ ▓██▓ ░    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
      ░ ██▒▓░  ▒██▒ ░      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
       ██▒▒▒   ▒ ░░        ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
     ▓██ ░▒░     ░           ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
     ▒ ▒ ░░    ░           ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
     ░ ░                              ░ ░      ░ ░      ░  ░
     ░ ░                                                    
    
                   Dev: xNetting / Grupo: Craka Squad
                                                                                                                                                
    ''')

def yt():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Ingrese la URL del video que quiere descargar     │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
    ''')

    yt_url = input('''
    
    root@xnetting: ~# ''')

    yt = pytube.YouTube(yt_url)
    video = yt.streams.first()
    video.download()

def main():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga lo que quiera hacer                         │                      
    │                                                     │
    │        1 - Descargar un video de YT                 │                    
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    
    ''')

    opcion = input('''
    
    root@xnetting: ~# ''')

    if opcion == '1':
        yt()
    else:
        sys.exit()

main()
