import random
import time
from datetime import datetime

class AssistenteIA:
    def __init__(self):
        self.nome_usuario = ""
        self.respostas = {}
        self.tarefas = []
        self.perfil_neurodivergente = None
        self.tempo_foco = 0

    def iniciar_dia(self):
        print("Assistente: Bom dia! Vamos começar nosso dia juntos.")
        self.nome_usuario = input("Assistente: Qual é o seu nome? ")
        print(f"Assistente: Olá, {self.nome_usuario}! Estou aqui para ajudar você ao longo do dia.")
        self.definir_perfil_neurodivergente()

    def definir_perfil_neurodivergente(self):
        print("Assistente: Para melhor atendê-lo, preciso saber um pouco mais sobre você.")
        print("1. TDAH")
        print("2. TEA")
        print("3. Outro")
        escolha = input("Por favor, escolha uma opção (1-3): ")
        if escolha == '1':
            self.perfil_neurodivergente = "TDAH"
            self.tempo_foco = 15  # 15 minutos de foco para TDAH
        elif escolha == '2':
            self.perfil_neurodivergente = "TEA"
            self.tempo_foco = 30  # 30 minutos de foco para TEA
        else:
            self.perfil_neurodivergente = "Outro"
            self.tempo_foco = 20  # 20 minutos de foco para outros perfis

    def fazer_pergunta(self, pergunta):
        resposta = input(f"Assistente: {pergunta} ")
        self.respostas[pergunta] = resposta
        return resposta

    def sugerir_atividade(self, atividade):
        print(f"Assistente: Que tal {atividade} agora?")
        resposta = input("Você (responda 'ok' quando terminar ou 'pular' para outra atividade): ")
        while resposta.lower() not in ['ok', 'pular']:
            resposta = input("Você (responda 'ok' quando terminar ou 'pular' para outra atividade): ")
        return resposta.lower() == 'ok'

    def interagir(self):
        print("\nAssistente: O que você gostaria de fazer agora?")
        print("1. Verificar estado emocional e saúde")
        print("2. Gerenciar medicações")
        print("3. Cuidados pessoais")
        print("4. Organizar tarefas")
        print("5. Iniciar sessão de foco")
        print("6. Finalizar o dia")
        print("7. Sair")

        escolha = input("Escolha uma opção (1-7): ")

        if escolha == '1':
            self.verificar_estado()
        elif escolha == '2':
            self.gerenciar_medicacoes()
        elif escolha == '3':
            self.cuidados_pessoais()
        elif escolha == '4':
            self.organizar_tarefas()
        elif escolha == '5':
            self.iniciar_sessao_foco()
        elif escolha == '6':
            self.finalizar_dia()
        elif escolha == '7':
            print(f"Assistente: Até logo, {self.nome_usuario}! Tenha um ótimo dia.")
            return False
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 7.")
        return True

    def verificar_estado(self):
        self.fazer_pergunta("Como você está se sentindo agora?")
        self.fazer_pergunta("Qual é sua leitura de pulso atual?")
        if self.perfil_neurodivergente == "TDAH":
            self.fazer_pergunta("Você está tendo dificuldade em se concentrar hoje?")
        elif self.perfil_neurodivergente == "TEA":
            self.fazer_pergunta("Houve alguma mudança na sua rotina que o deixou desconfortável?")

    def gerenciar_medicacoes(self):
        self.fazer_pergunta("Quais medicações você precisa tomar agora?")
        self.fazer_pergunta("A que horas você tomou suas medicações?")
        print("Assistente: Vou configurar um lembrete para sua próxima dose.")

    def cuidados_pessoais(self):
        self.sugerir_atividade("tomar um banho")
        self.sugerir_atividade("escovar os dentes")
        self.fazer_pergunta("O que você planeja comer na próxima refeição?")
        if self.perfil_neurodivergente in ["TDAH", "TEA"]:
            self.sugerir_atividade("fazer um exercício de respiração por 2 minutos")

    def organizar_tarefas(self):
        nova_tarefa = self.fazer_pergunta("Qual tarefa você precisa realizar?")
        self.tarefas.append(nova_tarefa)
        print("Suas tarefas atuais são:")
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa}")
        if self.perfil_neurodivergente == "TDAH":
            print("Assistente: Lembre-se de dividir suas tarefas em etapas menores para facilitar o foco.")
        elif self.perfil_neurodivergente == "TEA":
            print("Assistente: Vamos criar uma rotina visual para suas tarefas?")

    def iniciar_sessao_foco(self):
        print(f"Assistente: Vamos iniciar uma sessão de foco de {self.tempo_foco} minutos.")
        print("Concentre-se em uma tarefa específica durante esse tempo.")
        for i in range(self.tempo_foco, 0, -1):
            print(f"Tempo restante: {i} minutos")
            time.sleep(1)  # Espera 1 segundo (simulando 1 minuto para a demonstração)
        print("Assistente: Sessão de foco concluída! Ótimo trabalho!")

    def finalizar_dia(self):
        print("Assistente: Vamos organizar o final do seu dia.")
        self.sugerir_atividade("tomar um banho relaxante")
        self.sugerir_atividade("molhar as plantas")
        self.sugerir_atividade("alimentar seu animal de estimação")
        self.fazer_pergunta("O que você planeja jantar?")
        self.sugerir_atividade("escovar os dentes")
        self.fazer_pergunta("Como você se sente sobre o dia de hoje?")

def demonstracao_3_minutos():
    inicio = time.time()
    duracao = 180  # 3 minutos em segundos

    assistente = AssistenteIA()
    assistente.iniciar_dia()

    print("Iniciando demonstração de 3 minutos...")

    while time.time() - inicio < duracao:
        if not assistente.interagir():
            break
        time_restante = duracao - (time.time() - inicio)
        print(f"Tempo restante: {int(time_restante)} segundos")

    print("Demonstração concluída!")

if __name__ == "__main__":
    demonstracao_3_minutos()
