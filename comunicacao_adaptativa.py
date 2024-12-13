import random
class ComunicacaoAdaptativa:
    def __init__(self):
        self.contextos = ["escola", "casa", "trabalho"]
        self.emocoes = ["feliz", "ansioso", "frustrado", "calmo"]
        self.usuario_atual = None


    def interpretar_contexto(self, mensagem):
        # Simula a interpretação do contexto baseado em palavras-chave
        for contexto in self.contextos:
            if contexto in mensagem.lower():
                return contexto
        return random.choice(self.contextos)

    def analisar_emocao(self, mensagem):
        # Simula a análise de emoção baseada em palavras-chave
        for emocao in self.emocoes:
            if emocao in mensagem.lower():
                return emocao
        return random.choice(self.emocoes)

    def gerar_resposta(self, mensagem):
        contexto = self.interpretar_contexto(mensagem)
        emocao = self.analisar_emocao(mensagem)
        
        # Personaliza a resposta baseada no contexto e emoção
        if contexto == "escola" and emocao == "ansioso":
            return "Entendo que você está ansioso na escola. Que tal fazermos um exercício de respiração juntos?"
        elif contexto == "casa" and emocao == "feliz":
            return "Que bom que você está feliz em casa! Quer compartilhar o que está te deixando assim?"
        elif contexto == "trabalho" and emocao == "frustrado":
            return "Percebo que você está frustrado no trabalho. Vamos quebrar suas tarefas em partes menores?"
        else:
            return f"Estou aqui para te apoiar no contexto de {contexto}, percebendo que você está se sentindo {emocao}."

    def interagir(self):
        print("Bem-vindo à Plataforma de Comunicação Adaptativa!")
        self.usuario_atual = input("Como você gostaria de ser chamado? ")
        
        while True:
            mensagem = input(f"\n{self.usuario_atual}, como posso te ajudar hoje? (ou digite 'sair' para encerrar) ")
            if mensagem.lower() == 'sair':
                print("Obrigado por usar nossa plataforma. Até a próxima!")
                break
            
            resposta = self.gerar_resposta(mensagem)
            print(f"\nAssistente: {resposta}")
            
            # Feedback em tempo real
            feedback = input("Esta resposta foi útil? (sim/não) ")
            if feedback.lower() == 'não':
                print("Entendo. Vou me esforçar para melhorar minhas respostas no futuro.")

if __name__ == "__main__":
    plataforma = ComunicacaoAdaptativa()
    plataforma.interagir()
