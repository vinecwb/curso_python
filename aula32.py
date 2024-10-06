"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. 
Caso o usuário não digite um  número inteiro, informe que não é um número inteiro.
"""
# try:
#     numero = input('Digite um numero inteiro: ')


#     numero_inteiro = int(numero)

#     if type(numero_inteiro) == int:
            
#         if numero_inteiro % 2 == 0:
#             print('O número digitado é PAR!')
#         else: 
#             print('O número digitado é IMPAR')
# except:
#         print('Por favor, digite um numero inteiro')



"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horario descrito
Exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23,
"""
try:
    hora = input('Digite a hora atual: ')
    hora_saudacao = int(hora)

    if hora_saudacao >= 0 and hora_saudacao <= 11: 
          print('Bom dia!')
    elif hora_saudacao > 11 and hora_saudacao <=17:
         print("Boa tarde!")
    elif hora_saudacao > 17 and hora_saudacao <= 23:
         print("Boa noite!")
    else:
          print('Não conheço essa hora.')
except:
     print("Digite um valor entre 0 e 23")    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Maior que 6 escreve "Seu nome é muito grande".
"""
# nome = input('Digite o seu nome: ')

# if len(nome) <= 4:
#      print('Seu nome é curto')
# elif len(nome) > 4 and len(nome) <= 6:
#      print('Seu nome é normal')
# else:
#      print('Seu nome é muito grande')