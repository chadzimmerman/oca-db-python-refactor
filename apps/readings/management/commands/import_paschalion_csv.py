# apps/readings/management/commands/import_paschalion_csv.py
import csv
from django.core.management.base import BaseCommand
from apps.readings.models import Paschalion

class Command(BaseCommand):
    help = 'Import paschalion.csv into Paschalion model'

    def handle(self, *args, **options):
        with open('data/tables/paschalion.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Paschalion.objects.update_or_create(
                    ps_id=row['psId'],
                    defaults={
                        'ps_idx': row['psIdx'],
                        'ps_sid': row['psSid'],
                        'ps_text': row['psText'],
                        'ps_ctext': row['psCtext'],
                        'ps_fname': row['psFname'],
                        'ps_flevel': row['psFlevel'],
                        'ps_fast': row['psFast'],
                        'ps_icon': row['psIcon'],
                        'ps_flag': row['psFlag'],
                        'ps_sermon_url': row['psSermonURL'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Paschalion CSV imported successfully.'))
