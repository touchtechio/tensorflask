

python -m django --version

pip install django-taggit

Add "taggit" to your project’s INSTALLED_APPS setting.

Run ./manage.py migrate.


### dependencies

have a basic knowledge of python [django](https://docs.djangoproject.com/en/2.2/intro/tutorial05/webapps)

## running
```
python -m django --version
python manage.py runserver
python manage.py makemigrations images
python manage.py migrate
```

## shell testing

 ```python manage.py shell```
 ```
from images.models import Image, Region
Image.objects.all()
```

from django.utils import timezone
i = Image(filename="matt-filename", pub_date=timezone.now())
i.save()

from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

