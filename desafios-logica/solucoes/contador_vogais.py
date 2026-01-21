def contar_vogais(texto: str) -> int:
    vogais = set("aeiouAEIOU")
    return sum(1 for ch in texto if ch in vogais)


def executar() -> None:
    print("\n--- Desafio 04: Contador de Vogais ---")
    texto = input("Digite um texto: ")
    qtd = contar_vogais(texto)
    print(f"Quantidade de vogais: {qtd}")
