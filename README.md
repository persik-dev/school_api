## Мини RESTful API на примере школы, для представления:

    -Generic Views 
    -drf-writable-nested 
    -django-filter
    -djangorestframework.filters
    -drf_yasg


## Конфигурация
    pip install -r requirements.txt 
    python manage.py makemigrations
    python manage.py migrate


## Модели и связи между ними

    Teacher     <->     School      = ManyToMany 
    
    FormMaster  ->      School      = ManyToOne 
    FormMaster  <->     Teacher     = OneToOne
    FormMaster  ->      Section     = ManyToOne 

    Section     ->      School      = ManyToOne

    Subject     <->      Teacher     = ManyToMany
    Subject     ->      School      = ManyToOne 

    Student     ->      School      = ManyToOne 
    Student     ->      Section     = ManyToOne 


## Документация доступна по 
    
    http://127.0.0.1:8000/swagger/ 
    
    http://127.0.0.1:8000/redoc/


### Cсылки:
    https://www.django-rest-framework.org/api-guide/generic-views/
    
    https://pypi.org/project/drf-writable-nested/
    
    https://django-filter.readthedocs.io/en/stable/ 


