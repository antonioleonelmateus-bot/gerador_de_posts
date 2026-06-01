"""
ASSISTENTE DE ESTRATÉGIA DE CONTEÚDO
====================================
Assistente inteligente que aprende sua essência através de:
1. Conversas (diálogo contínuo)
2. Análise de posts (padrões históricos)
3. Feedback (validação/rejeição de sugestões)

O assistente evolui e se adapta ao seu perfil profissional.
"""

import json
import os
from datetime import datetime
from collections import defaultdict
import re

class EssenciaProfile:
    """Armazena e evolui a essência do usuário"""
    
    def __init__(self, filename="essencia_profile.json"):
        self.filename = filename
        self.profile = self._load_profile()
    
    def _load_profile(self):
        """Carrega perfil existente ou cria novo"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        
        return {
            "criado_em": datetime.now().isoformat(),
            "atualizado_em": datetime.now().isoformat(),
            "temas_principais": {},  # {tema: score}
            "horarios_ideais": {},    # {hora: score}
            "dias_ideais": {},        # {dia: score}
            "palavras_chave": {},     # {palavra: frequencia}
            "valores": [],            # ["autenticidade", "consistência", ...]
            "conversas": [],          # histórico de conversas
            "posts_analisados": 0,
            "feedback_dado": 0
        }
    
    def save(self):
        """Salva o perfil em JSON"""
        self.profile["atualizado_em"] = datetime.now().isoformat()
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.profile, f, ensure_ascii=False, indent=2)
        print(f"✅ Essência salva!")
    
    def adicionar_valor(self, valor):
        """Adiciona um valor/essência identificado"""
        if valor not in self.profile["valores"]:
            self.profile["valores"].append(valor)
            print(f"➕ Novo valor identificado: {valor}")
    
    def adicionar_conversas(self, usuario_msg, ia_msg):
        """Registra conversa com você"""
        self.profile["conversas"].append({
            "timestamp": datetime.now().isoformat(),
            "usuario": usuario_msg,
            "assistente": ia_msg
        })
    
    def atualizar_tema(self, tema, score=1):
        """Atualiza score de um tema"""
        self.profile["temas_principais"][tema] = \
            self.profile["temas_principais"].get(tema, 0) + score
    
    def atualizar_horario(self, hora, score=1):
        """Atualiza horário ideal"""
        self.profile["horarios_ideais"][hora] = \
            self.profile["horarios_ideais"].get(hora, 0) + score
    
    def atualizar_dia(self, dia, score=1):
        """Atualiza dia ideal"""
        self.profile["dias_ideais"][dia] = \
            self.profile["dias_ideais"].get(dia, 0) + score
    
    def get_top_temas(self, top=5):
        """Retorna temas principais"""
        return sorted(
            self.profile["temas_principais"].items(),
            key=lambda x: x[1],
            reverse=True
        )[:top]
    
    def get_essencia_summary(self):
        """Retorna resumo da essência atual"""
        return {
            "valores": self.profile["valores"],
            "temas_top": self.get_top_temas(3),
            "conversas_total": len(self.profile["conversas"]),
            "posts_analisados": self.profile["posts_analisados"],
            "atualizado_em": self.profile["atualizado_em"]
        }


class AnalisadorPosts:
    """Analisa posts para extrair padrões"""
    
    @staticmethod
    def extrair_temas(texto):
        """Extrai temas principais do texto"""
        # Regex simples para palavras-chave
        palavras_chave = re.findall(r'\b[A-Z][a-záéíóú]+(?:\s+[A-Z][a-záéíóú]+)?\b', texto)
        return palavras_chave
    
    @staticmethod
    def calcular_engajamento(reacoes, comentarios, compartilhamentos):
        """Calcula taxa de engajamento"""
        return reacoes + (comentarios * 2) + (compartilhamentos * 3)
    
    @staticmethod
    def analisar_post(post):
        """Analisa um post individual"""
        return {
            "texto": post.get("texto", ""),
            "data": post.get("data", ""),
            "hora": post.get("hora", ""),
            "temas": AnalisadorPosts.extrair_temas(post.get("texto", "")),
            "engajamento": AnalisadorPosts.calcular_engajamento(
                post.get("reacoes", 0),
                post.get("comentarios", 0),
                post.get("compartilhamentos", 0)
            )
        }


class AssistenteEstrategia:
    """Assistente principal que aprende e recomenda"""
    
    def __init__(self):
        self.essencia = EssenciaProfile()
        self.analisador = AnalisadorPosts()
        self.historico_posts = []
    
    def dialogar(self, mensagem_usuario):
        """Diálogo com o usuário para aprender essência"""
        
        resposta = self._processar_mensagem(mensagem_usuario)
        self.essencia.adicionar_conversas(mensagem_usuario, resposta)
        self.essencia.save()
        
        return resposta
    
    def _processar_mensagem(self, msg):
        """Processa mensagem e aprende"""
        
        msg_lower = msg.lower()
        
        # Detecta valores/essência
        valores_detectados = {
            "autenticidade": ["autentico", "genuino", "real", "verdadeiro"],
            "consistência": ["consistente", "regular", "frequente", "diario"],
            "impacto": ["impacto", "alcance", "influencia", "transformar"],
            "sabedoria": ["sabedoria", "conhecimento", "aprendizado", "crescimento"],
            "conexão": ["conexao", "comunidade", "relacionamento", "engajamento"]
        }
        
        for valor, palavras in valores_detectados.items():
            if any(palavra in msg_lower for palavra in palavras):
                self.essencia.adicionar_valor(valor)
        
        # Resposta do assistente
        resposta = f"""
🤖 ASSISTENTE DE ESTRATÉGIA

Obrigado por compartilhar isso! Estou aprendendo sua essência...

