# # src/insight_generator.py

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from .zodiac_utils import get_zodiac


load_dotenv()


HOROSCOPE_PROMPT = PromptTemplate(
    input_variables=["name", "birth_date", "birth_time", "birth_place"],
    template=(
        """You are an Professional astrologer generating a personalized horoscope for {name}, born on {birth_date}. 
        Based on the birth time of {birth_time} and the birth place of {birth_place},
        calculate the zodiac sign, ascendant, and any relevant astrological influences. 
        Then, use this information to determine the sun sign traits, moon traits, and rising sign traits for {name}. 
        Focus on the following for today: 
        - One opportunity they should take advantage of today. 
        - One challenge they may face and a way to handle it. 
        - One practical step they can take today to improve their life or align with their strengths. 
        Avoid using astrological or mystical language, and refrain from using any zodiac-related terms
    Keep the response under 3 sentences, and make sure it is uplifting and helpful.
    Start the response with a warm and friendly greeting like: "Hello {name}!, Today:"""
    )
   
)

def generate_insight(name: str, birth_date: str, birth_time: str, birth_place: str) -> dict:
    """
    Generate horoscope insight based on name, birth date, time, and place.

    Args:
        name: Person's name (for personalization)
        birth_date: Birth date (YYYY-MM-DD)
        birth_time: Birth time (HH:MM)
        birth_place: Birth place (City, Country)

    Returns:
        dict: Horoscope insight and associated details.
    """
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",  
        temperature=0.7  
    )

    sequence = HOROSCOPE_PROMPT | llm

    # input data for the LLM
    input_data = {
        "name": name,
        "birth_date": birth_date,
        "birth_time": birth_time,
        "birth_place": birth_place,
    }

    
    raw_text = sequence.invoke(input=input_data)

    clean_text = raw_text.content.strip()

    return {
        "zodiac": get_zodiac(birth_date), 
        "insight": clean_text,
        "language": "en"
    }

#CLI test 
# if __name__ == "__main__":
#     print(generate_insight(
#         name="Gaurav",
#         birth_date="1999-09-05",
#         birth_time="12:05",
#         birth_place="Dhar, India"
#     ))
