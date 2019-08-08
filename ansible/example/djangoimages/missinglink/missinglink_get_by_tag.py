import os, csv, datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "missinglink.settings")
import django
django.setup()

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from groundtruth.models import Image

print(Image.objects.all())

time = timezone.now() + datetime.timedelta(days=-60)

images = Image.objects.filter(
    shot_no=210,
    frame_no=276,
    tags__name__in=["pose-FRONT", "obstructed-FALSE", "camera-L"]
).distinct()

print("images: " + str(len(images)))

for image in images:
    print(image.filename)


