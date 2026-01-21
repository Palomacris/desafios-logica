def maior_menor(numeros: list[float]) -> tuple[float, float]:
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return max(numeros), min(numeros)


def executar() -> None:
    print("\n--- Desafio 05: Maior e Menor ---")
    print("Digite números separados por vírgula. Ex: 10, 2, 33, -5")
    entrada = input("Números: ").strip()

    try:
        numeros = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        maior, menor = maior_menor(numeros)
        print(f"Maior: {maior}")
        print(f"Menor: {menor}")
    except ValueError as e:
        print(f"Erro: {e}")
