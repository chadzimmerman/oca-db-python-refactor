from django.db import models

# --------------------
# Scripture
# --------------------
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
    
# --------------------
# Paschalion
# --------------------
class Paschalion(models.Model):
    ps_id = models.IntegerField(primary_key=True)
    ps_idx = models.IntegerField()
    ps_sid = models.IntegerField()
    ps_text = models.CharField(max_length=200, blank=True, null=True)
    ps_ctext = models.CharField(max_length=200, blank=True, null=True)
    ps_fname = models.CharField(max_length=200, blank=True, null=True)
    ps_flevel = models.IntegerField()
    ps_fast = models.IntegerField()
    ps_icon = models.CharField(max_length=200, blank=True, null=True)
    ps_flag = models.IntegerField()
    ps_sermon_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.ps_text or f"Paschalion {self.ps_id}"

# --------------------
# Pericopes
# --------------------
class Pericope(models.Model):
    pe_id = models.IntegerField(primary_key=True)
    pe_month = models.IntegerField()
    pe_day = models.IntegerField()
    pe_pday = models.IntegerField()
    pe_type = models.CharField(max_length=50)
    pe_desc = models.TextField(blank=True, null=True)
    pe_reading = models.CharField(max_length=50)
    pe_display = models.CharField(max_length=200)
    pe_index = models.IntegerField()
    pe_flag = models.IntegerField()

    def __str__(self):
        return f"{self.pe_type}: {self.pe_display}"
