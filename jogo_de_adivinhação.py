import random

max_tentativas = 5 #esta variável representa o número máximo de tentativas que o usuário terá para vencer o jogo
palavras_secretas = ['abacaxi', 'melão', 'banana', 'jaca', 'tomate'] #aqui está a lista de possíveis palavras secretas

while True: #esta operação significa que o programa se repetirá até que alguma condição faça com que ele pare de rodar
    palavra_secreta = random.choice(palavras_secretas) #aqui a função 'random.choice' escolhe aleatóriamente um item da lista de 'palavras_secretas' para ser a 'palavra_secreta'
    tentativa = input(f'Tente adivinhar a palavra secreta, você tem ({max_tentativas}) tentativas: ').lower() #aqui, o usuário terá a sua primeira chance de adivinhar a palavra, junto com um contador de tentativas
    palpite = '' #variável que irá armazenar as palavras que o usuário inserir
    tentativas_restantes = max_tentativas -1 #contador que exibe o número de tentativas restantes e diminui '1' cada vez que o loop é executado

    if tentativa == palavra_secreta:
        print('Parabéns, você acertou a palavra secreta! ')
    else:
        while palpite != palavra_secreta and tentativas_restantes > 0:
            input(f'Tente novamente, ({tentativas_restantes}) tentativas restantes. ').lower()
            tentativas_restantes -= 1
    #as 5 linhas de código acima representam as duas possíveis condições para que o programa consiga se repetir ou ser finalizado
        if palpite == palavra_secreta:
            print(f'Parabéns, você acertou a palavra secreta em ({int(tentativas_restantes - max_tentativas)})')
        else:
            print('Suas tentativas chegaram ao fim, reinicie o jogo...')
    jogar_novamente = input('Gostaria de tentar novamente? (s/n) ')
    if jogar_novamente != 's':
        break
    #as 7 linhas acima definem o que acontece se o usuário acertar ou errar a palavra no restante das tentativas, caso acabem as tentativas, o programa permite que o usuário reinicie o jogo ou pare o programa.
