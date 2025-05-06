from django.core.management.base import BaseCommand
import csv
import pathlib
import uuid
import datetime
from una_health_app.models import User,GlucoseTableLvels

class Command(BaseCommand):
    help="generate data to test the code"
    def handle(self, *args, **options):
        path = pathlib.Path(__file__).parent.parent.parent.parent
        data_folder = path / "sample-data"
        for file in list(data_folder.iterdir()):
            if file.suffix == ".csv":
                User.objects.create(user_id=file.name.split(".")[0],name=file.name.split(".")[0][:7])