📊 Resumo do que compreendi até agora:
- Valores identificados: {', '.join(self.essencia.profile['valores']) or 'Ainda aprendendo...'}
- Conversas registradas: {len(self.essencia.profile['conversas'])}
- Posts analisados: {self.essencia.profile['posts_analisados']}

💡 Próximos passos:
1. Continue conversando comigo (aprendo mais cada vez)
2. Compartilhe seus posts passados
3. Dê feedback sobre minhas recomendações

🎯 Objetivo: Evoluir para um assistente único que entende sua essência!
"""
        return resposta
    
    def analisar_posts_facebook(self, posts):
        """Analisa histórico de posts do Facebook"""
        
        print(f"\n📊 Analisando {len(posts)} posts...")
        
        for post in posts:
            analise = self.analisador.analisar_post(post)
            self.historico_posts.append(analise)
            
            # Atualiza essência baseado em posts
            for tema in analise["temas"]:
                self.essencia.atualizar_tema(tema, analise["engajamento"])
            
            # Atualiza horários/dias
            if "hora" in post:
                self.essencia.atualizar_horario(post["hora"])
            if "dia" in post:
                self.essencia.atualizar_dia(post["dia"])
        
        self.essencia.profile["posts_analisados"] = len(posts)
        self.essencia.save()
        
        print(f"✅ Posts analisados! Essência atualizada.")
    
    def gerar_recomendacao(self, tipo="proximo_post"):
        """Gera recomendação baseada na essência aprendida"""
        
        temas_top = self.essencia.get_top_temas(3)
        valores = self.essencia.profile["valores"]
        
        if not temas_top and not valores:
            return "📝 Ainda estou aprendendo sua essência. Continue compartilhando posts e conversando!"
        
        recomendacao = f"""
🎯 RECOMENDAÇÃO PARA PRÓXIMO POST

📌 Temas sugeridos (baseado em performance):
"""
        for tema, score in temas_top:
            recomendacao += f"   • {tema} (score: {score})\n"
        
        recomendacao += f"""
✨ Alinhado com sua essência:
   • {', '.join(valores) if valores else 'Ainda aprendendo...'}

⏰ Melhor horário: {self._encontrar_melhor_horario()}
📅 Melhor dia: {self._encontrar_melhor_dia()}

💡 Estratégia:
   1. Combine os temas sugeridos com sua essência
   2. Mantenha autenticidade
   3. Poste no horário recomendado
   4. Valide os resultados comigo depois!
"""
        return recomendacao
    
    def _encontrar_melhor_horario(self):
        """Encontra melhor horário baseado em análise"""
        if not self.essencia.profile["horarios_ideais"]:
            return "Ainda aprendendo..."
        
        melhor = max(
            self.essencia.profile["horarios_ideais"].items(),
            key=lambda x: x[1]
        )
        return f"{melhor[0]} (score: {melhor[1]})"
    
    def _encontrar_melhor_dia(self):
        """Encontra melhor dia baseado em análise"""
        if not self.essencia.profile["dias_ideais"]:
            return "Ainda aprendendo..."
        
        melhor = max(
            self.essencia.profile["dias_ideais"].items(),
            key=lambda x: x[1]
        )
        return f"{melhor[0]} (score: {melhor[1]})"
    
    def mostrar_essencia(self):
        """Mostra essência aprendida até agora"""
        summary = self.essencia.get_essencia_summary()
        
        print("\n" + "="*50)
        print("🧠 SUA ESSÊNCIA ATUAL")
        print("="*50)
        print(f"✨ Valores: {', '.join(summary['valores']) or 'Ainda aprendendo...'}")
        print(f"📊 Temas principais: {summary['temas_top']}")
        print(f"💬 Conversas: {summary['conversas_total']}")
        print(f"📝 Posts analisados: {summary['posts_analisados']}")
        print(f"🔄 Atualizado em: {summary['atualizado_em']}")
        print("="*50 + "\n")


def main():
    """Menu principal do assistente"""
    
    print("\n" + "="*60)
    print("🚀 BEM-VINDO AO ASSISTENTE DE ESTRATÉGIA DE CONTEÚDO")
    print("="*60)
    print("Vou aprender sua essência ao longo do tempo!")
    print("="*60 + "\n")
    
    assistente = AssistenteEstrategia()
    
    while True:
        print("\n📋 Escolha uma opção:")
        print("1️⃣ Conversar comigo (diálogo)")
        print("2️⃣ Analisar meus posts")
        print("3️⃣ Gerar recomendação")
        print("4️⃣ Ver minha essência")
        print("5️⃣ Sair")
        
        opcao = input("\n👉 Digite a opção: ").strip()
        
        if opcao == "1":
            msg = input("\n💬 O que você quer compartilhar comigo?\n> ")
            resposta = assistente.dialogar(msg)
            print(resposta)
        
        elif opcao == "2":
            print("\n📝 Digite seus posts (formato JSON):")
            print("Exemplo: {\"texto\": \"...\", \"data\": \"2026-06-01\", \"hora\": \"14:30\", \"reacoes\": 45, \"comentarios\": 10, \"compartilhamentos\": 5}")
            try:
                posts_json = input("\n> ")
                posts = json.loads(posts_json)
                if not isinstance(posts, list):
                    posts = [posts]
                assistente.analisar_posts_facebook(posts)
            except json.JSONDecodeError:
                print("❌ JSON inválido!")
        
        elif opcao == "3":
            recomendacao = assistente.gerar_recomendacao()
            print(recomendacao)
        
        elif opcao == "4":
            assistente.mostrar_essencia()
        
        elif opcao == "5":
            print("👋 Até logo! Continuo aprendendo sua essência...")
            break
        
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()
