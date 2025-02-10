import time
capacidade_de_pessoas = 8
andar = 0
andar_atual = 0
andar_destino = 0

def analizar_cap():
    x = int(input("Informe a quantidade de pessoas que desejam entrar: "))
    if (1 <= x <= capacidade_de_pessoas):
        pass # A quantidade de pessoas está dentro do limite
    else:
        print(f"Ultrapassou a capacidade de pessoas máximas! (Máximo: {capacidade_de_pessoas})")
        analizar_cap() # Chama a função novamente para solicitar uma nova entrada

def tempo(andar_atual, andar_destino):
# Move o elevador de 1 em 1 segundo até o andar de destino.
    if andar_destino > andar_atual:
        movimento = 1 # Elevador sobe
    else:
        movimento = -1 # Elevador desce

    # Move o elevador de 1 em 1 segundo
    while (andar_atual != andar_destino):
        andar_atual += movimento # Atualiza o andar atual
        print(f"Andar {andar_atual}") # Mostra andar por andar que está passando
        time.sleep(1) # Delay de 1 segundo por andar
    return andar_atual # Retorna o novo andar atual

def analizar_andar(andar_destino):
    global andar_atual # Declaro que a variável utilizada é global para não considera-la local e dar erro no código
    if (andar_destino == andar_atual): # Se o andar de destino for igual ao atual, o elavador permanecerá no mesmo local
        print("Andar inválido, o elevador se manterá neste andar.") 
        andar_destino = input("Informe qual andar de destino (0 a 10) ou digite '000' para sair: ")
     
        if (andar_destino != "000"):
            andar_destino = int(andar_destino)
    
        analizar_andar(andar_destino) # E resetará o processo de escolher um andar de destino
    
    elif (0 <= andar_destino) and (andar_destino <= 10):
        print(f"Elevador se movendo para o andar {andar_destino}")
       
        andar_atual = tempo(andar_atual, andar_destino) # Chama a função tempo para mover o elevador
        
        print(f"Elevador chegou ao andar {andar_destino}!")
    else:
        print("Andar inválido.")
        pass

while True:
    if andar_atual == 0:
        print("Térreo")
    
    analizar_cap() # Chama a função que analiza a capacidade de pessoas
    
    andar_destino = input("Informe qual andar de destino (0 a 10) ou digite '000' para sair: ") # Solicita o andar de destino
    if andar_destino == '000': # Verifica se o usuário quer sair
        print("Você saiu do elevador!")
        break # Sai do loop e encerra o programa
    
    andar_destino = int(andar_destino) # Converte o andar_destino para inteiro e continua o programa 
    analizar_andar(andar_destino)