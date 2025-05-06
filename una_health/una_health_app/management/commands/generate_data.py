from una_health_app.models import User,GlucoseTableLvels
from django.core.management.base import BaseCommand
import csv
import pathlib
import uuid
import datetime

class Command(BaseCommand):
    help="generate data to test the code"
    def handle(self, *args, **options):
        path = pathlib.Path(__file__).parent.parent.parent.parent
        data_folder = path / "sample-data"
        for file in list(data_folder.iterdir()):
            if file.suffix == ".csv":
                with open(file,mode="r",newline="") as f:
                    next(f)
                    next(f)
                    reader = csv.DictReader(f)
                    for row in reader:
                        GlucoseTableLvels.objects.create(
                            device = row["Gerät"],
                            serial_number = uuid.UUID(row["Seriennummer"]),
                            user = User.objects.get(user_id=file.name.split(".")[0]),
                            device_time_stamp=datetime.datetime.strptime(row['Gerätezeitstempel'], '%d-%m-%Y %H:%M'),
                            record_type = row["Aufzeichnungstyp"],
                            glucose_history = 0 if not row["Glukosewert-Verlauf mg/dL"] else row["Glukosewert-Verlauf mg/dL"],
                            glucose_scan = 0 if row.get("Glukose-Scan mg/dL") =="" else row.get("Glukose-Scan mg/dL") ,
                            non_numeric_rapid_acting_insulin = row["Nicht numerisches schnellwirkendes Insulin"],
                            rapid_acting_insulin = 0 if row["Schnellwirkendes Insulin (Einheiten)"]== "" else row["Schnellwirkendes Insulin (Einheiten)"],
                            food_data = row["Nicht numerische Nahrungsdaten"],
                            carbohydrates = 0 if row["Kohlenhydrate (Gramm)"] == "" else row["Kohlenhydrate (Gramm)"],
                            carbohydrates_servings = row["Kohlenhydrate (Portionen)"],
                            non_numeric_extended_release_insulin = row["Nicht numerisches Depotinsulin"],
                            extended_release_insulin = 0 if not row["Depotinsulin (Einheiten)"] else row["Depotinsulin (Einheiten)"] ,
                            notes = row["Notizen"],
                            glucose_test_strip = 0 if not row["Glukose-Teststreifen mg/dL"] else row["Glukose-Teststreifen mg/dL"],
                            ketone = 0 if not row["Keton mmol/L"] else  row["Keton mmol/L"],
                            mealtime_insuline = 0 if not row["Mahlzeiteninsulin (Einheiten)"] else  row["Mahlzeiteninsulin (Einheiten)"] ,
                            correction_insuline =0 if not row["Korrekturinsulin (Einheiten)"] else row["Korrekturinsulin (Einheiten)"] ,
                            user_change_insulin = 0 if not row["Insulin-Änderung durch Anwender (Einheiten)"] else row["Insulin-Änderung durch Anwender (Einheiten)"]
                            )     



        