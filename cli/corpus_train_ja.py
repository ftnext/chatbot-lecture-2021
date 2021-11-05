from chatterbot import ChatBot
from chatterbot.languages import JPN
from chatterbot.trainers import ChatterBotCorpusTrainer


class CustomJPN(JPN):
    ISO_639_1 = "ja_core_news_sm"


if __name__ == "__main__":
    chatbot = ChatBot("Training from corpus bot", tagger_language=CustomJPN)

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.japanese")

    while True:
        try:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
