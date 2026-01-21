from solucoes.par_ou_impar import executar as executar_par_ou_impar
from solucoes.media_notas import executar as executar_media_notas
from solucoes.fizz_buzz import executar as executar_fizz_buzz
from solucoes.contador_vogais import executar as executar_contador_vogais
from solucoes.maior_menor import executar as executar_maior_menor


def mostrar_menu() -> None:
    print("\n=== Desafios de Lógica e Pensamento Computacional ===")
    print("1) Par ou Ímpar")
    print("2) Média de Notas")
    print("3) FizzBuzz")
    print("4) Contador de Vogais")
    print("5) Maior e Menor de uma Lista")
    print("0) Sair")


def main() -> None:
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            executar_par_ou_impar()
        elif escolha == "2":
            executar_media_notas()
        elif escolha == "3":
            executar_fizz_buzz()
        elif escolha == "4":
            executar_contador_vogais()
        elif escolha == "5":
            executar_maior_menor()
        elif escolha == "0":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
