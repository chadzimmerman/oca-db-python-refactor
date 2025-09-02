from django.db import models

# --------------------
# Exceptions
# --------------------
class Xception(models.Model):
    xc_id = models.IntegerField(primary_key=True)
    xc_year = models.IntegerField()
    xc_month = models.IntegerField()
    xc_day = models.IntegerField()
    xc_new_month = models.IntegerField()
    xc_new_day = models.IntegerField()
    xc_note = models.TextField()
    xc_flag = models.IntegerField()

    def __str__(self):
        return f"Exception {self.xc_year}-{self.xc_month}-{self.xc_day}"