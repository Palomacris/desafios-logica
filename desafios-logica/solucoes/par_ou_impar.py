def par_ou_impar(numero: int) -> str:
    return "Par" if numero % 2 == 0 else "Ímpar"


def executar() -> None:
    print("\n--- Desafio 01: Par ou Ímpar ---")
    while True:
        entrada = input("Digite um número inteiro (ou 'sair'): ").strip().lower()
        if entrada == "sair":
            break

        try:
            n = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        print(f"Resultado: {par_ou_impar(n)}")
