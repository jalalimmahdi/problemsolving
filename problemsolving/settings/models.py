from django.db import models

# Create your models here.
class metadata1(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
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

    def __str__(self):
        return self.type + " - " + self.title
