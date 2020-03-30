import csv
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question
from .command_utils import get_csv_file


class Command(BaseCommand):
    help = "Insert questions from a CSV file. " \
           "CSV file name(s) should be passed. "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Question

    def insert_question_to_db(self, question_text):
        try:
            self.model_name.objects.create(
                question_text=question_text,
                pub_date=timezone.now()
            )
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                self.model_name, str(e)))

    def add_arguments(self, parser):
        parser.add_argument('filenames',
                            nargs='+',
                            type=str,
                            help="Inserts question from CSV file")

    def handle(self, *args, **options):
        for filename in options['filenames']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
            file_path = get_csv_file(filename)
            try:
                with open(file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        if row != "":
                            question_text = [word.strip() for word in row][0]
                            self.insert_question_to_db(question_text)
                            self.stdout.write(
                                self.style.SUCCESS('Added question: {}'.format(
                                        question_text
                                    )
                                )
                            )
            except FileNotFoundError:
                raise CommandError("File {} does not exist".format(
                    file_path))
