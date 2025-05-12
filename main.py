# import sys
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.reasoning import ReasoningTools


class CoverLetterAgent:
    def __init__(self, language: str = "en"):
        self.language = language
        self.instructions = self._get_instructions()
        self.agent = self._initialize_agent()

    def _get_instructions(self) -> list:
        # Retourne les instructions à donner à l'agent selon la langue (FR/EN) sélectionnée.
        """Returns instructions based on selected language."""
        instructions = {
            "en": [
                "You are a professional cover letter writing assistant.",
                "Break down the writing process into clear steps using reflection.",
                "Consider the job description, candidate qualifications, and company culture.",
                "Write in a professional yet engaging and natural tone, showcasing personality.",
                "Focus on specific achievements, relevant experience, and soft skills.",
                "Ensure the final output is well-structured and properly formatted.",
            ],
            "fr": [
                "Tu es un assistant professionnel spécialisé dans la rédaction de lettres de motivation."
                "Décompose le processus de rédaction en étapes claires en y intégrant une réflexion approfondie."
                "Tiens compte de la description du poste, des qualifications du candidat et de la culture de l'entreprise."
                "Adopte un ton professionnel tout en restant engageant et naturel, montrant ainsi une certaine personnalité."
                "Mets l'accent sur les réalisations, les expériences pertinentes, et les soft skills."
                "Assure-toi que le résultat final soit bien structuré et correctement mis en forme.",
            ],
        }
        return instructions.get(self.language, instructions["en"])

    def _initialize_agent(self) -> Agent:
        # Initilisation de l'Agent.
        """Initializes the Agno agent with appropriate configuration."""
        return Agent(
            # model=Groq(id="llama-3.3-70b-versatile"),
            model=Groq(id="meta-llama/llama-4-maverick-17b-128e-instruct"),
            tools=[ReasoningTools(add_instructions=True)],
            instructions=self.instructions,
            markdown=True,
            show_tool_calls=True,
            # show_tool_calls=False,
        )

    def generate_cover_letter(
        # Fonction qui génère la lettre de motivation.
        self,
        prompt: str,
        stream: bool = True,
        show_reasoning: bool = True,
        stream_steps: bool = True,
    ) -> None:
        """
        Generates a cover letter based on the provided prompt.

        Args:
            prompt (str): The user's prompt containing job details and qualifications
            stream (bool): Whether to stream the response or not
            show_reasoning (bool): Whether to show the agent's reasoning process or not
            stream_steps (bool): Whether to stream intermediate steps or not
        """
        self.agent.print_response(
            prompt,
            stream=stream,
            show_full_reasoning=show_reasoning,
            stream_intermediate_steps=stream_steps,
        )


def main():
    agent = CoverLetterAgent(language="fr")  # ou "en" pour l'anglais

    name = "IxyzC"
    prompt = f"""
    Je m'appelle {name}. J'ai découvert la data science en 2020 et continue à l'étudier depuis, avec notamment un double master dans le domaine. Aide-moi à écrire une lettre de motivation de taille moyenne pour un poste de data scientist chez WorkForUs, en mettant en avant mes 5 ans d'expérience en Python et SQL, ainsi que mes projets d'intelligence artificielle, qui vont de l'analyse de données à la création de modèles prédictifs grâce au machine & deep learning, data mining, en passant par la création d'agents conversationnels et d'outils de génération de texte. Les chargés de recrutement sont Mr. LeMonsieur et Mme. LaMadame.

    La description du poste, en anglais, est la suivante :
    - Master's degree in Statistics, Economics, Engineering, Mathematics, a related quantitative field, or equivalent practical experience.
    - 3 years of experience with statistical data analysis, data mining, and querying (e.g. SQL).
    - 3 years of experience managing analytical projects.
    
    Mon compte GitHhub se trouve à l'adresse suivante : https://github.com/github.
    Je suis joignable par mail à l'adresse gmail@gmail.com, et par téléphone au 06 12 34 56 78.
    """

    agent.generate_cover_letter(prompt)


# print("Python executable:", sys.executable)
load_dotenv()
print("\n> uv run main.py\n")

if __name__ == "__main__":
    main()
