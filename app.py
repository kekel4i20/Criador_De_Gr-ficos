import matplotlib.pyplot as plt

lista_x = []
lista_y = []
cores = []
destaque = []


def barras():
    global lista_x, lista_y
    quantidade_colunas_linhas = int(input('\nQuantas colunas irá ter?\n> '))

    pergunta = input('\nTem número quebrado? (S/N)\n> ').lower().strip()
    if pergunta == 's':
        for i in range(quantidade_colunas_linhas):
            pergunta_x = float(input('\nQual os números a se colocarem no gráfico no eixo x\n> '))
            lista_x.append(pergunta_x)
        print('Ok agora para as linhas')

        for i in range(quantidade_colunas_linhas):
            pergunta_y = float(input('\nQual os números a se colocarem no gráfico no eixo y\n> '))
            lista_y.append(pergunta_y)
        print('\nOk agora próxima etapa')

    elif pergunta == 'n':
        for i in range(quantidade_colunas_linhas):
            pergunta_x = int(input('\nQual os números a se colocarem no gráfico no eixo x\n> '))
            lista_x.append(pergunta_x)
        print('Ok agora próxima etapa')

        for i in range(quantidade_colunas_linhas):
            pergunta_y = int(input('\nQual os números a se colocarem no gráfico no eixo y\n> '))
            lista_y.append(pergunta_y)
        print('Ok agora próxima etapa')


    cor= input('\nQual cor: Green(verde) Red(vermelho) Purple(roxo) Black(preto) Yellow(amarelo)\n> ')

    titulo = input('\nQual será o titulo do gráfico?\n> ')
    tamanho_titulo = int(input('\nQual o tamanho do titulo?\n> '))

    descricao_y = input('\nQual será a descrição a esquerda?\n> ')
    tamanho_y = int(input('\nQual será o tamanho da descrição?\n> '))

    descricao_x = input('\nQual será a descrição a baixo?\n> ')
    tamanho_x = int(input('\nQual será o tamanho da descrição?\n> '))
    
    font1 =  {'family' : 'arial'}
    barras = plt.bar(lista_x,lista_y, color=cor)
    plt.title(titulo, fontsize=tamanho_titulo, fontdict=font1)
    plt.ylabel(descricao_y, fontsize=tamanho_y)
    plt.xlabel(descricao_x, fontsize=tamanho_x)
    plt.bar_label(barras, labels=lista_x, fontsize=10,fontweight='bold', padding=-15)
    plt.show()


def pizza():
    global lista_x, lista_y
    quantidade_fatias = int(input('\nQuantas fatias irá ter?\n> '))

    pergunta = input('\nTem número quebrado? (S/N)\n> ').lower().strip()
    if pergunta == 's':
        for i in range(quantidade_fatias):
            pergunta_fatias = float(input(f'\nQual o número a se colocar nesta fatia\n> '))
            lista_x.append(pergunta_fatias)
        print('\nOk agora para os rótulos!')

        for i in range(quantidade_fatias):
            pergunta_rotulos = input(f'\nQual o rótulo a se colocarem nesta fatia {lista_x[i]}\n> ')
            lista_y.append(pergunta_rotulos)
        print('\nOk agora próxima etapa')

    elif pergunta == 'n':
        for i in range(quantidade_fatias):
            pergunta_fatias = int(input(f'\nQual o número a se colocar nesta fatia\n> '))
            lista_x.append(pergunta_fatias)
        print('\nOk agora para os rótulos!')

        for i in range(quantidade_fatias):
            pergunta_rotulos = input(f'\nQual o rótulo a se colocarem nesta fatia {lista_x[i]}\n> ')
            lista_y.append(pergunta_rotulos)
        print('\nOk agora próxima etapa')

    for i in range(quantidade_fatias):
        cor = input('\nQuais cores: Green(verde) Red(vermelho) Purple(roxo) Black(preto) Yellow(amarelo) Blue(azul)\n> ').lower().strip()
        cores.append(cor)

    titulo = input('\nQual será o titulo do gráfico?\n> ')
    tamanho_titulo = int(input('\nQual o tamanho do titulo?\n> '))
    for i in range(quantidade_fatias):
        quantidade_destaque = float(input(f'\nQual o tamanho do destaque que você irá dar para esta fatia {lista_x[i]}\n> '))
        destaque.append(quantidade_destaque)

    font1 =  {'family' : 'arial'}
    plt.pie(lista_x, labels=lista_y, colors=cores,explode=destaque ,shadow=True, autopct='%1.1f%%') 
    plt.title(titulo, fontsize=tamanho_titulo, fontdict=font1)
    plt.legend()
    plt.show()

barras_pizza = input('Qual gráfico deseja? (barras / pizza)\n> ').lower()
if barras_pizza == 'barras':
    barras()
elif barras_pizza == 'pizza':
    pizza()
else:
    print('Não foi encontrado')