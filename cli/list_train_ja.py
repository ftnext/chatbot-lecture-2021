from chatterbot import ChatBot
from chatterbot.languages import JPN
from chatterbot.trainers import ListTrainer

conversation = [
    "こんにちは",
    "どうも！",
    "調子はどうですか？",
    "順調です",
    "それはよかったですね。",
    "ありがとうございます",
    "どういたしまして",
]


class CustomJPN(JPN):
    ISO_639_1 = "ja_core_news_sm"


if __name__ == "__main__":
    chatbot = ChatBot("Training with list bot", tagger_language=CustomJPN)

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    while True:
        try:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
