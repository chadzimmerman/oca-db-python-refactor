from django.db import models

class Scripture(models.Model):
    #title or type of reading (i.e., "Gospel", "Epistle")
    title = models.CharField(max_length=100)

    #Full text
    text = models.TextField()

    #Opt fields to connect dates
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.month}/{self.day})"
