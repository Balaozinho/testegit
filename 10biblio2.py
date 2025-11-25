import pandas as pd

# Criando uma mini base de dados
dados = {
    "Produto": ["Camisa", "Calça", "Boné", "Tênis"],
    "Preço": [79.90, 129.90, 39.90, 299.90],
    "Estoque": [10, 5, 20, 8]
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame
print("Tabela de produtos:")
print(df)

# Operações simples
print("\nPreço médio:", df["Preço"].mean())
print("Produto mais caro:", df.loc[df["Preço"].idxmax(), "Produto"])