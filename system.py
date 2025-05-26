import os

def abrir_app(opcao):
    aplicativos = {
        #'1': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        #'2': 'C:\\Program Files\\DigiteoUsuario\\AppData\\Roaming\\Spotify\\Spotify.exe',
        #'3': 'C:\\Program Files\\DigiteoUsuario\\AppData\\Local\\Postman\\Postman.exe',
        #'4': 'explorer',
        #'5': 'C:\\Program Files\\DigiteoUsuario\\Downloads'
    }
    
    caminho = aplicativos.get(opcao)
    if caminho:
        os.startfile(caminho)
    else:
        print("Opção inválida!")

def menu():
    while True:
        print("\nEscolha um aplicativo para abrir:")
        print("1 - Google Chrome")
        print("2 - Spotify")
        print("3 - Postman")
        print("4 - Windows Explorer")
        print("5 - Downloads")
        print("99 - Sair")
        
        escolha = input("Digite o número da opção: ")
        
        if escolha == '99':
            print("Saindo...")
            break
        
        abrir_app(escolha)
        
menu()
