import csv
from django.shortcuts import render
from datetime import date

def daily_reading(request):
    readings = []
    with open('data/tables/scriptures.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            readings.append(row)
    
    # For POC, picks a reading based on day of year
    today = date.today().timetuple().tm_yday
    reading = readings[today % len(readings)]  # simple example

    return render(request, 'readings/daily.html', {'reading': reading})

