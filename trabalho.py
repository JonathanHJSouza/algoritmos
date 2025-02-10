import os #import é uma meneira de importar outra biblioteca, a biblioteca os akuda em algumas funcionalidades inclusive interragir com o prompt, importei para limpar o prompt, tipo cls
import time #a bibliote time é ussada para usufluir de data e hora no sistema, mas tambem permite mexer no fluxo do codigo, criando pausas ou acelerando as pausas entre outras

# Aqui eu defino algumas variaveis que nao se mudaram durante o codgio todo:
CAPACIDADE_MAXIMA = 4 #Aqui eu defino que a capacidade de pessaos sera 4 pessoas, mas poderia fazer por kg
ANDAR_MIN = 1 #aqui eu defino o andar minimo do predio como 1, abaixo disso nao existe
ANDAR_MAX = 10 #aqui eu defino o valor maximo como 10, acima nao exite nada

andar_atual = ANDAR_MIN #aqui eu defino que no inicio de todo run eu começo no andar 1 padrão

def desenhar_predio(andar_elevador): #aqui eu quis fazer uma graça e desenhar o elevador andando entre os andares com os imports
    """Desenha o prédio no terminal com o elevador na posição correta.""" #isso aqui a gente define como docstring é outri tipo de comentario, geralmente uso para dar enfase no conteudo mas é mais usada para explicar funcoes ou calsses, mas nao mexe no funcionamento do codigo
    os.system('cls' if os.name == 'nt' else 'clear') # aqui eu uso a biblioteca os, para limpar o prompt como se fosse varios cls
    print("\n=== Prédio ===") #coloco o titulo do predio
    for andar in range(ANDAR_MAX, ANDAR_MIN - 1, -1): #percorrer os andares de cima oara baixo
        if andar == andar_elevador: # se o andar atual é o local onde vc esta
            print(f"| {andar:2d} |  🛗    |")  # Elevador na onde deve estar, local subindo ou descendo ou ficando no local, usando o cls parece que esta andando
        else:
            print(f"| {andar:2d} |       |")  # Mostra o andar sem elevador
    print("=" * 15)  # Base do prédio ============================

print("Seja bem-vindo! Os serviços são do térreo ao andar 10.") #olá
print("Quando desejar parar, digite 000.")#deixando explicito de como sair do while que vamos entrar e nao causar um "loop"

while True: # while true vai ser o loop principal do codigo, fazendo nao parar quando o elevador andar, enquanto for verdadeiro

    destino = input("\nDigite o andar que você deseja ir: ") #pede o andar que o usuario quer ir

    if destino == "000": #aqui eu defino que se o usuario difitar 000 eu saia do loop, com o brack voce encera o looping
        print("Você saiu do elevador! 🚶‍♂️")
        break

    if destino.isdigit(): #essa funçaõ identifica o tipo de variavel que vc digitou, nao coloquei as variaveis como int, porque aqui eu irei usar essa funçaõ para advertir se digitar algo que nao quero
        destino = int(destino) # aqui defino que a variavel destino eu quero que ela seja numero
    else:
        print(f"Entrada '{destino}' inválida! Digite um número de {ANDAR_MIN} a {ANDAR_MAX}.") #se for letra adverte
        continue #continue se da para entrar la no começo do loop

    if destino < ANDAR_MIN or destino > ANDAR_MAX: # verifica se o andar informado enta entre 1<destino<=10
        print(f"Entrada '{destino}' inválida! Digite um valor de {ANDAR_MIN} a {ANDAR_MAX}.") # se andar nao condizer adverte
        continue

    if destino == andar_atual: #aqui  eu adverto quando o destino é o mesmo que vc esta
        print("Você já está no seu destino! 😊")
        continue

    pessoas = input("Quantas pessoas vão embarcar? ") #agora é a hora que eu peço a quantidade de pessoas, lembrando que esse while é totalmente de cima para baixo em partes

    if pessoas.isdigit(): #verifico se a variavel é mesmo um numero
        pessoas = int(pessoas) #converto para inteiro
    else:
        print("Entrada inválida! Digite um número entre 1 e 4.") #adverto se nao for um numero
        continue

    if pessoas > CAPACIDADE_MAXIMA:
        print("🚨 Capacidade máxima atingida! O elevador suporta até 4 pessoas.") #adveeto se a capacidade é 1<pessoas<4
        continue

    print(f"\nElevador se movimentando do andar {andar_atual} para {destino}...") #esse print com f, serve para atribuir variaveis de forma mais facil dentro do print

    i = 1 if destino > andar_atual else -1 #define o movimento do elevador, descendo tira ou subindo
    for andar in range(andar_atual, destino + i, i):  # Inclui o andar final na animação
        desenhar_predio(andar)  # Atualiza a posição do elevador
        time.sleep(0.5)

    print(f"🚪 Elevador chegou ao andar {destino}.\n")
    andar_atual = destino  # Atualiza posição do elevador

print("Obrigado por usar o elevador! ") # se eu der 000 aparece esse final

# o codigo tem varios coisas que nao é necessaria, foram questao de beleza