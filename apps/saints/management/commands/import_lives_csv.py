import csv
from django.core.management.base import BaseCommand
from apps.saints.models import Life

class Command(BaseCommand):
    help = 'Import lives.csv into Life model'

    def handle(self, *args, **options):
        with open('data/tables/lives.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Life.objects.update_or_create(
                    lives_id=row['livesId'],
                    defaults={
                        'lives_sid': row['livesSid'],
                        'lives_name': row['livesName'],
                        'lives_text': row['livesText'],
                        'lives_flag': row['livesFlag'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Lives CSV imported successfully.'))
