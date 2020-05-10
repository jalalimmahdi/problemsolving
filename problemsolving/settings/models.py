from django.db import models

# Create your models here.
class metadata1(models.Model):
    title=models.CharField(max_length=255)
    types_list=(
        ('pt','broblem type'),
        ('ft','finding type'),
        ('ps','problem status'),
        ('ss','solution status')
    )
    type=models.CharField(
        max_length=2,
        choices=types_list,
        default="pt"
    )
    description=models.TextField(blank=True)

    def __str__(self):
        return self.type + " - " + self.title


class metadataN(models.Model):
    title=models.CharField(max_length=255)
    types_list=(
        ('gr','subject group'),
        ('pl','place'),
        ('un','company unit'),
        ('pr','process'),
        ('go','goal')
    )
    type=models.CharField(
        max_length=2,
        choices=types_list,
        default="gr"
    )
    description=models.TextField(blank=True)
    json=models.TextField(blank=True)

    def __str__(self):
        return self.type + " - " + self.title
