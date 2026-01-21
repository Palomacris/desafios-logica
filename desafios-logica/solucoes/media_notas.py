def media(notas: list[float]) -> float:
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)


def executar() -> None:
    print("\n--- Desafio 02: Média de Notas ---")
    print("Digite notas separadas por vírgula. Ex: 7.5, 8, 10")
    entrada = input("Notas: ").strip()

    try:
        notas = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
        resultado = media(notas)
        print(f"Média: {resultado:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")
