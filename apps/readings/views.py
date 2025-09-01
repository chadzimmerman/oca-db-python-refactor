import csv
from django.shortcuts import render
from datetime import date
from apps.readings.models import Scripture

# Loads the mapping of scrabbers
BOOK_FULL_NAMES = {}
with open('data/tables/scrabbrs.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        BOOK_FULL_NAMES[row['scriptureAbbr']] = row['scriptureBook']

def daily_reading(request):
    # For POC, picks a reading based on day of year
    today = date.today().timetuple().tm_yday
    scripture = Scripture.objects.all()[today % Scripture.objects.count()]
    
    #Attaches the full book name
    scripture.full_book_name = BOOK_FULL_NAMES.get(scripture.scripture_book, scripture.scripture_book)

    return render(request, 'readings/daily.html', {'reading': scripture})