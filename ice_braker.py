import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__ == "__main__":
    load_dotenv()
    print("I'm the main program")

    information = """
    Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world, with an estimated net worth of US$213 billion as of February 2024, according to the Bloomberg Billionaires Index, and $210 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX"""

    summary_template = """
    given the information {information} about a person I want to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["information"]
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain  =LLMChain(llm = llm, prompt = summary_prompt_template)
    res = chain.invoke(input={"information": information})
    print(res["text"])