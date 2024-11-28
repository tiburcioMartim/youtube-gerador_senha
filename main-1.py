import string, random

def gerar_senha(tamanho, minusculo, maiusculo, numeros, simbolos):
    caracteres = ''
    if minusculo:
        caracteres += string.ascii_lowercase    
    if maiusculo:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

tamanho = int(input('Qual será o tamanho da senha? '))
minusculo = input('Deseja incluir letras minusculas? (s/n)').lower() == 's'
maiusculo = input('Deseja incluir letras maiusculas? (s/n)').lower() == 's'
numeros = input('Deseja incluir numeros? (s/n)').lower() == 's'
simbolos = input('Deseja incluir simbolos? (s/n)').lower() == 's'
senha = gerar_senha(tamanho, minusculo, maiusculo, numeros, simbolos)

print(senha)