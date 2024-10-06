import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI


def main():
    load_dotenv()

    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    chain = prompt | llm

    response = chain.invoke("colorful socks")
    print(response)


if __name__ == "__main__":
    main()
