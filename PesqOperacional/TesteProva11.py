from pulp import LpMaximize, LpProblem, LpVariable

#Atribuindo os valores informados às variáveis
MP1_max = 600.00
MP2_max = 400.00
lucro_P1 = 80.00
lucro_P2 = 60.00
consumo_MP1_P1 = 5.0
consumo_MP1_P2 = 3.0
consumo_MP2_P1 = 3.0
consumo_MP2_P2 = 2.0

#Criando o modelo de otimização
model = LpProblem(name="maximizacao-lucro", sense=LpMaximize)

#Definição das variáveis de decisão

#Número de polimero
x = LpVariable(name="polimero", lowBound=0, cat="Continuous")
#Número de fibra
y = LpVariable(name="fibra", lowBound=0, cat="Continuous")

#Função objetivo: Maximizar o lucro
model += lucro_P1 * x + lucro_P2 * y, "Lucro_Total"

#Restrições de recursos disponíveis

#Restrição do polimero (kg)
model += consumo_MP1_P1 * x + consumo_MP1_P2 * y <= MP1_max, "Restricao_Polimero"
#Restrição da fibra (kg)
model += consumo_MP2_P1 * x + consumo_MP2_P2 * y <= MP2_max, "Restricao_Fibra"


#Resolver o modelo
model.solve()

#Exibir os resultados
print("Status da solução:", model.status)
print(f"Quantidade de Paineis produzidos: {x.varValue}")
print(f"Quantidade de Carcaças produzidas: {y.varValue}")
print(f"Lucro máximo obtido: R$ {model.objective.value()}")