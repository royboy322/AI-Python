"""Homework 2 - Eliza, The Simple Therapist"""

__author__ = "Michael Roy"

import re
import random

def extract_name(input_text):
    name_patterns = [
        re.compile(r'my name is (\w+)', re.IGNORECASE),
        re.compile(r'I am (\w+)', re.IGNORECASE),
        re.compile(r'(\w+) is my name', re.IGNORECASE),
        re.compile(r'my name is (\w+) is my name', re.IGNORECASE)
    ]

    for pattern in name_patterns:
        match = pattern.search(input_text)
        if match:
            return match.group(1)

    return None

def main():
    print("Hello! I'm Eliza, and I will be your therapist today. What is your name?")
    user_name = input()
    print("Hello " + user_name + "! How are you feeling today?")

    while True:
        user_input = input()
        name = extract_name(user_input)
        if name:
            user_name = name
            print("Hello " + user_name + "! How are you feeling today?")
            continue

        response = eliza_response(user_input)
        print(response)

        if response.lower() == "Goodbye! Take care and have a wonderful rest of your day.".lower():
            break

def remove_ed(verb):
    return re.sub('ed$', '', verb)

def eliza_response(user_input):
    response = ""

    if user_input.lower() == "bye":
        response = "Goodbye! Take care and have a wonderful rest of your day."
        return response

    if 'you' in user_input.lower().split():
        response = "We were discussing you, not me."

    feelings = re.findall(r'\b(joy|joyful|joyfulness|ok|okay|good|bad|well|sad|happy|saddened)\b', user_input.lower())
    if feelings:
        response += random.choice(feeling_responses[feelings[0]]) + " "

    verbs = re.findall(r'\b(\w+ed)\b', user_input.lower())
    if verbs:
        response += "Why did it " + remove_ed(verbs[0]) + "? "

    relationships = re.findall(r'\b(mother|mom|father|dad|brother|sister|friend)\b', user_input.lower())
    if relationships:
        response += random.choice(relationship_responses[relationships[0]])

    if not response:
        response = "Tell me more about that."

    return response

feeling_responses = {
    'joy': ["It's great to be joyful! What's bringing you joy today?"],
    'joyful': ["Embrace the joy! What's making you feel joyful?"],
    'joyfulness': ["Feeling joyful is wonderful! What's bringing you this joy?"],
    'ok': ["It's alright to feel just okay. Is there anything on your mind that you'd like to share?"],
    'okay': ["It's alright to feel just okay. Is there anything on your mind that you'd like to share?"],
    'good': ["I'm glad to hear that you're feeling good. What's been going well for you?"],
    'bad': ["I'm sorry to hear that you're feeling bad. Is there something specific bothering you?"],
    'well': ["That's good to hear. Is there anything else you'd like to share?"],
    'sad': ["I'm sorry to hear that. Would you like to talk about why you're feeling sad?"],
    'happy': ["Happiness is wonderful! What's making you feel happy?"],
    'saddened': ["I'm here to listen. Would you like to share why you're feeling saddened?"]
}

relationship_responses = {
    'mother': ["Tell me more about your relationship with your mother."],
    'mom': ["What's your relationship like with your mom?"],
    'father': ["How do you feel about your relationship with your father?"],
    'dad': ["What's your relationship with your dad like?"],
    'brother': ["What's your relationship with your brother like?"],
    'sister': ["Tell me more about your relationship with your sister."],
    'friend': ["Friends are important. How do you feel about your friend?"]
}

if __name__ == "__main__":
    main()


