nome = input("Digite o nome do herói: ")
exp = int(input("Digite a experiência do herói: "))

bonus = exp + 100

def nivel(bonus):
    if bonus < 1000:
        return "Ferro"
    elif 1001 <= bonus <= 2000:
        return "Bronze"
    elif 2001 <= bonus <= 5000:
        return "Prata"
    elif 5001 <= bonus <= 7000:
        return "Ouro"
    elif 7001 <= bonus <= 8000:
        return "Platina"
    elif 8001 <= bonus <= 9000:
        return "Ascendente"
    elif 9001 <= bonus <= 10000:
        return "Imortal"
    else:
        return "Radiante"



print("O Herói de nome {} está no nivel de {}".format(nome, nivel(bonus)))

