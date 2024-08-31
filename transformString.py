# Trocando uma palavra dentro de um texto
texto = 'Pedro Miho'
troca_palavra = texto.replace('Miho', 'Souza')

print(troca_palavra)
print('')  
  
#Deixando todos os caracteres em maiúsculo 
outroTexto = 'JOsECArloS@OUtlOoK.COm'
texto_maiusculo = outroTexto.upper()
print(outroTexto)
print('')  

#Deixando todos os caracteres em minusculo 
texto_minusculo = outroTexto.lower()
print(outroTexto)
print('')  

#Deixando a primeira letra de cada palavra maiúscula
outroOutroTexto = "meu primeiro curso no senai"
primeiraLetraMaiuscula = outroOutroTexto.title()
print(primeiraLetraMaiuscula)
print('')  

#Deixando a primeira letra da primeira palavra maiúscula
primeiraLetraDaFraseMaiuscula = outroOutroTexto.capitalize()
print(primeiraLetraDaFraseMaiuscula)
print('')  

#Texto sem eliminar espaços inúteis
textoBisavo = "        SENAI       "
print(f' A palavra {textoBisavo} tem {len(textoBisavo)} caracteres') 
print('')  

#Texto eliminando espaços inúteis
textoSemEspaco = textoBisavo.strip()
print(f' A palavra {textoSemEspaco} tem {len(textoSemEspaco)} caracteres')
print('')  


