from django.db import models

class Scripture(models.Model):
    scripture_id = models.IntegerField(unique=True)  # matches scriptureId in scriptures.csv
    scripture_index = models.IntegerField()          # matches scriptureIndex
    scripture_testament = models.IntegerField()      # 0=OT, 1=NT? adjust as needed
    scripture_book = models.CharField(max_length=50) # e.g., "Matt"
    scripture_verse = models.IntegerField()         # e.g., 1001
    scripture_text = models.TextField()             # the verse text

    @property
    def chapter_and_verse(self):
        chapter = self.scripture_verse // 1000   # integer division: 9010 // 1000 = 9
        verse = self.scripture_verse % 1000      # remainder: 9010 % 1000 = 10
        return f"{chapter}:{verse}"

    def __str__(self):
        return f"{self.full_book_name} {self.chapter_and_verse}: {self.scripture_text}..."
