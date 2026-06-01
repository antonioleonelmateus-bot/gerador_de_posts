import random
import csv
from datetime import datetime
import os

# Listas de ideias para cruzar conteúdos
temas = [
    "O impacto do tempo e dos imprevistos na nossa carreira",
    "Como a ética e a honestidade constroem uma reputação indestrutível",
    "A diferença prática entre agir por impulso e agir com sabedoria",
    "Por que esperar pelas condições perfeitas é a maior armadilha",
    "A importância de construir relacionamentos autênticos e duradouros",
    "Como transformar fracassos em lições valiosas para o crescimento",
    "O poder da consistência: pequenas ações geram grandes resultados",
    "Por que sair da zona de conforto é essencial para evoluir",
    "A mentalidade de abundância versus a mentalidade de escassez",
    "Como manter a foco e a disciplina em tempos de distração"
]

gatilhos = [
    "Foca-te no controle emocional e na resiliência mental.",
    "Lembra o teu público de que o sucesso na vida exige paciência.",
    "Desafia os teus seguidores a eliminarem uma desculpa ainda hoje.",
    "Mostra que o caráter (honra) vale mais do que o aplauso (glória)."
]

hashtags = ["#SabedoriaPratica", "#InteligenciaEmocional", "#AcaoSemDesculpas", "#LeonelMateus"]

# Função para gerar um post
def gerar_post():
    tema = random.choice(temas)
    gatilho = random.choice(gatilhos)
    hashtag = random.choice(hashtags)
    
    return {
        "tema": tema,
        "gatilho": gatilho,
        "hashtag": hashtag,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Função para exibir o post no terminal
def exibir_post(post):
    print("\n" + "="*45)
    print("🌟 INSPIRAÇÃO PARA O TEU PRÓXIMO POST 🌟")
    print("="*45)
    print(f"👉 TEMA PRINCIPAL: {post['tema']}")
    print(f"🧠 FOCO EMOCIONAL: {post['gatilho']}")
    print(f"🏷️ HASHTAG SUGERIDA: {post['hashtag']}")
    print(f"⏰ GERADO EM: {post['timestamp']}")
    print("="*45 + "\n")

# Função para salvar em arquivo TXT
def salvar_em_txt(post, filename="posts_sugestoes.txt"):
    with open(filename, "a", encoding="utf-8") as arquivo:
        arquivo.write("\n" + "="*45 + "\n")
        arquivo.write("🌟 SUGESTÃO DE POST 🌟\n")
        arquivo.write("="*45 + "\n")
        arquivo.write(f"📌 TEMA: {post['tema']}\n")
        arquivo.write(f"💡 GATILHO: {post['gatilho']}\n")
        arquivo.write(f"🏷️ HASHTAG: {post['hashtag']}\n")
        arquivo.write(f"⏰ DATA/HORA: {post['timestamp']}\n")
        arquivo.write("="*45 + "\n\n")
    print(f"✅ Post salvo em {filename}")

# Função para salvar em arquivo CSV
def salvar_em_csv(post, filename="posts_sugestoes.csv"):
    file_exists = os.path.isfile(filename)
    
    with open(filename, "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Data/Hora", "Tema", "Gatilho", "Hashtag"])
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            "Data/Hora": post['timestamp'],
            "Tema": post['tema'],
            "Gatilho": post['gatilho'],
            "Hashtag": post['hashtag']
        })
    print(f"✅ Post salvo em {filename}")

# Função para postar no Twitter (requer tweepy instalado)
def postar_no_twitter(post, api_key=None, api_secret=None, access_token=None, access_secret=None):
    """
    Para usar esta função, você precisa:
    1. Instalar tweepy: pip install tweepy
    2. Criar uma conta de desenvolvedor em https://developer.twitter.com/
    3. Gerar suas chaves de API
    4. Passar os tokens como parâmetros
    """
    try:
        import tweepy
        
        if not all([api_key, api_secret, access_token, access_secret]):
            print("❌ Erro: Credenciais do Twitter não fornecidas!")
            print("📝 Configure suas chaves de API para postar no Twitter.")
            return False
        
        # Autenticar no Twitter
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        
        # Formatar o post
        tweet = f"{post['tema']}\n\n{post['gatilho']}\n\n{post['hashtag']}"
        
        # Postar
        api.update_status(tweet)
        print("✅ Post publicado no Twitter com sucesso!")
        return True
        
    except ImportError:
        print("❌ Erro: tweepy não está instalado!")
        print("📝 Instale com: pip install tweepy")
        return False
    except Exception as e:
        print(f"❌ Erro ao postar no Twitter: {e}")
        return False

# Função principal
def main():
    print("\n🚀 BEM-VINDO AO GERADOR DE POSTS EXPANDIDO! 🚀\n")
    
    while True:
        print("Escolha uma opção:")
        print("1️⃣ Gerar nova sugestão")
        print("2️⃣ Gerar e salvar em TXT")
        print("3️⃣ Gerar e salvar em CSV")
        print("4️⃣ Gerar e postar no Twitter")
        print("5️⃣ Sair")
        
        opcao = input("\nDigite o número da opção: ").strip()
        
        if opcao == "1":
            post = gerar_post()
            exibir_post(post)
        
        elif opcao == "2":
            post = gerar_post()
            exibir_post(post)
            salvar_em_txt(post)
        
        elif opcao == "3":
            post = gerar_post()
            exibir_post(post)
            salvar_em_csv(post)
        
        elif opcao == "4":
            post = gerar_post()
            exibir_post(post)
            print("\n⚠️ Para postar no Twitter, você precisa das suas credenciais.")
            print("📝 Visite: https://developer.twitter.com/")
            # Aqui você poderia adicionar entrada de credenciais
            # postar_no_twitter(post, api_key, api_secret, access_token, access_secret)
            print("💡 Configure suas chaves no código e tente novamente.")
        
        elif opcao == "5":
            print("👋 Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
