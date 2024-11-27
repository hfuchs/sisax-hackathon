from pydantic import BaseModel
from enum import Enum
from openai import OpenAI

client = OpenAI()

class ValidSkatCards(str, Enum):
    ace_clubs = "ace-clubs"
    ace_diamonds = "ace-diamonds"
    ace_hearts = "ace-hearts"
    ace_spades = "ace-spades"
    eight_clubs = "8-clubs"
    eight_diamonds = "8-diamonds"
    eight_hearts = "8-hearts"
    eight_spades = "8-spades"
    jack_clubs = "jack-clubs"
    jack_diamonds = "jack-diamonds"
    jack_hearts = "jack-hearts"
    jack_spades = "jack-spades"
    king_clubs = "king-clubs"
    king_diamonds = "king-diamonds"
    king_hearts = "king-hearts"
    king_spades = "king-spades"
    nine_clubs = "9-clubs"
    nine_diamonds = "9-diamonds"
    nine_spades = "9-spades"
    queen_clubs = "queen-clubs"
    queen_diamonds = "queen-diamonds"
    queen_hearts = "queen-hearts"
    queen_spades = "queen-spades"
    seven_clubs = "7-clubs"
    seven_diamonds = "7-diamonds"
    seven_hearts = "7-hearts"
    seven_spades = "7-spades"
    ten_clubs = "10-clubs"
    ten_diamonds = "10-diamonds"
    ten_hearts = "10-hearts"
    ten_spades = "10-spades"

#
# NOTE Tightening the available values makes no difference.
#
class SkatContent(BaseModel):
    skatcards: list[str]
    #skatcards: list[ValidSkatCards]


messages = []
f = open("prompts/system.skat4-structured")
system_prompt = "".join(f.readlines())
model = "gpt-4o"
# model = 'gpt-3.5-turbo'
# model = 'o1-preview'
temp = 0.1

test_case = """
These are the three hands and the skat:

P1: [jack-hearts, jack-clubs, ace-diamonds, 10-diamonds, 9-diamonds, ace-hearts, 10-hearts, 8-hearts, 7-hearts, queen-spades]
P2: [jack-spades, king-hearts, king-diamonds, queen-diamonds, queen-hearts, 8-diamonds, 7-diamonds, ace-clubs, 10-clubs, 9-clubs]
P3: [jack-diamonds, king-clubs, queen-clubs, 8-clubs, 7-clubs, ace-spades, king-spades, 10-spades, 9-spades, 8-spades]

Skat: [?, ?]

You are the game master: which cards are in the Skat?  Determine the answer by
arranging and sorting all known cards and comparing to the full 32-card set.

"""

completion = client.beta.chat.completions.parse(
    model=model,
    temperature=temp,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": test_case},
    ],
    response_format=SkatContent,
)

answer = completion.choices[0].message.content
print(answer)

structured = completion.choices[0].message.parsed
if structured:
    print("Structured:")
    print(structured)
print("Expected: 9-hearts, 7-spades")

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
