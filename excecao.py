from main import *

def main():
    try:
        while True:
            print("\n1. Login")
            print("2. Cadastro")
            print("3. Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == '1':
                login()
            elif opcao == '2':
                cadastrar_estudante()
            elif opcao == '3':
                print("Encerrando o sistema...")
                break
    except ValueError:
        print("Opção inválida. Tente novamente.")
