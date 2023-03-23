from django.http import HttpResponse
from django.shortcuts import render
from pandas import read_csv,read_excel,read_sql,read_json,DataFrame
from re import search
from pymysql import connect
from .models import import_data1

#from __future__ import print_function

import os.path


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

data_creation=import_data1()
# Create your views here.
#Here we are going to render home page of our project
def home_view(request,*args,**kwargs):
    return render(request,"about.html",{})



#this is the functions will redirect to the appropriate page for requesting of datasets
def csv_dataset(request):
    return render(request,"csvimport.html",{})
def excel_dataset(request):
    return render(request,"excelimport.html",{})
def database_dataset(request):
    return render(request,"mysqlimport.html",{})
def googlesheets_dataset(request):
    return render(request,"googlesheetsimport.html",{})

def csv_importing_data(request,*args,**kwargs):
    file_name="F:/DATASETS/CSV/"+request.POST.get('fname')
    #print(file_name)
    try:
        df=read_csv(file_name)
        data_creation.data=df
        cols_data=list(data_creation.data.columns)
        my_data={"cols":cols_data}
        return render(request,"show_cols.html",my_data)
    except:
        err="Seems the dataset you searced here is not found sorry"
        return render(request,"Error_google.html",{"Error":err})
def excel_importing_data(request,*args,**kwargs):
    file_name="F:/DATASETS/EXCEL/"+request.POST.get('fname')
    #print(file_name)
    try:
        df=read_excel(file_name)
        print(df.columns)
        data_creation.data=df
        cols_data=list(data_creation.data.columns)
        my_data={"cols":cols_data}
        return render(request,"show_cols.html",my_data)
    except:
        err="Seems the dataset you searced here is not found sorry"
        return render(request,"Error_google.html",{"Error":err})
def data_base_importing_data(request,*args,**kwargs):
    #selecting database
    data_base=connect(host="localhost",user="root",passwd="Harikrishna1.",database="infosy_project")

    #this below code snipt will check whether the searching table is in database or not
    #if it is in database then go on ti next step    
    # django_migrations    
    table_name=request.POST.get('fname')
    print(request)
    #table_name=(table_name,)
    """query1="show tables"
    cur=data_base.cursor()
    cur.execute(query1)
    tables=cur.fetchall
    if table_name in tables:"""

    #this code snipt comes under the if: condition
    #table_name.strip()
    #query="select * from "+table_name
    query="select * from "+table_name
    cur=data_base.cursor()
    cur.execute(query)


    tables=cur.fetchall()
    df=read_sql(query,data_base)
    data_creation.data=df
    cols_data=list(df.columns)
    my_data={"cols":cols_data}
    return render(request,"show_cols.html",my_data)
def googlesheets_importing_data(request,*args,**kwargs):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'C:/infosys_project/import_data1/keys.json'
    creds=None
    creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = request.POST.get("fname")
    Sheet_range=request.POST.get('range')
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        
        #this is for reading 
        #"Sheet1!A1:I95"
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=Sheet_range).execute()
        #list=[["haell",400],["erwe",4563]]
        #this is for writing
        #request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!B1", valueInputOption="USER_ENTERED", body={"values":list}).execute()
        #print(result)

        #this is for conversion of sheet to dataframe
        df=DataFrame(result["values"])
        df.columns=result["values"][0]
        df=df.drop(0)
        df.reset_index(drop=True,inplace=True)
        cols_data=list(df.columns)
        data_creation.data=df
        my_data={"cols":cols_data}
        return render(request,"show_cols.html",my_data)
    except HttpError as err:
        return render(request,"Error_google.html",{"Error":err})
#Here this code will import the required csv file from github or from localstorage of the server.
#And shows the data.In the for of a table
def view_data(request,*args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")

    #if the columns for masking is not given then the length of the column name will be 0
    column=request.POST.get('fname')

    try:
        """df=read_csv(file_name)
        data_creation.data=df"""
        cols_data=list(data_creation.data.columns)
        if len(column)>0:
            cols_data.remove(column)
        #print(cols_data)
        df=data_creation.data
        li=[]
        min_rows=int(df.shape[0]*0.2)
        for i in range(min_rows):
            li.append(list(df.loc[i][cols_data]))
        my_data={"data":li,"cols":cols_data}
        return render(request,"show.html",my_data)
    except:
        err="Seems there is an error found sorry"
        return render(request,"Error_google.html",{"Error":err})
