from django.db import models


# Create your models here.
class Reports(models.Model):
    title = models.CharField(max_length=240)

    def __str__(self):
        return self.title


class Item(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

