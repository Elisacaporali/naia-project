import random
from datetime import datetime, timedelta

class AssistenteIA:
    def __init__(self):
        self.nome_usuario = ""
        self.tarefas = {
            "saude": [
                {"descricao": "Tomar medicação", "prioridade": 5},
                {"descricao": "Tomar água de hora em hora", "prioridade": 4},
                {"descricao": "Tomar banho", "prioridade": 3},
                {"descricao": "Escovar os dentes", "prioridade": 4},
                {"descricao": "Fazer exercício físico", "prioridade": 4},
                {"descricao": "Lavar os cabelos", "prioridade": 2}
            ],
            "casa": [
                {"descricao": "Varrer a casa", "prioridade": 3},
                {"descricao": "Cuidar das plantas", "prioridade": 2},
                {"descricao": "Tratar dos animais", "prioridade": 5},
                {"descricao": "Verificar correspondências", "prioridade": 3},
                {"descricao": "Verificar contas para pagar", "prioridade": 4},
                {"descricao": "Fazer compra de supermercado", "prioridade": 4}
            ],
            "escola": [
                {"descricao": "Fazer trabalho ou para casa", "prioridade": 5},
                {"descricao": "Ler", "prioridade": 4},
                {"descricao": "Organizar as matérias do dia seguinte", "prioridade": 4},
                {"descricao": "Separar material para não esquecer", "prioridade": 5}
            ],
            "trabalho": [
                {"descricao": "Agendar reunião", "prioridade": 4},
                {"descricao": "Terminar apresentação", "prioridade": 5},
                {"descricao": "Ligar para clientes", "prioridade": 4, "clientes": []}
            ]
        }
        self.avisos = []

    def iniciar_dia(self):
        print("Assistente: Bom dia! Vamos começar nosso dia juntos.")
        self.nome_usuario = input("Assistente: Qual é o seu nome? ")
        print(f"Assistente: Olá, {self.nome_usuario}! Estou aqui para ajudar você ao longo do dia.")

    def fazer_pergunta(self, pergunta):
        return input(f"Assistente: {pergunta} ")

    def adicionar_tarefa(self, categoria):
        tarefa = self.fazer_pergunta(f"Qual tarefa de {categoria} você precisa adicionar?")
        while True:
            prioridade_str = self.fazer_pergunta("Qual a prioridade desta tarefa? (1-5, sendo 5 a mais alta)")
            try:
                prioridade = int(prioridade_str)
                if 1 <= prioridade <= 5:
                    break
                else:
                    print("Assistente: Por favor, insira um número entre 1 e 5.")
            except ValueError:
                print("Assistente: Por favor, insira apenas um número entre 1 e 5.")
        
        self.tarefas[categoria].append({"descricao": tarefa, "prioridade": prioridade})
        print(f"Assistente: Tarefa '{tarefa}' adicionada à categoria {categoria} com prioridade {prioridade}.")

    def listar_tarefas(self, categoria):
        if not self.tarefas[categoria]:
            print(f"Assistente: Não há tarefas na categoria {categoria}.")
        else:
            print(f"Tarefas de {categoria}:")
            for i, tarefa in enumerate(sorted(self.tarefas[categoria], key=lambda x: x['prioridade'], reverse=True), 1):
                print(f"{i}. [{tarefa['prioridade']}] {tarefa['descricao']}")

    def gerenciar_saude(self):
        print("\nGerenciando Saúde e Bem-estar")
        self.listar_tarefas("saude")
        acao = self.fazer_pergunta("O que você gostaria de fazer? (adicionar tarefa/definir horário exercício/beber água)")
        if acao == "adicionar tarefa":
            self.adicionar_tarefa("saude")
        elif acao == "definir horário exercício":
            horario = self.fazer_pergunta("Em que horário você deseja fazer exercício?")
            self.avisos.append(f"Fazer exercício às {horario}")
            print(f"Assistente: Aviso definido para fazer exercício às {horario}.")
        elif acao == "beber água":
            print("Assistente: Lembre-se de beber água a cada hora. Vou te avisar!")
            self.avisos.append("Beber água a cada hora")

    def gerenciar_casa(self):
        print("\nGerenciando Tarefas Domésticas")
        self.listar_tarefas("casa")
        acao = self.fazer_pergunta("O que você gostaria de fazer? (adicionar tarefa/listar tarefas)")
        if acao == "adicionar tarefa":
            self.adicionar_tarefa("casa")
        elif acao == "listar tarefas":
            self.listar_tarefas("casa")

    def gerenciar_escola(self):
        print("\nGerenciando Tarefas Escolares")
        self.listar_tarefas("escola")
        acao = self.fazer_pergunta("O que você gostaria de fazer? (adicionar tarefa/verificar material)")
        if acao == "adicionar tarefa":
            self.adicionar_tarefa("escola")
        elif acao == "verificar material":
            print("Assistente: Vamos verificar se você separou todo o material necessário.")
            verificacao = self.fazer_pergunta("Você separou todos os materiais para a escola? (sim/não)")
            if verificacao.lower() == "não":
                print("Assistente: Por favor, verifique novamente e separe todos os materiais necessários.")

    def gerenciar_trabalho(self):
        print("\nGerenciando Tarefas de Trabalho")
        self.listar_tarefas("trabalho")
        acao = self.fazer_pergunta("O que você gostaria de fazer? (adicionar tarefa/listar tarefas/gerenciar ligações)")
        if acao == "adicionar tarefa":
            self.adicionar_tarefa("trabalho")
        elif acao == "listar tarefas":
            self.listar_tarefas("trabalho")
        elif acao == "gerenciar ligações":
            self.gerenciar_ligacoes()

    def gerenciar_ligacoes(self):
        tarefa_ligacoes = next((t for t in self.tarefas["trabalho"] if t["descricao"] == "Ligar para clientes"), None)
        if not tarefa_ligacoes:
            tarefa_ligacoes = {"descricao": "Ligar para clientes", "prioridade": 4, "clientes": []}
            self.tarefas["trabalho"].append(tarefa_ligacoes)

        while True:
            print("\nGerenciando Ligações para Clientes")
            print("1. Adicionar cliente para ligar")
            print("2. Listar clientes para ligar")
            print("3. Editar cliente")
            print("4. Remover cliente")
            print("5. Voltar")

            escolha = self.fazer_pergunta("Escolha uma opção (1-5): ")

            if escolha == "1":
                self.adicionar_cliente(tarefa_ligacoes)
            elif escolha == "2":
                self.listar_clientes(tarefa_ligacoes)
            elif escolha == "3":
                self.editar_cliente(tarefa_ligacoes)
            elif escolha == "4":
                self.remover_cliente(tarefa_ligacoes)
            elif escolha == "5":
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 5.")

    def adicionar_cliente(self, tarefa_ligacoes):
        nome_cliente = self.fazer_pergunta("Nome do cliente: ")
        telefone = self.fazer_pergunta("Número de telefone do cliente: ")
        horario = self.fazer_pergunta("Horário para ligar (ex: 14:30): ")
        tarefa_ligacoes["clientes"].append({"nome": nome_cliente, "telefone": telefone, "horario": horario})
        print(f"Cliente {nome_cliente} adicionado para ligar às {horario}.")
        self.atualizar_avisos_ligacoes(nome_cliente, telefone, horario)

    def listar_clientes(self, tarefa_ligacoes):
        if not tarefa_ligacoes["clientes"]:
            print("Não há clientes agendados para ligar.")
        else:
            print("Clientes para ligar:")
            for i, cliente in enumerate(tarefa_ligacoes["clientes"], 1):
                print(f"{i}. {cliente['nome']} - Tel: {cliente['telefone']} às {cliente['horario']}")

    def editar_cliente(self, tarefa_ligacoes):
        self.listar_clientes(tarefa_ligacoes)
        if tarefa_ligacoes["clientes"]:
            indice = int(self.fazer_pergunta("Qual o número do cliente que deseja editar?")) - 1
            if 0 <= indice < len(tarefa_ligacoes["clientes"]):
                cliente = tarefa_ligacoes["clientes"][indice]
                cliente['nome'] = self.fazer_pergunta("Novo nome (ou Enter para manter): ") or cliente['nome']
                cliente['telefone'] = self.fazer_pergunta("Novo telefone (ou Enter para manter): ") or cliente['telefone']
                cliente['horario'] = self.fazer_pergunta("Novo horário (ou Enter para manter): ") or cliente['horario']
                print("Cliente atualizado com sucesso.")
                self.atualizar_avisos_ligacoes(cliente['nome'], cliente['telefone'], cliente['horario'])
            else:
                print("Índice de cliente inválido.")

    def remover_cliente(self, tarefa_ligacoes):
        self.listar_clientes(tarefa_ligacoes)
        if tarefa_ligacoes["clientes"]:
            indice = int(self.fazer_pergunta("Qual o número do cliente que deseja remover?")) - 1
            if 0 <= indice < len(tarefa_ligacoes["clientes"]):
                cliente_removido = tarefa_ligacoes["clientes"].pop(indice)
                print(f"Cliente {cliente_removido['nome']} removido com sucesso.")
                self.remover_aviso_ligacao(cliente_removido['nome'])
            else:
                print("Índice de cliente inválido.")

    def atualizar_avisos_ligacoes(self, nome_cliente, telefone, horario):
        aviso = f"Ligar para {nome_cliente} (Tel: {telefone}) às {horario}"
        self.avisos = [a for a in self.avisos if not a.startswith(f"Ligar para {nome_cliente}")]
        self.avisos.append(aviso)
        print(f"Assistente: Aviso atualizado para ligar para {nome_cliente} às {horario}.")

    def remover_aviso_ligacao(self, nome_cliente):
        self.avisos = [a for a in self.avisos if not a.startswith(f"Ligar para {nome_cliente}")]

    def revisar_tarefas(self):
        print("\nRevisando todas as tarefas:")
        for categoria in self.tarefas:
            self.listar_tarefas(categoria)

    def sugerir_proximos_passos(self):
        todas_tarefas = []
        for categoria in self.tarefas:
            todas_tarefas.extend(self.tarefas[categoria])
        
        if todas_tarefas:
            tarefa_prioritaria = max(todas_tarefas, key=lambda x: x['prioridade'])
            print(f"\nAssistente: Sugiro que você comece com a tarefa: {tarefa_prioritaria['descricao']}")
            iniciar = self.fazer_pergunta("Gostaria de começar esta tarefa agora? (sim/não)")
            if iniciar.lower() == 'sim':
                print("Assistente: Ótimo! Vamos começar. Lembre-se de fazer pausas regulares.")
                self.definir_temporizador()
            else:
                print("Assistente: Tudo bem. Quando estiver pronto, me avise e podemos revisar suas tarefas novamente.")
        else:
            print("Assistente: Você não tem tarefas registradas ainda. Que tal adicionar algumas?")

    def definir_temporizador(self):
        duracao = int(self.fazer_pergunta("Por quanto tempo você quer trabalhar nesta tarefa? (em minutos)"))
        print(f"Assistente: Ótimo! Vou te lembrar em {duracao} minutos.")
        # Simulação do temporizador
        print(f"Assistente: {duracao} minutos se passaram. É hora de fazer uma pausa!")

    def mostrar_avisos(self):
        if self.avisos:
            print("\nAvisos importantes:")
            for aviso in self.avisos:
                print(f"- {aviso}")
        else:
            print("Não há avisos no momento.")

    def finalizar_dia(self):
        print("Assistente: Vamos finalizar seu dia.")
        self.fazer_pergunta("Como você se sente sobre o que realizou hoje?")
        print(f"Assistente: Obrigado por compartilhar seu dia comigo, {self.nome_usuario}. Descanse bem e até amanhã!")

    def interagir(self):
        self.iniciar_dia()

        while True:
            self.mostrar_avisos()
            print("\nAssistente: O que você gostaria de fazer agora?")
            print("1. Gerenciar Saúde e Bem-estar")
            print("2. Organizar Casa")
            print("3. Organizar Escola")
            print("4. Organizar Trabalho")
            print("5. Revisar Todas as Tarefas")
            print("6. Sugerir Próximos Passos")
            print("7. Finalizar o dia")
            print("8. Sair")

            escolha = input("Escolha uma opção (1-8): ")

            if escolha == '1':
                self.gerenciar_saude()
            elif escolha == '2':
                self.gerenciar_casa()
            elif escolha == '3':
                self.gerenciar_escola()
            elif escolha == '4':
                self.gerenciar_trabalho()
            elif escolha == '5':
                self.revisar_tarefas()
            elif escolha == '6':
                self.sugerir_proximos_passos()
            elif escolha == '7':
                self.finalizar_dia()
            elif escolha == '8':
                print(f"Assistente: Até logo, {self.nome_usuario}! Tenha um ótimo dia.")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 8.")

def main():
    assistente = AssistenteIA()
    assistente.interagir()

if __name__ == "__main__":
    main()
