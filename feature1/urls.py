"""feature1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from import_data1.views import *
from Validations.views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name='home'),
    #This following are the paths which will show the columns of the imported files
    path('csv_imported/',csv_importing_data,name="importing the csv file"),
    path('excel_imported/',excel_importing_data,name="importing the excel file"),
    path('database_imported/',data_base_importing_data,name="importing the database file"),
    path('googlsheet_imported/',googlesheets_importing_data,name="importing the googlesheets file"),

    #The following are the paths which are going to display the content of imported file in a table format
    path('viewing_data/', view_data, name='csv'),
    

    #this is admin path
    path("admin/", admin.site.urls),

    #this path for validation of the datasets
    path("validation/",validation_on_datasets,name="validation on dataset"),

    #this path is for importing of datasets..
    path("csv_dataset/",csv_dataset,name="csv_import_datasets"),
    path("excel_dataset/",excel_dataset,name="excel_import_dataset"),
    path("database_dataset/",database_dataset,name="database_import_dataset"),
    path("googlesheets_dataset/",googlesheets_dataset,name="googlesheets_import_dataset"),
]
