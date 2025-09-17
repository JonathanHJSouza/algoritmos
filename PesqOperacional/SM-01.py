#Este código foi gerado com apoio de ferramentas de inteligência artificial generativa.
#Necessário instalar "pandas": pip install pandas

import pandas as pd

def simular_fluxo(chegadas, atendentes, capacidade_atendente=3):
    """
    Simula o fluxo de uma fila por intervalos.
    - chegadas: lista de chegadas por intervalo
    - atendentes: lista com número de atendentes por intervalo
    - capacidade_atendente: atendimentos por atendente em cada intervalo (default=3)
    Retorna: DataFrame com a simulação e dicionário de indicadores.
    """
    if len(chegadas) != len(atendentes):
        raise ValueError("As listas 'chegadas' e 'atendentes' devem ter o mesmo tamanho.")
    
    capacidade = [a * capacidade_atendente for a in atendentes]
    fila_final = 0
    dados = []
    
    for i in range(len(chegadas)):
        fila_inicial = fila_final
        em_sistema = fila_inicial + chegadas[i]
        atendidos = min(em_sistema, capacidade[i])
        fila_final = em_sistema - atendidos
        dados.append({
            'Intervalo': i+1,
            'Chegadas': chegadas[i],
            'Capacidade': capacidade[i],
            'Fila Inicial': fila_inicial,
            'Atendidos': atendidos,
            'Fila Final': fila_final
        })
    
    df = pd.DataFrame(dados)

    # Indicadores
    chegadas_totais = sum(chegadas)
    atendidos_periodo = int(df['Atendidos'].sum())
    fila_ao_final = int(df['Fila Final'].iloc[-1])
    fila_maxima = int(df['Fila Final'].max())

    # Atendidos imediatamente (FIFO: quantos dos atendidos eram da leva do próprio intervalo)
    atendidos_imediatos = int(df.apply(lambda r: max(0, r['Atendidos'] - r['Fila Inicial']), axis=1).sum())
    atendidos_imediatos_pct = atendidos_imediatos / chegadas_totais * 100 if chegadas_totais else 0.0

    indicadores = {
        'Chegadas totais': chegadas_totais,
        'Atendidos no período': atendidos_periodo,
        'Fila ao final': fila_ao_final,
        'Fila máxima': fila_maxima,
        'Atendidos imediatamente (n)': atendidos_imediatos,
        'Atendidos imediatamente (%)': atendidos_imediatos_pct
    }

    return df, indicadores


# =====================
# Definição dos cenários
# =====================

# Dados observados
chegadas_base = [3,5,6,4,5,4,3,2]

# Cenário Base: 1 atendente em todos os intervalos
atendentes_base = [1,1,1,1,1,1,1,1]

# Hipótese 1: aumento de atendentes nos intervalos 3 e 4
atendentes_H1 = [1,1,2,2,1,1,1,1]

# Hipótese 2: redução de atendentes nos intervalos 3 e 4
atendentes_H2 = [1,1,0,0,1,1,1,1]

# =====================
# Simulações
# =====================
df_base, ind_base = simular_fluxo(chegadas_base, atendentes_base, capacidade_atendente=3)
df_H1, ind_H1   = simular_fluxo(chegadas_base, atendentes_H1, capacidade_atendente=3)
df_H2, ind_H2   = simular_fluxo(chegadas_base, atendentes_H2, capacidade_atendente=3)

# =====================
# Resultados
# =====================
def mostrar_indicadores(nome, indicadores):
    print(f"\nIndicadores - {nome}:")
    print(f"Alunos (chegadas) totais: {indicadores['Chegadas totais']} alunos")
    print(f"Atendidos no período: {indicadores['Atendidos no período']} alunos")
    print(f"Fila ao final: {indicadores['Fila ao final']}")
    print(f"Fila máxima: {indicadores['Fila máxima']}")
    print(f"Atendidos imediatamente (no mesmo intervalo que chegaram): "
          f"{indicadores['Atendidos imediatamente (n)']} de {indicadores['Chegadas totais']} "
          f"= {indicadores['Atendidos imediatamente (%)']:.1f}%")

mostrar_indicadores("Cenário Base", ind_base)
mostrar_indicadores("Hipótese 1", ind_H1)
mostrar_indicadores("Hipótese 2", ind_H2)
