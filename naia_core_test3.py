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
        self.contatos_emergencia = {}
        self.respostas_emocionais = {
            "cansado": ("Entendo que você está cansado. Que tal tirar um momento para relaxar? Lembre-se, descansar também é produtivo.", 
                        "Sugestão: Que tal fazer uma pausa de 10 minutos? Respire fundo, tome um copo d'água e, se possível, faça um breve alongamento."),
            "triste": ("Sinto muito que você esteja triste. Lembre-se que seus sentimentos são válidos e que isso vai passar. Estou aqui para te apoiar.", 
                       "Sugestão: Às vezes, expressar nossos sentimentos pode ajudar. Que tal escrever um pouco sobre o que está sentindo ou conversar com alguém de confiança?"),
            "realizado": ("Que maravilha! É ótimo se sentir realizado. Você merece celebrar suas conquistas!", 
                          "Sugestão: Aproveite esse momento positivo! Que tal fazer algo que você gosta como recompensa?"),
            "feliz": ("Fico muito feliz em saber que você está feliz! Seu sorriso ilumina o dia.", 
                      "Sugestão: Que tal compartilhar essa felicidade? Você poderia fazer algo legal para alguém ou simplesmente ligar para um amigo."),
            "ansioso": ("A ansiedade pode ser desafiadora. Que tal fazermos juntos um exercício de respiração para acalmar?", 
                        "Sugestão: Vamos tentar um exercício de respiração? Inspire profundamente por 4 segundos, segure por 4 e expire por 4. Repita 5 vezes."),
            "estressado": ("O estresse pode ser difícil. Vamos pensar em algumas atividades relaxantes que você gosta de fazer?", 
                           "Sugestão: Que tal uma atividade que te acalme? Pode ser ouvir uma música tranquila, fazer um desenho ou dar uma curta caminhada."),
            "animado": ("Sua animação é contagiante! Que bom ver você assim. O que está te deixando tão empolgado?", 
                        "Sugestão: Aproveite essa energia positiva! Que tal começar aquele projeto que você vem adiando?"),
            "frustrado": ("Frustração é normal às vezes. Lembre-se de que cada desafio é uma oportunidade de aprendizado.", 
                          "Sugestão: Às vezes, mudar o foco ajuda. Que tal fazer uma pausa e se dedicar a uma atividade que você goste por alguns minutos?"),
            "orgulhoso": ("Você tem todo o direito de se sentir orgulhoso! Suas conquistas são importantes e merecem ser reconhecidas.", 
                          "Sugestão: Que tal registrar essa conquista? Você poderia escrever sobre ela em um diário ou compartilhar com alguém especial."),
            "confuso": ("Entendo que você esteja confuso. Vamos tentar organizar seus pensamentos juntos?", 
                        "Sugestão: Às vezes, colocar as ideias no papel ajuda. Que tal fazer uma lista dos pontos que estão te confundindo?"),
            "motivado": ("Que ótimo que você está motivado! Vamos aproveitar essa energia para realizar algo incrível hoje?", 
                         "Sugestão: Aproveite esse momento de motivação! Que tal estabelecer uma meta para hoje e trabalhar nela?"),
            "entediado": ("O tédio pode ser uma oportunidade para explorar novos interesses. Que tal tentarmos algo novo juntos?", 
                          "Sugestão: Que tal aprender algo novo hoje? Você poderia assistir a um vídeo educativo ou começar um novo hobby."),
            "grato": ("A gratidão é um sentimento poderoso. É maravilhoso que você consiga reconhecer as coisas boas em sua vida.", 
                      "Sugestão: Que tal fazer uma lista de 3 coisas pelas quais você é grato hoje? Isso pode ajudar a manter esse sentimento positivo."),
            "sobrecarregado": ("Sentir-se sobrecarregado é comum. Vamos tentar dividir suas tarefas em partes menores e mais gerenciáveis?", 
                               "Sugestão: Vamos fazer uma lista de todas as suas tarefas e depois priorizar as 3 mais importantes para hoje?"),
            "esperançoso": ("A esperança é uma força incrível. É inspirador ver você olhando para o futuro com otimismo.", 
                            "Sugestão: Que tal definir uma meta para o futuro próximo? Algo que você possa trabalhar e que alimente essa esperança."),
            "inseguro": ("Todos nos sentimos inseguros às vezes. Lembre-se de todas as vezes que você superou desafios no passado.", 
                         "Sugestão: Que tal fazer uma lista de suas qualidades e conquistas? Isso pode ajudar a lembrar o quão capaz você é."),
            "empolgado": ("Sua empolgação é contagiante! O que te deixou assim? Vamos aproveitar esse momento!", 
                          "Sugestão: Canalize essa empolgação! Que tal começar aquele projeto que você sempre quis fazer?"),
            "calmo": ("É ótimo que você esteja se sentindo calmo. A tranquilidade nos ajuda a enfrentar os desafios com mais clareza.", 
                      "Sugestão: Aproveite esse momento de calma para refletir ou meditar. Isso pode ajudar a manter esse estado positivo."),
            "determinado": ("Sua determinação é admirável. Com essa atitude, tenho certeza de que você alcançará seus objetivos.", 
                            "Sugestão: Que tal definir um objetivo claro para hoje e trabalhar nele com toda essa determinação?"),
            "curioso": ("A curiosidade é o primeiro passo para o aprendizado. Que tal explorarmos juntos esse novo interesse?", 
                        "Sugestão: Aproveite essa curiosidade! Que tal pesquisar sobre um tópico novo que te interessa?"),
            "preocupado": ("Entendo suas preocupações. Vamos conversar sobre elas e pensar em soluções juntos?", 
                           "Sugestão: Às vezes, escrever nossas preocupações ajuda. Que tal fazer uma lista do que te preocupa e depois pensarmos em possíveis soluções?"),
            "satisfeito": ("É maravilhoso ouvir que você está satisfeito. Aproveite esse momento de contentamento!", 
                           "Sugestão: Que tal refletir sobre o que te trouxe essa satisfação? Isso pode ajudar a criar mais momentos como esse no futuro."),
            "inspirado": ("A inspiração é um combustível poderoso. O que despertou essa faísca em você hoje?", 
                          "Sugestão: Aproveite essa inspiração! Que tal começar um projeto criativo ou escrever suas ideias?"),
            "nostálgico": ("A nostalgia nos conecta com nossas raízes. Que memórias especiais estão em sua mente agora?", 
                           "Sugestão: Que tal reviver um pouco essa nostalgia? Você poderia ouvir uma música antiga favorita ou olhar fotos de bons momentos."),
            "confiante": ("Sua confiança é inspiradora. Com essa atitude, você está pronto para enfrentar qualquer desafio!", 
                          "Sugestão: Aproveite essa confiança para enfrentar algo que você vem adiando. Você está em um ótimo momento para superar desafios!"),
            "amoroso": ("O amor é um sentimento precioso. É lindo ver você transbordando afeto.", 
                        "Sugestão: Que tal expressar esse amor? Você poderia fazer algo especial para alguém que ama ou praticar um ato de bondade."),
            "agradecido": ("A gratidão enriquece nossa vida. É maravilhoso que você reconheça as bênçãos ao seu redor.", 
                           "Sugestão: Que tal escrever uma carta de agradecimento para alguém que fez diferença na sua vida?"),
            "entusiasmado": ("Seu entusiasmo é contagiante! Que projetos empolgantes você tem em mente?", 
                             "Sugestão: Canalize esse entusiasmo! Comece a planejar ou trabalhar em um projeto que te empolga."),
            "sereno": ("A serenidade é um estado valioso. Aproveite essa paz interior para refletir e recarregar.", 
                       "Sugestão: Que tal praticar mindfulness ou meditação para aproveitar ao máximo esse momento de serenidade?"),
            "otimista": ("Seu otimismo é inspirador. Com essa atitude positiva, você está pronto para aproveitar as oportunidades que surgirem!", 
                         "Sugestão: Que tal fazer uma lista de metas positivas para o futuro? Seu otimismo pode ser um grande aliado para realizá-las.")
        }

    def iniciar_dia(self):
        print("Assistente: Bom dia! Vamos começar nosso dia juntos.")
        self.nome_usuario = input("Assistente: Qual é o seu nome? ")
        print(f"Assistente: Olá, {self.nome_usuario}! É um prazer conhecer você.")
        self.verificar_estado_inicial()
        self.definir_perfil_neurodivergente()
        self.configurar_contatos_emergencia()

    def verificar_estado_inicial(self):
        estado = input("Assistente: Como você está se sentindo agora? ").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Entendo que você está se sentindo {estado}. Cada sentimento é único e importante.")
            print("Assistente: Lembre-se de que estou aqui para te apoiar no que precisar.")

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

    def configurar_contatos_emergencia(self):
        print("Assistente: Vamos configurar seus contatos de emergência.")
        familiar = input("Por favor, digite o nome e número de telefone de um familiar (ex: Maria 11999999999): ")
        medico = input("Agora, digite o nome e número de telefone do seu médico (ex: Dr. Silva 11988888888): ")
        self.contatos_emergencia['familiar'] = familiar
        self.contatos_emergencia['medico'] = medico

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
        estado = self.fazer_pergunta("Como você está se sentindo agora?").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Entendo que você está se sentindo {estado}. Saiba que estou aqui para te apoiar no que precisar.")
        
        self.verificar_pulso()
        if self.perfil_neurodivergente == "TDAH":
            self.fazer_pergunta("Você está tendo dificuldade em se concentrar hoje?")
        elif self.perfil_neurodivergente == "TEA":
            self.fazer_pergunta("Houve alguma mudança na sua rotina que o deixou desconfortável?")

    def verificar_pulso(self):
        pulso = int(self.fazer_pergunta("Qual é sua leitura de pulso atual?"))
        if pulso < 60:
            print("Assistente: Sua frequência cardíaca está baixa. Recomendo que você descanse um pouco e beba água.")
        elif pulso > 100:
            print("Assistente: Sua frequência cardíaca está alta.")
            medicacao = self.fazer_pergunta("Você já tomou sua medicação hoje?")
            if medicacao.lower() == 'não':
                print("Assistente: Por favor, tome sua medicação conforme prescrito pelo médico.")
            aviso = self.fazer_pergunta("Gostaria que eu enviasse um aviso para seu familiar ou médico? (sim/não)")
            if aviso.lower() == 'sim':
                self.enviar_aviso("Frequência cardíaca alta detectada.")
        else:
            print("Assistente: Sua frequência cardíaca está normal. Ótimo!")

    def enviar_aviso(self, mensagem):
        print("Assistente: Enviando aviso...")
        for contato, info in self.contatos_emergencia.items():
            nome, numero = info.split()
            print(f"Aviso enviado para {nome} ({numero}): {mensagem}")
        print("Assistente: Avisos enviados com sucesso.")

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
        estado = self.fazer_pergunta("Como você se sente sobre o dia de hoje?").lower()
        if estado in self.respostas_emocionais:
            resposta, sugestao = self.respostas_emocionais[estado]
            print(f"Assistente: {resposta}")
            print(f"Assistente: {sugestao}")
        else:
            print(f"Assistente: Obrigado por compartilhar como se sente. Cada dia é uma nova oportunidade. Descanse bem e amanhã será um novo começo!")

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
