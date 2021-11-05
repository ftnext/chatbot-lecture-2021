from pathlib import Path

from chatterbot import ChatBot
from chatterbot.languages import JPN
from chatterbot.trainers import ChatterBotCorpusTrainer


class CustomJPN(JPN):
    ISO_639_1 = "ja_core_news_sm"


if __name__ == "__main__":
    cli_dir_path = Path(__file__).resolve().parent
    data_yml_path = cli_dir_path / "greetings_ja.yml"

    chatbot = ChatBot(
        "Training from yaml bot", database_uri=None, tagger_language=CustomJPN
    )

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(str(data_yml_path))

    while True:
        try:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
