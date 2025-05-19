from pulp import LpMaximize, LpProblem, LpVariable

#Atribuindo os valores informados às variáveis
MP1_max = 900.0
MP2_max = 600.0
lucro_P1 = 120.0
lucro_P2 = 90.0
lucro_P3 = 150.0
consumo_MP1_P1 = 7.0
consumo_MP1_P2 = 5.0
consumo_MP1_P3 = 6.0
consumo_MP2_P1 = 4.0
consumo_MP2_P2 = 3.0
consumo_MP2_P3 = 7.0

#Criando o modelo de otimização
model = LpProblem(name="maximizacao-lucro", sense=LpMaximize)

#Definição das variáveis de decisão

#Número de jaquetas
x = LpVariable(name="jaqueta", lowBound=0, cat="Continuous")
#Número de calca
y = LpVariable(name="calca", lowBound=0, cat="Continuous")
#Número de Moleton
z = LpVariable(name="moleton", lowBound=0, cat="Continuous")


#Função objetivo: Maximizar o lucro
model += lucro_P1 * x + lucro_P2 * y + lucro_P3 * z, "Lucro_Total"

#Restrições de recursos disponíveis

#Restrição do tecido (kg)
model += consumo_MP1_P1 * x + consumo_MP1_P2 * y + consumo_MP1_P3 * z <= MP1_max, "Restricao_tecido"
#Restrição da algodao (kg)
model += consumo_MP2_P1 * x + consumo_MP2_P2 * y + consumo_MP2_P3 * z <= MP2_max, "Restricao_algodao"


#Resolver o modelo
model.solve()

#Exibir os resultados
print("Status da solução:", model.status)
print(f"Quantidade de jaquetas produzidas: {x.varValue}")
print(f"Quantidade de calcas produzidas: {y.varValue}")
print(f"Quantidade de moletons produzidos: {z.varValue}")
print(f"Lucro máximo obtido: R$ {model.objective.value()}")