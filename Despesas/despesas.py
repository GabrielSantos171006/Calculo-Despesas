import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

from datetime import datetime, timedelta

hoje = datetime.now()
dias_semana = 1
total_semana = 0
contagem_semanas = 1

#Listas de despesas
alimentacao = []
aluguel = []
vestuario = []
entretenimento = []
outros = []

def guardar_despesa(opc_menu):
    global total_semana
    while opc_menu == 1:
        print('Em que categoria a despesa atual se encaixa:')
        print('1) Alimentação: 🍎🍕')
        print('2) Aluguel: 🏠🏢')
        print('3) Vestuário: 👕👖')
        print('4) Entretenimento: 🍿🎮')
        print('5) Outros:⚙️🔗')
        print('=============================================')
        print('Digite ''0'' caso queira voltar ↩️\n')
        resp_menu = int(input())

        if resp_menu == 0:
            limpar_tela()
            break

        elif resp_menu == 1:
            limpar_tela()
            voltar_despesas = 1
            while voltar_despesas == 1:
                print("=============ADICIONAR DESPESA DE ALIMENTAÇÃO=============")
                vlr_despesa_alimentos = int(input(f"Digite o valor em R$: "))
                alimentacao.append(vlr_despesa_alimentos)
                total_semana += vlr_despesa_alimentos
                limpar_tela()
                voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                while voltar_despesas != 1 and voltar_despesas != 2:
                    limpar_tela()
                    print("Opção inválida! Por favor digite 1 ou 2.")
                    voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                if voltar_despesas == 2:
                    limpar_tela()
                    break
                
        elif resp_menu == 2:
            limpar_tela()
            voltar_despesas = 1
            while voltar_despesas == 1:
                print("=============ADICIONAR DESPESA DE ALUGUEL=============")
                vlr_despesa_aluguel = int(input(f"Digite o valor em R$: "))
                aluguel.append(vlr_despesa_aluguel)
                total_semana += vlr_despesa_aluguel
                limpar_tela()
                voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                while voltar_despesas != 1 and voltar_despesas != 2:
                    limpar_tela()
                    print("Opção inválida! Por favor digite 1 ou 2.")
                    voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                if voltar_despesas == 2:
                    limpar_tela()
                    break

        elif resp_menu == 3:
            limpar_tela()
            voltar_despesas = 1
            while voltar_despesas == 1:
                print("=============ADICIONAR DESPESA DE VESTUÁRIO=============")
                vlr_despesa_vestuario = int(input(f"Digite o valor em R$: "))
                vestuario.append(vlr_despesa_vestuario)
                total_semana += vlr_despesa_vestuario
                limpar_tela()
                voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                while voltar_despesas != 1 and voltar_despesas != 2:
                    limpar_tela()
                    print("Opção inválida! Por favor digite 1 ou 2.")
                    voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                if voltar_despesas == 2:
                    limpar_tela()
                    break

        elif resp_menu == 4:
            limpar_tela()
            voltar_despesas = 1
            while voltar_despesas == 1:
                print("=============ADICIONAR DESPESA DE ENTRETENIMENTO=============")
                vlr_despesa_entretenimento = int(input(f"Digite o valor em R$: "))
                entretenimento.append(vlr_despesa_entretenimento)
                total_semana += vlr_despesa_entretenimento
                limpar_tela()
                voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                while voltar_despesas != 1 and voltar_despesas != 2:
                    limpar_tela()
                    print("Opção inválida! Por favor digite 1 ou 2.")
                    voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                if voltar_despesas == 2:
                    limpar_tela()
                    break

        elif resp_menu == 5:
            limpar_tela()
            voltar_despesas = 1
            while voltar_despesas == 1:
                print("=============ADICIONAR DESPESA DE OUTRA CATEGORIA=============")
                vlr_despesa_outros = int(input(f"Digite o valor em R$: "))
                outros.append(vlr_despesa_outros)
                total_semana += vlr_despesa_outros
                limpar_tela()
                voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                while voltar_despesas != 1 and voltar_despesas != 2:
                    limpar_tela()
                    print("Opção inválida! Por favor digite 1 ou 2.")
                    voltar_despesas = int(input("Adicionar mais despesas?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
                if voltar_despesas == 2:
                    limpar_tela()
                    break
        else:
            limpar_tela()
            print("❌ Resposta não valida! Digite um valor aceitavel")
            #Quando já esta em looping o menu se repete, basta colocar a resposta de erro

def relatorio(opc_menu):
    global contagem_semanas
    global total_semana
    global dias_semana
    global hoje #<-- Permite alterar a data externa
    while opc_menu == 2:
        voltar_relatorio = 2
        while voltar_relatorio == 2 :
            print(f"Data: ",(hoje.day),"/",(hoje.month),"/",(hoje.year), "📆")
            print(f"{contagem_semanas}° Semana\nDia: {dias_semana}\n")
            total_dia = sum(alimentacao + aluguel + vestuario + entretenimento + outros)
            print("="*15)
            print(f"📍 Gastos de hoje:  {total_dia}")
            print(f"💰 Gastos da semana: {total_semana}")
            print(f"📊 Média de gastos da semana: {total_semana/dias_semana:.2f}") 
            print("="*15)
            voltar_relatorio = int(input("\nEncerrar o dia?\n| 1-SIM ✅ | 2-NÃO ❌ |\n\n"))
            while voltar_relatorio != 1 and voltar_relatorio!= 2:
                limpar_tela()
                print("Opção inválida! Por favor digite 1 ou 2.")
                voltar_relatorio = int(input("Encerrar o dia?\n| 1-SIM ✅ | 2-NÃO ❌ |\n"))
            if voltar_relatorio == 1:
                limpar_tela()
                hoje += timedelta(days=1)
                dias_semana += 1
                if dias_semana > 7:
                    dias_semana = 1 
                    total_semana = 0
                    contagem_semanas += 1
                alimentacao.clear()
                aluguel.clear()
                vestuario.clear()
                entretenimento.clear()
                outros.clear()
                opc_menu = 0  
                break
            elif voltar_relatorio == 2:
                limpar_tela()
                opc_menu = 0
                break