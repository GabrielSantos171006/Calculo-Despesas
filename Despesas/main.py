from despesas import guardar_despesa, limpar_tela,relatorio
gerar_sessao = 1

while gerar_sessao == 1:
    print('========== 💸 Contador de Despezas 💸 ==========\n')
    print('1) Registar despesas 💾​📉')
    print('2) Relatório de gastos 📝​💸​')
    print('0) - Sair do programa 👋🔚')
    opc_menu = int(input('Digite o número do que deseja fazer: '))
    if opc_menu == 0:
        limpar_tela()
        print('O programa foi encerrado!')
        break
    elif opc_menu == 1:
        limpar_tela()
        guardar_despesa(opc_menu)
    elif opc_menu == 2:
        limpar_tela()
        relatorio(opc_menu)
    else:
        limpar_tela()
        print('❌ERRO❌\nDigite um número válido!')