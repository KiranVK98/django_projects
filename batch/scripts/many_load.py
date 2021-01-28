import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('/home/kiranvk98/django_projects/batch/unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()
    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        n=row[0]
        d=row[1]
        j=row[2]
        y=row[3]
        long=row[4]
        lat=row[5]
        a=row[6]
        c, created = Category.objects.get_or_create(name=row[7])
        c.save()
        s, created = State.objects.get_or_create(name=row[8])
        s.save()
        r, created = Region.objects.get_or_create(name=row[9])
        r.save()
        i, created = Iso.objects.get_or_create(name=row[10])
        i.save()

        try:
            y = int(row[3])
        except:
            y = None

        try:
            long = int(row[4])
        except:
            long = None

        try:
            lat = int(row[5])
        except:
            lat = None

        try:
            a = int(row[6])
        except:
            a = None

        k = Site(name=n, description=d, justification=j, year=y, longitude=long, latitude=lat, area_hectares=a, category=c, states=s, region=r, iso=i)
        k.save()