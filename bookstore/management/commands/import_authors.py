from django.core.management.base import BaseCommand
from bookstore.models import Author
import csv


class Command(BaseCommand):
	help = 'create authors from a csv file'

	def add_arguments(self, parser):
		parser.add_argument('csv_path', type=str)

	def handle(self, *args, **options):
		csv_path = options['csv_path']

		with open(csv_path, mode='r', encoding='utf-8') as csv_authors:
			authors_reader = csv.reader(csv_authors)
			next(authors_reader, None) #skip header

			self.stdout.write('importing authors from csv file...')

			for name in authors_reader:
				try:
					new_author = Author(name=name[0])
					new_author.save()
				except Exception as e:
					self.stdout.write(f'author: {name[0][:20]:20} - error: {e}')

			self.stdout.write('\n')
			self.stdout.write('imported authors!')