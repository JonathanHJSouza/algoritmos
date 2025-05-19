from pulp import LpMaximize, LpProblem, LpVariable

#Atribuindo os valores informados às variáveis
couro_max = float(input("Informe a quantidade máxima de couro disponível (kg): "))
borracha_max = float(input("Informe a quantidade máxima de borracha disponível (kg): "))
lucro_sandalia = float(input("Informe o lucro por unidade de sandália: "))
lucro_sapato = float(input("Informe o lucro por unidade de sapato: "))
consumo_couro_sandalia = float(input("Informe o consumo de couro por sandália (kg): "))
consumo_couro_sapato = float(input("Informe o consumo de couro por sapato (kg): "))
consumo_borracha_sandalia = float(input("Informe o consumo de borracha por sandália (kg): "))
consumo_borracha_sapato = float(input("Informe o consumo de borracha por sapato (kg): "))

#Criando o modelo de otimização
model = LpProblem(name="maximizacao-lucro", sense=LpMaximize)

#Definição das variáveis de decisão

#Número de sandálias
x = LpVariable(name="sandalias", lowBound=0, cat="Continuous")
#Número de sapatos
y = LpVariable(name="sapatos", lowBound=0, cat="Continuous")

#Função objetivo: Maximizar o lucro
model += lucro_sandalia * x + lucro_sapato * y, "Lucro_Total"

#Restrições de recursos disponíveis

#Restrição do couro (kg)
model += consumo_couro_sandalia * x + consumo_couro_sapato * y <= couro_max, "Restricao_Couro"
#Restrição da borracha (kg)
model += consumo_borracha_sandalia * x + consumo_borracha_sapato * y <= borracha_max, "Restricao_Borracha"


model += x >= 100, "Restricao_Demanda_Minima_Sandalias"

model += y >= 50, "Restricao_Demanda_Minima_Sapatos"

model += x <= 800, "Restricao_Capacidade_Sandalias"

model += y <= 700, "Restricao_Capacidade_Sapatos"


horas_max = float(input("Informe a quantidade máxima de horas disponíveis: "))
tempo_sandalia = float(input("Informe o tempo de produção de uma sandália (horas): "))
tempo_sapato = float(input("Informe o tempo de produção de um sapato (horas): "))

model += tempo_sandalia * x + tempo_sapato * y <= horas_max, "Restricao_Horas_Producao"




#Resolver o modelo
model.solve()

#Exibir os resultados
print("Status da solução:", model.status)
print(f"Quantidade de sandálias produzidas: {x.varValue}")
print(f"Quantidade de sapatos produzidos: {y.varValue}")
print(f"Lucro máximo obtido: R$ {model.objective.value()}")