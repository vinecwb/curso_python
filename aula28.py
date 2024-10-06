'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar a sua idade
Se nome e idade forem digitados: 
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios."
'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

nome_invertido = nome[-1:-10:-1]
n = len(nome)
letra = nome


if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
    print(f'Seu nome contém {n} letras')
    print(f'A primeira letra do seu nome é {letra[0]}')
    print(f'A primeira letra do seu nome é {letra[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')