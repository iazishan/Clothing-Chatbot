import json, random

with open('data/responses.json') as file:
    responses = json.load(file)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return random.choice(responses["greetings"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["farewell"])
    elif "trend" in user_input or "trending" in user_input:
        return random.choice(responses["trending"])
    elif "recommend" in user_input or "suggest" in user_input:
        return random.choice(responses["recommendations"])
    elif "what should i wear" in user_input:
        return random.choice(responses["personal"])
    else:
        return "Tell me what you're looking for — casual, party, formal or trending outfits?" 
