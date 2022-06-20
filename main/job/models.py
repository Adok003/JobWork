from django.db import models


POSITIONS = [
    ('director', 'director'),
    ('senior', 'senior'),
    ('middle', 'middle'),
    ('junior', 'junior'),
    ('ordinary', 'ordinary')
]


class Employees(models.Model):
    manager_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=100)
    position = models.CharField(choices=POSITIONS, max_length=50)
    hire_date = models.DateField()
    salary = models.IntegerField()

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.full_name
