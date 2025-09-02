# apps/readings/management/commands/import_pericopes_csv.py
import csv
from django.core.management.base import BaseCommand
from apps.readings.models import Pericope

class Command(BaseCommand):
    help = 'Import pericopes.csv into Pericope model'

    def handle(self, *args, **options):
        with open('data/tables/pericopes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Pericope.objects.update_or_create(
                    pe_id=row['peId'],
                    defaults={
                        'pe_month': row['peMonth'],
                        'pe_day': row['peDay'],
                        'pe_pday': row['pePday'],
                        'pe_type': row['peType'],
                        'pe_desc': row['peDesc'],
                        'pe_reading': row['peReading'],
                        'pe_display': row['peDisplay'],
                        'pe_index': row['peIndex'],
                        'pe_flag': row['peFlag'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Pericopes CSV imported successfully.'))
