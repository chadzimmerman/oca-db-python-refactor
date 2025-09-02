from django.db import models

# --------------------
# Icons
# --------------------
class Icon(models.Model):
    icon_id = models.IntegerField(primary_key=True)
    icon_category = models.IntegerField()
    icon_month = models.IntegerField()
    icon_day = models.IntegerField()
    icon_dday = models.CharField(max_length=50, blank=True, null=True)
    icon_idx = models.IntegerField()
    icon_sid = models.IntegerField()
    icon_name = models.CharField(max_length=200)
    icon_icon = models.CharField(max_length=200, blank=True, null=True)
    icon_flag = models.IntegerField()

    def __str__(self):
        return self.icon_name