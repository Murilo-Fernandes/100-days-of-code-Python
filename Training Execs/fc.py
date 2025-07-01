import os

fluxo_caixa = []

print("_________________")
print("Fluxo de Caixa")
print("_________________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("Digite outro número para sair")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append( {
        "nome": nome,
        "valor": valor
    })

while True:
    opcao = input("Opção: ")
    
    if opcao == "1":
        adicionar_transacao()
    elif opcao == "2":
        adicionar_transacao()
    else:
        print("Saindo...")
        break

total = 0
for transacao in fluxo_caixa:
    print(f"Nome: {transacao['nome']}, Valor: {transacao['valor']}")
    total += transacao['valor']

print(f"Total: ${total:.2f}")