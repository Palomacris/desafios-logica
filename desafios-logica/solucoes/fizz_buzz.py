def fizz_buzz(n: int) -> list[str]:
    if n <= 0:
        raise ValueError("n deve ser maior que 0.")

    saida: list[str] = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            saida.append("FizzBuzz")
        elif i % 3 == 0:
            saida.append("Fizz")
        elif i % 5 == 0:
            saida.append("Buzz")
        else:
            saida.append(str(i))
    return saida


def executar() -> None:
    print("\n--- Desafio 03: FizzBuzz ---")
    entrada = input("Digite um número inteiro n (ex: 15): ").strip()

    try:
        n = int(entrada)
        resultado = fizz_buzz(n)
        print("Resultado:")
        print(", ".join(resultado))
    except ValueError as e:
        print(f"Erro: {e}")
