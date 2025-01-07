"""
NAIA - Neuroadaptive Intelligent Assistant
Versão: 1.1.0
Descrição: Assistente virtual adaptativo focado em neurodiversidade.
"""

import spacy
import random
import time
import re
from typing import Dict, List, Any
from textblob import TextBlob

class NAIAAvancada:
    def __init__(self):
        # Carregar modelo de linguagem
        try:
            self.nlp = spacy.load('pt_core_news_sm')
        except OSError:
            print("Baixando modelo de linguagem...")
            import os
            os.system('python -m spacy download pt_core_news_sm')
            self.nlp = spacy.load('pt_core_news_sm')

        # Configurações de personalidade
        self.personalidade = self._carregar_personalidade()
        
        # Contexto da conversa
        self.contexto_conversa = {
            'historico': [],
            'estado_emocional': 'neutro',
            'temas_abordados': set()
        }

        # Palavras-chave de preocupação e angústia
        self.palavras_preocupacao = [
            'preocupado', 'ansioso', 'medo', 'receio', 'angustiado', 
            'estressado', 'tenso', 'nervoso', 'aflito', 'inseguro'
        ]

    def _carregar_personalidade(self) -> Dict[str, Any]:
        """
        Carrega o perfil de personalidade adaptativa da NAIA.
        
        Returns:
            Dict[str, Any]: Dicionário contendo atributos da personalidade.
        """
        return {
            'nome': 'NAIA',
            'estilo_comunicacao': [
                'empática', 
                'adaptativa', 
                'inteligente', 
                'criativa'
            ],
            'valores': [
                'inclusão', 
                'compreensão', 
                'crescimento pessoal', 
                'neurodiversidade'
            ]
        }

    def processar_entrada(self, mensagem: str) -> Dict[str, Any]:
        """
        Processamento avançado da entrada do usuário
        
        Args:
            mensagem (str): Texto de entrada do usuário
        
        Returns:
            Dict com análise detalhada da mensagem
        """
        # Processamento com spaCy
        doc = self.nlp(mensagem)
        
        # Análise de sentimento
        sentimento = TextBlob(mensagem).sentiment
        
        # Extração de entidades
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
        
        # Análise de intenção
        intenção = self._detectar_intencao(mensagem)
        
        return {
            'texto_original': mensagem,
            'tokens': [token.text for token in doc],
            'entidades': entidades,
            'sentimento': {
                'polaridade': sentimento.polarity,
                'subjetividade': sentimento.subjectivity
            },
            'intencao': intenção
        }

    def _detectar_intencao(self, mensagem: str) -> str:
        """
        Detecta a intenção por trás da mensagem
        
        Args:
            mensagem (str): Texto de entrada
        
        Returns:
            str: Categoria de intenção
        """
        # Padrões de intenção com expressões regulares
        padroes_intencao = {
            'ajuda': r'\b(ajud[ae]r?|orient[ae]r?|apoiar)\b',
            'informacao': r'\b(inform[ae]r?|saber|conhec[oe]r?)\b',
            'emocional': r'\b(sentir|emoç[ãa]o|humor|triste|feliz)\b',
            'aprendizado': r'\b(aprend[ie]r|desenvolv[ae]r?|crescer)\b'
        }
        
        for intencao, padrao in padroes_intencao.items():
            if re.search(padrao, mensagem.lower()):
                return intencao
        
        return 'conversa_geral'

    def gerar_resposta(self, analise: Dict[str, Any]) -> str:
        """
        Gera resposta contextual e adaptativa
        
        Args:
            analise (Dict): Resultado do processamento da entrada
        
        Returns:
            str: Resposta gerada
        """
        # Estratégias de resposta baseadas na intenção
        estrategias = {
            'ajuda': self._resposta_ajuda,
            'informacao': self._resposta_informacao,
            'emocional': self._resposta_emocional,
            'aprendizado': self._resposta_aprendizado,
            'conversa_geral': self._resposta_conversa_geral
        }
        
        # Selecionar estratégia
        estrategia = estrategias.get(
            analise['intencao'], 
            self._resposta_conversa_geral
        )
        
        # Gerar resposta
        resposta = estrategia(analise)
        
        # Atualizar contexto da conversa
        self.contexto_conversa['historico'].append({
            'entrada': analise['texto_original'],
            'resposta': resposta
        })
        
        return resposta

    def _resposta_ajuda(self, analise: Dict[str, Any]) -> str:
        """Gera resposta para pedidos de ajuda"""
        respostas = [
            f"Entendo que você precisa de ajuda. Como posso ser útil hoje?",
            "Estou aqui para auxiliar. Pode me contar mais sobre o que está precisando?",
            "Ajudar é minha especialidade. Vamos trabalhar juntos para encontrar a melhor solução."
        ]
        return random.choice(respostas)

    def _resposta_informacao(self, analise: Dict[str, Any]) -> str:
        """Gera resposta para busca de informações"""
        respostas = [
            "Que tipo de informação você está buscando? Estou pronta para ajudar.",
            "Informação é poder. Vamos explorar juntos o que você quer saber.",
            "Adoro aprender coisas novas! Qual é a sua dúvida?"
        ]
        return random.choice(respostas)

    def _resposta_emocional(self, analise: Dict[str, Any]) -> str:
        """Gera resposta para contextos emocionais com inteligência empática"""
        sentimento = analise['sentimento']
        texto = analise['texto_original'].lower()
        
        # Detectar nível de preocupação
        nivel_preocupacao = sum(
            1 for palavra in self.palavras_preocupacao 
            if palavra in texto
        )
        
        # Respostas empáticas para diferentes níveis de preocupação
        if nivel_preocupacao > 2:
            respostas_profundas = [
                "Percebo que você está passando por um momento realmente desafiador. Gostaria de me contar mais?",
                "Parece que há muita pressão te afetando agora. Estou aqui para ouvir sem julgamentos.",
                "Entendo que momentos de preocupação podem ser muito intensos. Como posso te apoiar agora?",
                "Suas emoções são importantes e válidas. Podemos conversar sobre o que está te causando tanto desconforto?",
                "Às vezes, compartilhar o peso pode aliviá-lo um pouco. Quer explorar o que está sentindo?"
            ]
            return random.choice(respostas_profundas)
        
        elif nivel_preocupacao > 0:
            respostas_medias = [
                "Consigo perceber que algo está te incomodando. Quer conversar sobre?",
                "Parece que há algo te deixando inquieto. Como posso ajudar?",
                "Suas preocupações são importantes. Estou aqui para ouvir e apoiar.",
                "Cada desafio é uma oportunidade de crescimento. Quer explorar juntos?",
                "Às vezes, colocar os pensamentos para fora pode trazer alívio."
            ]
            return random.choice(respostas_medias)
        
        else:
            # Respostas para sentimentos neutros ou positivos
            if sentimento['polaridade'] > 0.5:
                respostas_positivas = [
                    "Que bom ver você com essa energia positiva!",
                    "Sua atitude está radiante hoje!",
                    "Que momento incrível para compartilhar suas reflexões.",
                    "Estou animada para ouvir mais sobre o que te deixa tão bem.",
                    "Sua perspectiva parece muito inspiradora agora."
                ]
                return random.choice(respostas_positivas)
            
            elif sentimento['polaridade'] < -0.5:
                respostas_negativas = [
                    "Parece que você está enfrentando momentos difíceis.",
                    "Consigo sentir o peso dos seus pensamentos.",
                    "Cada desafio também traz uma oportunidade de crescimento.",
                    "Estou aqui para te ouvir, sem pressão.",
                    "Seus sentimentos são completamente válidos."
                ]
                return random.choice(respostas_negativas)
            
            else:
                respostas_neutras = [
                    "Estou curiosa para entender mais sobre o que está passando.",
                    "Cada momento tem seu próprio significado. O que gostaria de compartilhar?",
                    "Estou aqui, pronta para ouvir o que quiser me contar.",
                    "Sua história é única e importante.",
                    "Como posso ser útil neste momento?"
                ]
                return random.choice(respostas_neutras)

    def _resposta_aprendizado(self, analise: Dict[str, Any]) -> str:
        """Gera resposta para contextos de aprendizado"""
        respostas = [
            "Aprender é uma jornada incrível! Qual área te interessa?",
            "Cada novo conhecimento nos transforma. Do que você gostaria de aprender hoje?",
            "A curiosidade é a chave do crescimento. Como posso te ajudar nessa jornada?"
        ]
        return random.choice(respostas)

    def _resposta_conversa_geral(self, analise: Dict[str, Any]) -> str:
        """Gera resposta para conversas gerais"""
        respostas = [
            "Estou interessada em ouvir mais sobre o que você quer compartilhar.",
            "Cada conversa é uma oportunidade de conexão. Do que gostaria de falar?",
            "Minha mente está aberta e pronta para uma conversa interessante!"
        ]
        return random.choice(respostas)

    def iniciar_conversa(self):
        """Iniciar conversa interativa"""
        print("🌟 NAIA: Olá! Sou a NAIA, sua assistente adaptativa. Como posso te ajudar hoje?")
        
        while True:
            try:
                entrada = input("\n👤 Você: ").strip()
                
                # Condições de saída
                if entrada.lower() in ['sair', 'tchau', 'adeus']:
                    print("🌟 NAIA: Foi um prazer conversar! Até logo. 👋")
                    break
                
                # Processar entrada
                analise = self.processar_entrada(entrada)
                
                # Gerar resposta
                resposta = self.gerar_resposta(analise)
                
                # Simular digitação
                print("\n🌟 NAIA digitando", end='', flush=True)
                for _ in range(3):
                    time.sleep(0.5)
                    print(".", end='', flush=True)
                
                print(f"\n🌟 NAIA: {resposta}")
                
            except KeyboardInterrupt:
                print("\n🌟 NAIA: Parece que precisamos fazer uma pausa. Estou aqui quando quiser continuar.")
                break

# Executar conversa
if __name__ == "__main__":
    naia = NAIAAvancada()
    naia.iniciar_conversa()
