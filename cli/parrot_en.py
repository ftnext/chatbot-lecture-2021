from chatterbot import ChatBot

if __name__ == "__main__":
    chatbot = ChatBot("Parrot bot", database_uri=None)

    while True:
        try:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
