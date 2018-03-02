# dst_django
django app to query Dst index

To import the data in the database using csv file:
```
python manage.py shell
>> import csv
>> from data.models import Data
>> with open('25.csv') as f:
      reader = csv.DictReader(f)
      for row in reader:
          q = Data(date=row['DATE'],time=row['TIME'],doy=row['DOY'],dst=int(float(row['DST'])))
          q.save()
