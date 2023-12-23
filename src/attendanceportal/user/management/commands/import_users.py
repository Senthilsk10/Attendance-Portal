from django.core.management.base import BaseCommand
import pandas as pd
from user.models import User  # Replace 'yourapp' with the actual name of your Django app
import logging
class Command(BaseCommand):
    help = "Seed data from CSV files"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            df = pd.read_csv(file_path) 
            for index,row in df.iterrows():
                roll = row['RollNumber']
                password = str(row['RollNumber'])
                name = row['Name']
                sem = row['sem']
                dept = row['dept']
                user = User.objects.create_user(username=name, password=password, dept=dept, sem=sem, userid=roll)
                print(roll,name,sem,dept)
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            logging.error(f'Error importing data: {str(e)}')
            self.stdout.write(self.style.ERROR(f'Error importing data: {str(e)}'))
