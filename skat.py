import aisisax.object_detection.lsa_interface as aisax_object_detection
import aisisax.llm.openai_connector as aisax_openai
import aisisax.llm.ollama_connector as aisax_ollama

messages = []
f = open('prompts/system.skat3')
system_prompt = "".join(f.readlines())
model = 'gpt-4o'
#model = 'gpt-3.5-turbo'
#model = 'o1-preview'
temp = 0.0

test_case = """
Let's suppose these are the three suits:

P1: [jack-hearts, jack-clubs, ace-diamonds, 10diamonds, 9diamonds, ace-hearts, 10hearts, 8hearts, 7hearts, queen-spades]

P2: [jack-spades, queen-hearts, king-hearts, king-diamonds, queen-diamonds, 8diamonds, 7diamonds, ace-clubs, 10clubs, 9clubs]

P3: [jack-diamonds, king-clubs, queen-clubs, 8clubs, 7clubs, ace-spades, king-spades, 10spades, 9spades, 8spades]

We're pre-bidding -- what's in the Skat?

"""

result = aisax_openai.generate_answer(test_case, temperature=temp, model=model, system_prompt=system_prompt)
messages.append({'role': 'user', 'content': test_case})
messages.append({'role': 'assistant', 'content': result})
print(result)
print("Expected: 9hearts, 7spades")

#while True:
#    myinput = input("> ")
#    if myinput.strip() in ('exit', 'quit'):
#        break
#    result = aisax_openai.generate_answer(myinput, messages=messages,
#                                          temperature=temp, model=model, system_prompt=system_prompt)
#    messages.append({'role': 'user', 'content': myinput})
#    messages.append({'role': 'assistant', 'content': result})
#
#    print(result)
