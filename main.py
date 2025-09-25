import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv


load_dotenv()

print("SISTEMA MULTIAGENTE - RESUMOS DE IA")
print("Powered only by Groq")
print("=" * 40)

# modelo válido do Groq
GROQ_MODEL = "groq/llama-3.1-8b-instant"

#  Definição dos agentes
pesquisador = Agent(
    role="Pesquisador de Notícias de IA",
    goal="Pesquisar as 5 principais notícias sobre Inteligência Artificial e Machine Learning.",
    backstory="Você é um pesquisador que acompanha diariamente o cenário de IA.",
    verbose=True,
    allow_delegation=False,
    llm=GROQ_MODEL
)

resumidor = Agent(
    role="Resumidor de Notícias de IA",
    goal="Resumir as principais notícias coletadas sobre IA.",
    backstory="Você é especialista em transformar informações complexas em resumos claros e objetivos.",
    verbose=True,
    allow_delegation=False,
    llm=GROQ_MODEL
)

#= Definição das tarefas 
tarefa_pesquisa = Task(
    description="Pesquise e colete as 5 principais notícias recentes sobre IA e ML. "
                "Para cada notícia, forneça:\n"
                "- Título\n- Fonte\n- Data\n- URL\n- Resumo (2-3 frases)",
    expected_output="Lista organizada com 5 notícias de IA e ML.",
    agent=pesquisador
)

tarefa_resumo = Task(
    description="Crie um resumo único e coeso a partir das 5 notícias coletadas. "
                "O texto deve ter no máximo 2 parágrafos, em linguagem clara e objetiva.",
    expected_output="Resumo final em até 2 parágrafos sobre IA na semana.",
    agent=resumidor
)

#  Crew 
crew = Crew(
    agents=[pesquisador, resumidor],
    tasks=[tarefa_pesquisa, tarefa_resumo],
    verbose=True
)

# Execução
print("\nIniciando geração do resumo semanal de IA...\n")
resultado = crew.kickoff()

print("\n" + "="*60)
print("RESUMO FINAL GERADO PELO SISTEMA")
print("="*60)
print(resultado)
