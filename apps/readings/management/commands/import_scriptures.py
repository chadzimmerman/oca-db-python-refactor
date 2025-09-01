# apps/readings/management/commands/import_scriptures.py
import csv
from django.core.management.base import BaseCommand
from apps.readings.models import Scripture

class Command(BaseCommand):
    help = "Import scriptures from scriptures.csv"

    def handle(self, *args, **options):
        with open('data/tables/scriptures.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Scripture.objects.update_or_create(
                    scripture_id=int(row['scriptureId']),
                    defaults={
                        'scripture_index': int(row['scriptureIndex']),
                        'scripture_testament': int(row['scriptureTestament']),
                        'scripture_book': row['scriptureBook'],
                        'scripture_verse': int(row['scriptureVerse']),
                        'scripture_text': row['scriptureText'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Scriptures imported successfully.'))