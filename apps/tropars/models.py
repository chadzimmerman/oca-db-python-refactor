from django.db import models

# --------------------
# Tropars
# --------------------
class Tropar(models.Model):
    tr_id = models.IntegerField(primary_key=True)
    tr_tid = models.IntegerField()
    tr_sid = models.IntegerField()
    tr_type = models.IntegerField()
    tr_tone = models.IntegerField()
    tr_text = models.TextField()
    tr_flag = models.IntegerField()

    def __str__(self):
        return f"Tropar {self.tr_id}"