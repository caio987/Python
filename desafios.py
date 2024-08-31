#DESAFIO 01

# Crie um programa que leia o nome completo de uma pessoas e mostre:

# O nome com todas as letras maiúsculas

# O nome com todas as letras minúsculas

# Quantas letras ao todo (sem considerar espaços)

# Quantas letras tem o primeiro nome

nome = input('Escreva um nome: ')
separador = nome.split()
anuladorDeEspaços = nome.replace(' ', '')
contador = len(anuladorDeEspaços)
print(f' Texto e maiúsculo - {nome.upper()}')
print(f' Texto e minúsculo - {nome.lower()}')
print(f' Tem {contador} letras no nome {nome}')
print(f' O primeiro nome é: {separador[0]}')

# DESAFIO 02

# Crie um programa que leia o nome de uma cidade e siga se ela começa ou não com o nome “Santo”.
print('')
cidade = input('Escreva o nome de uma cidade: ')
fatiamento = cidade.split()
santo = 'Santo'
verificacao = santo in fatiamento[0]
print(f' Tem a palavra {santo} como primeiro nome em {cidade}? {verificacao}')

# DESAFIO 03

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
print('')
nome2 = input('Escreva um nome: ')
silva = "Silva"
verificacao2 = silva in nome2
print(f' Tem a palavra {silva} em {nome2}? {verificacao2}')


# DESAFIO 04

# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez
print('')
palavra = input('Escreva uma palavra: ')
palavraA = palavra.upper()
verificacao3 = palavraA.count('A') 
primeiroA = palavraA.find("A")
ultimoA = palavraA.rfind("A")

print(f'Na palavra tem {verificacao3} "A"')
print(f' O primeiro "A" começa em {primeiroA} ')
print(f' O último "A" começa em {ultimoA}')

# DESAFIO 05

# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome
# separadamente
print('')
nome3 = input('Escreva um nome: ')
separador2 = nome3.split()

print(f'O primeiro nome é {separador2[0]}')
print(f'O último nome é {separador2[-1]}')

