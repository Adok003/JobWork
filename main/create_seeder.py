import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'main.settings')

import django

django.setup()

import random
from job.models import Employees
from faker import Faker

fake = Faker()


def create_seeder(value):
    for i in range(value):
        manager_id = random.randint(10003, 25002)
        full_name = fake.name()
        position = 'rank_and_file'
        hire_date = fake.date_between()
        salary = random.randint(90000, 200000)
        create = Employees.objects.get_or_create(manager_id=manager_id,
                                                 full_name=full_name,
                                                 position=position,
                                                 hire_date=hire_date,
                                                 salary=salary)


def main():
    no = int(input("how many you want add employees: "))
    create_seeder(no)


if __name__ == "__main__":
    main()
