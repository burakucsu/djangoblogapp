#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dblog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
#python manage.py runserver --> server açmak için
#python manage.py migrate --> uyarı veriyor modülleri kullanmak için
#python manage.py createsuperuser --> ana kullanıcı oluşturmak için 
#python manage.py startapp article --> modül oluşturmak için bkz Settinng admin vs.
#python manage.py makemigrations --> Article tablosunu db tarafında oluşturmak için yapılan modül
#python manage.py shell bunda django sorguları da dahil