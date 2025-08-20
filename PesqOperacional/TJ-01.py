#Este código foi gerado com apoio de ferramentas de inteligência artificial generativa.
#Necessário instalar "pandas": pip install pandas

import itertools
import pandas as pd

# Jogadores e estratégias
players = ["Aluno 1", "Aluno 2", "Aluno 3"]
strategies = ["C", "NC"]

# Payoffs: (Aluno1, Aluno2, Aluno3)
payoffs = {
    ("C","C","C"): (10,10,10),
    ("C","C","NC"): (5,5,15),
    ("C","NC","C"): (5,15,5),
    ("C","NC","NC"): (2,8,8),
    ("NC","C","C"): (15,5,5),
    ("NC","C","NC"): (8,2,8),
    ("NC","NC","C"): (8,8,2),
    ("NC","NC","NC"): (0,0,0),
}

# Função para checar estratégia dominante
def check_dominant(player_index):
    dominant = None
    for s in strategies:
        is_dominant = True
        for profile in itertools.product(strategies, repeat=2):
            full_s1 = list(profile)
            full_s1.insert(player_index, s)
            payoff_s1 = payoffs[tuple(full_s1)][player_index]

            other_s = [x for x in strategies if x != s][0]
            full_s2 = list(profile)
            full_s2.insert(player_index, other_s)
            payoff_s2 = payoffs[tuple(full_s2)][player_index]

            if payoff_s1 < payoff_s2:
                is_dominant = False
                break
        if is_dominant:
            dominant = s
            break
    return dominant

# Função para checar equilíbrio de Nash
def is_nash(profile):
    for i, player_choice in enumerate(profile):
        # Testa se mudar a estratégia aumenta o payoff
        other_indices = [0,1,2]
        other_indices.remove(i)
        for s in strategies:
            if s == player_choice:
                continue
            test_profile = list(profile)
            test_profile[i] = s
            if payoffs[tuple(test_profile)][i] > payoffs[tuple(profile)][i]:
                return False
    return True

# Encontrar todos os equilíbrios de Nash
nash_equilibria = [profile for profile in itertools.product(strategies, repeat=3) if is_nash(profile)]

# Checar estratégias dominantes
dominant_strategies = [check_dominant(i) for i in range(3)]

# Criar tabela visual
rows = []
for profile in itertools.product(strategies, repeat=3):
    row = {
        "Aluno 1": profile[0],
        "Aluno 2": profile[1],
        "Aluno 3": profile[2],
        "Payoff Aluno 1": payoffs[profile][0],
        "Payoff Aluno 2": payoffs[profile][1],
        "Payoff Aluno 3": payoffs[profile][2],
        "Total": sum(payoffs[profile]),
        "Nash": profile in nash_equilibria
    }
    rows.append(row)

df = pd.DataFrame(rows)

# Marcar solução cooperativa
max_total = df["Total"].max()
df["Cooperativa"] = df["Total"] == max_total

# Mostrar resultados
for i, s in enumerate(dominant_strategies):
    if s:
        print(f"Estratégia dominante de {players[i]}: {s}")
    else:
        print(f"{players[i]} não possui estratégia dominante.")

print("\nEquilíbrios de Nash encontrados:")
for eq in nash_equilibria:
    print(eq)

print("\nTabela completa com solução cooperativa e Nash marcada:\n")
print(df)
