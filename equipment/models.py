from django.db import models
from django.urls import reverse
from django.utils import timezone

# Тип оборудования
class equipmentType(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)

    # Создать новую единицу оборудования
    def create(self):
        self.date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.name

