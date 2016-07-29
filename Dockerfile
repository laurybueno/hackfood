FROM django:onbuild

RUN pip install djangorestframework && \
    pip install markdown      && \
    pip install django-filter

CMD python manage.py runserver 0.0.0.0:8000
