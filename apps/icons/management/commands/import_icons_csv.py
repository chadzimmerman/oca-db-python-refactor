import csv
from django.core.management.base import BaseCommand
from apps.icons.models import Icon

class Command(BaseCommand):
    help = 'Import icons.csv into Icon model'

    def handle(self, *args, **options):
        with open('data/tables/icons.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Remove BOM if present
            reader.fieldnames = [f.strip().lstrip('\ufeff') for f in reader.fieldnames]

            for row in reader:
                Icon.objects.update_or_create(
                    icon_id=row['iconId'],  # primary key field in model
                    defaults={
                        'icon_category': row['iconCategory'],
                        'icon_month': row['iconMonth'],
                        'icon_day': row['iconDay'],
                        'icon_dday': row['iconDday'],
                        'icon_idx': row['iconIdx'],
                        'icon_sid': row['iconSid'],
                        'icon_name': row['iconName'],
                        'icon_icon': row['iconIcon'],
                        'icon_flag': row['iconFlag'],
                    }
                )

        self.stdout.write(self.style.SUCCESS('Icons CSV imported successfully.'))
