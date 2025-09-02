# apps/tropars/management/commands/import_tropars_csv.py
import csv
from django.core.management.base import BaseCommand
from apps.tropars.models import Tropar 

class Command(BaseCommand):
    help = 'Import tropars.csv into Tropar model'

    def handle(self, *args, **options):
        with open('data/tables/tropars.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Tropar.objects.update_or_create(
                    tr_id=row['trId'],  # primary key field in model
                    defaults={
                        'tr_tid': row['trTid'],
                        'tr_sid': row['trSid'],
                        'tr_type': row['trType'],
                        'tr_tone': row['trTone'],
                        'tr_text': row['trText'],
                        'tr_flag': row['trFlag'],
                    }
                )

        self.stdout.write(self.style.SUCCESS('Tropars CSV imported successfully.'))
