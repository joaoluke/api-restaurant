from django.db import models

from django.db import models

class Plate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=18)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
