# apps/saints/management/commands/import_menaion_csv.py
import csv
from django.core.management.base import BaseCommand
from apps.saints.models import Menaion

class Command(BaseCommand):
    help = 'Import menaion.csv into Menaion model'

    def handle(self, *args, **options):
        with open('data/tables/menaion.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Menaion.objects.update_or_create(
                    mn_id=row['mnId'],
                    defaults={
                        'mn_month': row['mnMonth'],
                        'mn_day': row['mnDay'],
                        'mn_sid': row['mnSid'],
                        'mn_name': row['mnName'],
                        'mn_alpha': row['mnAlpha'],
                        'mn_fname': row['mnFname'],
                        'mn_gender': row['mnGender'],
                        'mn_date': row['mnDate'],
                        'mn_loc': row['mnLoc'],
                        'mn_disp': row['mnDisp'],
                        'mn_flevel': row['mnFlevel'],
                        'mn_fast': row['mnFast'],
                        'mn_collect': row['mnCollect'],
                        'mn_indiv': row['mnIndiv'],
                        'mn_icon': row['mnIcon'],
                        'mn_flag': row['mnFlag'],
                        'mn_sermon_url': row['mnSermonURL'],
                        'mn_sort': row['mnSort'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Menaion CSV imported successfully.'))
