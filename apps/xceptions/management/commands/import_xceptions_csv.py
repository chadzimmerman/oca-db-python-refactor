# apps/xceptions/management/commands/import_xceptions_csv.py
import csv
from django.core.management.base import BaseCommand
from apps.xceptions.models import Xception  # Adjust if your app path differs

class Command(BaseCommand):
    help = 'Import xceptions.csv into Xception model'

    def handle(self, *args, **options):
        with open('data/tables/xceptions.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Xception.objects.update_or_create(
                    xc_id=row['xcId'],  # primary key field in model
                    defaults={
                        'xc_year': row['xcYear'],
                        'xc_month': row['xcMonth'],
                        'xc_day': row['xcDay'],
                        'xc_new_month': row['xcNewMonth'],
                        'xc_new_day': row['xcNewDay'],
                        'xc_note': row['xcNote'],
                        'xc_flag': row['xcFlag'],
                    }
                )

        self.stdout.write(self.style.SUCCESS('Xceptions CSV imported successfully.'))
