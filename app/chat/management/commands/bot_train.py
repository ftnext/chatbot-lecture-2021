from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.ext.django_chatterbot.models import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Train chatbot with corpus"

    def handle(self, *args, **kwargs):
        statements = Statement.objects.all()
        if statements:
            statements.delete()
            self.stdout.write(
                self.style.SUCCESS("All data have been deleted.")
            )

        chatbot = ChatBot(**settings.CHATTERBOT)

        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.japanese")

        self.stdout.write(self.style.SUCCESS("Training completed."))
