import random
from datetime import datetime

class AssistenteIA:
    def __init__(self):
        self.nome_usuario = ""
        self.respostas = {}
        self.tarefas = []

    def iniciar_dia(self):
        print("Assistente: Bom dia! Vamos começar nosso dia juntos.")
        self.nome_usuario = input("Assistente: Qual é o seu nome? ")
        print(f"Assistente: Olá, {self.nome_usuario}! Estou aqui para ajudar você ao longo do dia.")

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
        self.iniciar_dia()

        while True:
            print("\nAssistente: O que você gostaria de fazer agora?")
            print("1. Verificar estado emocional e saúde")
            print("2. Gerenciar medicações")
            print("3. Cuidados pessoais")
            print("4. Organizar tarefas")
            print("5. Finalizar o dia")
            print("6. Sair")

            escolha = input("Escolha uma opção (1-6): ")

            if escolha == '1':
                self.verificar_estado()
            elif escolha == '2':
                self.gerenciar_medicacoes()
            elif escolha == '3':
                self.cuidados_pessoais()
            elif escolha == '4':
                self.organizar_tarefas()
            elif escolha == '5':
                self.finalizar_dia()
            elif escolha == '6':
                print(f"Assistente: Até logo, {self.nome_usuario}! Tenha um ótimo dia.")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 6.")

    def verificar_estado(self):
        self.fazer_pergunta("Como você está se sentindo agora?")
        self.fazer_pergunta("Qual é sua leitura de pulso atual?")

    def gerenciar_medicacoes(self):
        self.fazer_pergunta("Quais medicações você precisa tomar agora?")
        self.fazer_pergunta("A que horas você tomou suas medicações?")

    def cuidados_pessoais(self):
        self.sugerir_atividade("tomar um banho")
        self.sugerir_atividade("escovar os dentes")
        self.fazer_pergunta("O que você planeja comer na próxima refeição?")

    def organizar_tarefas(self):
        nova_tarefa = self.fazer_pergunta("Qual tarefa você precisa realizar?")
        self.tarefas.append(nova_tarefa)
        print("Suas tarefas atuais são:")
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa}")

    def finalizar_dia(self):
        print("Assistente: Vamos organizar o final do seu dia.")
        self.sugerir_atividade("tomar um banho relaxante")
        self.sugerir_atividade("molhar as plantas")
        self.sugerir_atividade("alimentar seu animal de estimação")
        self.fazer_pergunta("O que você planeja jantar?")
        self.sugerir_atividade("escovar os dentes")
        self.fazer_pergunta("Como você se sente sobre o dia de hoje?")

def main():
    assistente = AssistenteIA()
    assistente.interagir()

if __name__ == "__main__":
    main()
