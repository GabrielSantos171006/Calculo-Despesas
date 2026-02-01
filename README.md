# 💸 Contador de Despesas

Um sistema simples e eficiente via linha de comando (CLI) desenvolvido em Python para o controle de gastos pessoais diários e semanais.

O projeto permite registrar despesas em diversas categorias, visualizar relatórios financeiros e simular a passagem dos dias para controle semanal.

## 📋 Funcionalidades

* **Menu Interativo:** Navegação simples via terminal com limpeza de tela automática.
* **Categorização de Gastos:**
* **Relatórios Dinâmicos:**
  * Visualização do total gasto no dia.
  * Acumulado da semana.
  * Média de gastos semanais.
* **Simulação de Calendário:** O sistema possui uma função de "Encerrar o dia", que avança a data atual, reseta os gastos do dia mas mantém o acumulado da semana.

## 🚀 Como executar

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

1. Baixe os arquivos do projeto (`main.py` e `despesas.py`) para a mesma pasta.
2. Abra o terminal nessa pasta.
3. Execute o arquivo principal:

```bash
python main.py
```

## 🛠️ Estrutura do Projeto

- **`main.py`**: O ponto de entrada do programa. Gerencia o menu principal e o loop da sessão.
- **`despesas.py`**: Contém a lógica de negócio, incluindo:
  - Listas de armazenamento temporário.
  - Funções de cálculo (somas e médias).
  - Lógica de manipulação de datas (`datetime`).
  - Funções de interface (`limpar_tela`, `guardar_despesa`, `relatorio`).

## 📖 Como Usar

1. **Registrar Despesas (Opção 1):**
   - Escolha a categoria desejada.
   - Digite o valor e confirme.
   - Você pode adicionar múltiplos gastos consecutivamente.

2. **Relatório de Gastos (Opção 2):**
   - Visualize seus totais.
   - Ao final da visualização, o sistema perguntará se deseja **"Encerrar o dia"**.
   - Se escolher **SIM**, o dia avança (ex: dia 1 vira dia 2), limpando os gastos pontuais mas somando ao total da semana.

## ⚠️ Observações Importantes

O uso de letras resulta na quebra e encerramento do programa **Não utilize letras**

Este projeto utiliza armazenamento em memória (listas Python). Isso significa que **ao fechar o programa (Sair do programa / Opção 0), os dados inseridos serão perdidos**.

---

<p align="center">
  Feito com 🐍 Python
</p>
