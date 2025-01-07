import os
import openai
import streamlit as st
import spacy
import random
import time
import re
from typing import Dict, List, Any
from textblob import TextBlob
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

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
        return {
            'nome': 'NAIA',
            'estilo_comunicacao': [
                'empática', 'adaptativa', 'inteligente', 'criativa'
            ],
            'valores': [
                'inclusão', 'compreensão', 'crescimento pessoal', 'neurodiversidade'
            ]
        }

    def processar_entrada(self, mensagem: str) -> Dict[str, Any]:
        doc = self.nlp(mensagem)
        sentimento = TextBlob(mensagem).sentiment
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
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
        estrategias = {
            'ajuda': self._resposta_ajuda,
            'informacao': self._resposta_informacao,
            'emocional': self._resposta_emocional,
            'aprendizado': self._resposta_aprendizado,
            'conversa_geral': self._resposta_conversa_geral
        }
        
        estrategia = estrategias.get(analise['intencao'], self._resposta_conversa_geral)
        resposta = estrategia(analise)
        
        self.contexto_conversa['historico'].append({
            'entrada': analise['texto_original'],
            'resposta': resposta
        })
        
        return resposta

    def _resposta_ajuda(self, analise: Dict[str, Any]) -> str:
        respostas = [
            f"Entendo que você precisa de ajuda. Como posso ser útil hoje?",
            "Estou aqui para auxiliar. Pode me contar mais sobre o que está precisando?",
            "Ajudar é minha especialidade. Vamos trabalhar juntos para encontrar a melhor solução."
        ]
        return random.choice(respostas)

    def _resposta_informacao(self, analise: Dict[str, Any]) -> str:
        respostas = [
            "Que tipo de informação você está buscando? Estou pronta para ajudar.",
            "Informação é poder. Vamos explorar juntos o que você quer saber.",
            "Adoro aprender coisas novas! Qual é a sua dúvida?"
        ]
        return random.choice(respostas)

    def _resposta_emocional(self, analise: Dict[str, Any]) -> str:
        sentimento = analise['sentimento']
        texto = analise['texto_original'].lower()
        
        nivel_preocupacao = sum(1 for palavra in self.palavras_preocupacao if palavra in texto)
        
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
        respostas = [
            "Aprender é uma jornada incrível! Qual área te interessa?",
            "Cada novo conhecimento nos transforma. Do que você gostaria de aprender hoje?",
            "A curiosidade é a chave do crescimento. Como posso te ajudar nessa jornada?"
        ]
        return random.choice(respostas)

    def _resposta_conversa_geral(self, analise: Dict[str, Any]) -> str:
        respostas = [
            "Estou interessada em ouvir mais sobre o que você quer compartilhar.",
            "Cada conversa é uma oportunidade de conexão. Do que gostaria de falar?",
            "Minha mente está aberta e pronta para uma conversa interessante!"
        ]
        return random.choice(respostas)

# Função para obter resposta do ChatGPT
def obter_resposta_chatgpt(mensagens):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensagens
        )
        return resposta.choices[0].message["content"]
    except Exception as e:
        return f"Erro ao acessar a API do ChatGPT: {e}"

# Configuração da página Streamlit
st.set_page_config(page_title="NAIA - Assistente Neuroadaptativa", page_icon="🧠")

# Interface do Streamlit
st.title("NAIA - Assistente Neuroadaptativa")

# Inicializar NAIA
if 'naia' not in st.session_state:
    st.session_state.naia = NAIAAvancada()

# Inicializar histórico de mensagens
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Exibir histórico de mensagens
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# Entrada do usuário
if prompt := st.chat_input("Digite sua mensagem para a NAIA:"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processar entrada com NAIA
    analise = st.session_state.naia.processar_entrada(prompt)
    resposta_naia = st.session_state.naia.gerar_resposta(analise)

    # Obter resposta do ChatGPT
    mensagens_chatgpt = [
        {"role": "system", "content": "Você é NAIA, uma assistente neuroadaptativa focada em inclusão e neurodiversidade."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": resposta_naia}
    ]
    resposta_chatgpt = obter_resposta_chatgpt(mensagens_chatgpt)

    # Combinar respostas
    resposta_final = f"{resposta_naia}\n\nAdicional do ChatGPT: {resposta_chatgpt}"

    # Exibir resposta da NAIA
    with st.chat_message("assistant"):
        st.markdown(resposta_final)
    
    # Adicionar resposta da NAIA ao histórico
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_final})

# Botão para limpar o histórico
if st.button("Limpar Conversa"):
    st.session_state.mensagens = []
    st.experimental_rerun()

# Exibir informações sobre a NAIA
with st.expander("Sobre a NAIA"):
    st.write("""
    NAIA é uma Assistente Neuroadaptativa de Inteligência Artificial, projetada para fornecer suporte e informações sobre neurodiversidade e inclusão.
    Ela é capaz de adaptar sua comunicação para atender às necessidades específicas de cada usuário.
    """)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️ para promover a inclusão e compreensão da neurodiversidade.")
