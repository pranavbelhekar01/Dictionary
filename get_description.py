from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from templates import system_prompt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_GEN_API_KEY")
# model
llm = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def get_meaning(query: str):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            ("human", "{query}"),
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "query": query,
        }
    )
    return response


# if __name__ == "__main__":
#     query = ''
#     while query != 'exit' or query != 'Exit':
#         query = input('Enter your Query: ')
#         response = get_meaning(query)
#         print("Reponse:: ", response)
#         print("-----------")