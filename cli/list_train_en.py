from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello.",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear.",
    "Thank you.",
    "You're welcome.",
]

if __name__ == "__main__":
    chatbot = ChatBot("Training with list bot")

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    while True:
        try:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
