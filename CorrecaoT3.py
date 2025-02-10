# Definição dos parâmetros do elevador
CAPACIDADE_MAXIMA = 5 # Número máximo de pessoas permitidas
ANDAR_MINIMO = 0 # Térreo
ANDAR_MAXIMO = 10 # Último andar
# Estado inicial do elevador
andar_atual = 0
print("Bem-vindo ao Simulador de Elevador!")
print(f"O elevador está no andar {andar_atual}.")
while True:
    # Solicita o andar de destino ao usuário
    destino = input("\nDigite o andar de destino (0 a 10) ou '000' para sair: ")
    # Verifica se o usuário deseja sair
    if destino == '000':
        print("Encerrando o programa...")
        break # Sai do loop
    
    # Converte a entrada para número e valida se é um andar válido
    if not destino.isdigit() or not (ANDAR_MINIMO <= int(destino) <= ANDAR_MAXIMO):
        print("Entrada inválida! Escolha um andar entre 0 e 10.")
        continue # Volta ao início do loop

    destino = int(destino) # Converte o destino para número inteiro
    # Verifica se o usuário está tentando ir para o mesmo andar
    if destino == andar_atual:
        print(f"Você já está no andar {andar_atual}. Nenhuma movimentação necessária.")
        continue

    # Solicita o número de passageiros
    pessoas = input("Quantas pessoas vão entrar no elevador? ")
     # Verifica se a entrada é numérica e dentro do limite permitido
    if not pessoas.isdigit() or int(pessoas) > CAPACIDADE_MAXIMA or int(pessoas) <= 0:
        print(f"Capacidade excedida! O número de pessoas deve ser entre 1 e {CAPACIDADE_MAXIMA}.")
        continue
    pessoas = int(pessoas) # Converte o número de pessoas para inteiro
    # Simulação do movimento andar por andar
    print(f"Elevador saindo do andar {andar_atual}...")
    if destino > andar_atual:
        for i in range(andar_atual + 1, destino + 1):
            print(f"Subindo... Andar {i}")
    else:
        for i in range(andar_atual - 1, destino - 1, -1):
            print(f"Descendo... Andar {i}")
    # Atualiza o andar atual
    andar_atual = destino
    print(f"Elevador chegou ao andar {andar_atual}. Portas abertas.")
