from datetime import date

from django.db import models

from organization.models import Employee


class Case(models.Model):
    number = models.SmallIntegerField(unique=True, blank=True)
    start_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.start_date.isoformat()}-{self.number}"


class Task(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
