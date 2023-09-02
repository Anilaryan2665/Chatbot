import random

responses = {
    "hi" :["Hello"],
    "hello": ["Hello!", "Hey!"],
    "how are you?": [ "I'm doing well, thank you! what about you?"],
    "fine":["Good"],
    "what is your name": ["I'm just a chatbot."],
    "What is your name?": ["I am just a chatbot"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "good morning" : ["Very good morning!"],
    "good night" : ["Good Night, have a nice dreams"],


}

def get_response(message):
    message = message.lower()
    
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    
    return "Sorry, Please type correctly."

print("Chatbot: Hello! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
