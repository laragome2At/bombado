import random
import string

def gerar_senha(comprimento, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_caracteres_especiais=True)
    caracteres= ''

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de Senhas Seguras")
    print("--------------------------")

    while True:
        comprimento = int(input("Digite o comprimento da senha desejada: "))

        incluir_maiusculas = input("Incluir letras maiúsculas na senha? (s/n):").lower() == 's'
        incluir_minusculas = input("Incluir letras minúsculas na senha? (s/n): ").lower() == 's'
        incluir_numeros = input("Incluir números na senha? (s/n): ").lower() == 's'
        incluir_caracteres_especiais = input("Incluir caracteres especiais na senha? (s/n) ").lower() == 's'

        senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiais)
        print("Senha gerada:", senha)

        continuar = input("Deseja gerar outra senha? (s/n): ").lower()
        if continuar != 's':
            break
        if __name__ == "__main__"
        main()