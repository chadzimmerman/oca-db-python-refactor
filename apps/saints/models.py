from django.db import models

# --------------------
# Lives of the Saints
# --------------------
class Life(models.Model):
    lives_id = models.IntegerField(primary_key=True)
    lives_sid = models.IntegerField()
    lives_name = models.CharField(max_length=200)
    lives_text = models.TextField()
    lives_flag = models.IntegerField()

    def __str__(self):
        return self.lives_name

# --------------------
# Menaion
# --------------------
class Menaion(models.Model):
    mn_id = models.IntegerField(primary_key=True)
    mn_month = models.IntegerField()
    mn_day = models.IntegerField()
    mn_sid = models.IntegerField()
    mn_name = models.CharField(max_length=200)
    mn_alpha = models.CharField(max_length=50, blank=True, null=True)
    mn_fname = models.CharField(max_length=200, blank=True, null=True)
    mn_gender = models.CharField(max_length=50, blank=True, null=True)
    mn_date = models.CharField(max_length=50, blank=True, null=True)
    mn_loc = models.CharField(max_length=200, blank=True, null=True)
    mn_disp = models.CharField(max_length=50, blank=True, null=True)
    mn_flevel = models.IntegerField()
    mn_fast = models.IntegerField()
    mn_collect = models.IntegerField()
    mn_indiv = models.IntegerField()
    mn_icon = models.CharField(max_length=200, blank=True, null=True)
    mn_flag = models.IntegerField()
    mn_sermon_url = models.CharField(max_length=200, blank=True, null=True)
    mn_sort = models.IntegerField()

    def __str__(self):
        return self.mn_name