import random

def gerar_numeros_sorte(total_numeros, numero_minimo, numero_maximo):
    if total_numeros > (numero_maximo - numero_minimo + 1):
        print("Erro: O número total de números deve ser menor ou igual à faixa de números permitida.")
        return None
    numeros_sorte = random.sample(range(numero_minimo, numero_maximo + 1), total_numeros)
    return sorted(numeros_sorte)

def main():
    print("Bem-vindo ao Gerador de Números da Sorte!")
    while True:
        total_numeros = int(input("Quantos números da sorte você deseja gerar? "))
        numero_minimo = int(input("Qual é o número mínimo da faixa? "))
        numero_maximo = int(input("Qual é o número máximo da faixa? "))
        numeros_sorte = gerar_numeros_sorte(total_numeros, numero_minimo, numero_maximo)
        if numeros_sorte:
            print("Números da sorte gerados:", numeros_sorte)
            jogar_novamente = input("Deseja gerar mais números da sorte? (s/n) ").lower()
            if jogar_novamente != 's':
                break

if __name__ == "__main__":
    main()