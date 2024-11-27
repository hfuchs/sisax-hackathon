from pydantic import BaseModel
from enum import Enum
from openai import OpenAI

client = OpenAI()


class ValidSkatCards(str, Enum):
    ace_clubs = "A♣️"
    ace_diamonds = "A♦️"
    ace_hearts = "A♥️"
    ace_spades = "A♠️"
    eight_clubs = "8♣️"
    eight_diamonds = "8♦️"
    eight_hearts = "8♥️"
    eight_spades = "8♠️"
    jack_clubs = "J♣️"
    jack_diamonds = "J♦️"
    jack_hearts = "J♥️"
    jack_spades = "J♠️"
    king_clubs = "K♣️"
    king_diamonds = "K♦️"
    king_hearts = "K♥️"
    king_spades = "K♠️"
    nine_clubs = "9♣️"
    nine_diamonds = "9♦️"
    nine_spades = "9♠️"
    queen_clubs = "Q♣️"
    queen_diamonds = "Q♦️"
    queen_hearts = "Q♥️"
    queen_spades = "Q♠️"
    seven_clubs = "7♣️"
    seven_diamonds = "7♦️"
    seven_hearts = "7♥️"
    seven_spades = "7♠️"
    ten_clubs = "10♣️"
    ten_diamonds = "10♦️"
    ten_hearts = "10♥️"
    ten_spades = "10♠️"


#
# NOTE Tightening the available values makes no difference for the one-shot
# correctness of the structured-output approach.
#
class SkatContent(BaseModel):
    skatcards: list[str]
    # skatcards: list[ValidSkatCards]


messages = []
with open("prompts/system.skat5") as f:
    system_prompt = "".join(f.readlines())

model = "gpt-4o"
# model = 'gpt-3.5-turbo'
# model = 'o1-preview'
temp = 0

test_case = """
These are the three hands and the skat:

P1: [J♥️, J♣️, A♦️, 10♦️, 9♦️, A♥️, 10♥️, 8♥️, 7♥️, Q♠️]
P2: [J♠️, K♥️, K♦️, Q♦️, Q♥️, 8♦️, 7♦️, A♣️, 10♣️, 9♣️]
P3: [J♦️, K♣️, Q♣️, 8♣️, 7♣️, A♠️, K♠️, 10♠️, 9♠️, 8♠️]

Skat: [?, ?]

You are the game master: which cards are in the Skat?  Determine the answer by
first sorting and printing all players' cards and then and comparing them to
the full 32-card set.  Do this comparison twice to avoid errors.

"""

completion = client.beta.chat.completions.parse(
    model=model,
    temperature=temp,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": test_case},
    ],
    # response_format=SkatContent,
)

answer = completion.choices[0].message.content
print(answer)

structured = completion.choices[0].message.parsed
if structured:
    print("Structured:")
    print(structured)
print("Expected: 9♥️, 7♠️")

# while True:
#    myinput = input("> ")
#    if myinput.strip() in ('exit', 'quit'):
#        break
#    result = aisax_openai.generate_answer(myinput, messages=messages,
#                                          temperature=temp, model=model, system_prompt=system_prompt)
#    messages.append({'role': 'user', 'content': myinput})
#    messages.append({'role': 'assistant', 'content': result})
#
#    print(result)
