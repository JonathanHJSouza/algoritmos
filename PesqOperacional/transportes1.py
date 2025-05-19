import pulp

# Fábricas (oferta) e sua capacidade
fabricas = {
    'Amsterda': 70,
    'Cairo': 105,
    'NovaYork': 130,
    'CidadeMexico': 65
}

# Lojas (demanda) e suas necessidades
lojas = {
    'California': 50,
    'Teera': 80,
    'Rio': 150,
    'Madri': 90
}

# Custos de transporte (origem, destino): custo
custos = {
    ('Amsterda', 'California'): 8,
    ('Amsterda', 'Teera'): 8,
    ('Amsterda', 'Rio'): 5,
    ('Amsterda', 'Madri'): 2,
    ('Cairo', 'California'): 10,
    ('Cairo', 'Teera'): 5,
    ('Cairo', 'Rio'): 10,
    ('Cairo', 'Madri'): 10,
    ('NovaYork', 'California'): 7,
    ('NovaYork', 'Teera'): 10,
    ('NovaYork', 'Rio'): 6,
    ('NovaYork', 'Madri'): 8,
    ('CidadeMexico', 'California'): 4,
    ('CidadeMexico', 'Teera'): 10,
    ('CidadeMexico', 'Rio'): 10,
    ('CidadeMexico', 'Madri'): 5
}

# Define o problema de minimização
problema = pulp.LpProblem("Problema_de_Transporte", pulp.LpMinimize)

# Variáveis de decisão
x = pulp.LpVariable.dicts("Transporte", custos, lowBound=0, cat='Continuous')

# Função objetivo: minimizar o custo total
problema += pulp.lpSum(x[orig_dest] * custo for orig_dest, custo in custos.items())

# Restrição de oferta (cada fábrica envia no máximo sua capacidade)
for origem in fabricas:
    problema += pulp.lpSum(x[(origem, destino)] for destino in lojas) <= fabricas[origem], f"Oferta_{origem}"

# Restrição de demanda (cada loja recebe exatamente o que precisa)
for destino in lojas:
    problema += pulp.lpSum(x[(origem, destino)] for origem in fabricas) == lojas[destino], f"Demanda_{destino}"

# Resolver
problema.solve()

# Resultado
print("Status:", pulp.LpStatus[problema.status])
print("\nQuantidades transportadas:")
for var in x.values():
    if var.varValue > 0:
        print(f"{var.name} = {var.varValue}")

print(f"\nCusto total mínimo: {pulp.value(problema.objective)}")
