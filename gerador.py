import random

# Listas de ideias para cruzar conteúdos
temas = [
    "O impacto do tempo e dos imprevistos na nossa carreira",
    "Como a ética e a honestidade constroem uma reputação indestrutível",
    "A diferença prática entre agir por impulso e agir com sabedoria",
    "Por que esperar pelas condições perfeitas é a maior armadilha"
]

gatilhos = [
    "Foca-te no controle emocional e na resiliência mental.",
    "Lembra o teu público de que o sucesso na vida exige paciência.",
    "Desafia os teus seguidores a eliminarem uma desculpa ainda hoje.",
    "Mostra que o caráter (honra) vale mais do que o aplauso (glória)."
]

hashtags = ["#SabedoriaPratica", "#InteligenciaEmocional", "#AcaoSemDesculpas", "#LeonelMateus"]

# Lógica para escolher um elemento aleatório de cada lista
tema_escolhido = random.choice(temas)
gatilho_escolhido = random.choice(gatilhos)
tag_escolhida = random.choice(hashtags)

# Exibir a sugestão de post formatada no ecrã
print("\n" + "="*45)
print("🌟 INSPIRAÇÃO PARA O TEU PRÓXIMO POST 🌟")
print("="*45)
print(f"👉 TEMA PRINCIPAL: {tema_escolhido}")
print(f"🧠 FOCO EMOCIONAL: {gatilho_escolhido}")
print(f"🏷️ HASHTAG SUGERIDA: {tag_escolhida}")
print("="*45 + "\n")

