from django.shortcuts import render
from pandas import read_json
from import_data1.models import import_data1
from import_data1.views import data_creation
from upload.views import save_file_name
from re import search
# Create your views here.
def cleaning_dataset(request,*args,**kwargs):
    df=data_creation.data
    #print(df)
    if len(df)==0:
        return render(request,"Error_google.html",{"Error":"There is no any dataset downloaded upto now"})
    try:
        df2=read_json("C:/infosys_project/media/"+save_file_name.file_name)
        df=data_creation.data
        column_cleaning=list(df2)[0]
        if df2.loc["method",list(df2)[0]]=="mean":
            try:
                if df2.loc["data_type",list(df2)[0]]=="int":
                    mean_value=int(df[column_cleaning].mean())
                    df[column_cleaning].fillna(mean_value,inplace=True)
                else:
                    mean_value=(df[column_cleaning].mean())
                    df[column_cleaning].fillna(mean_value,inplace=True)
            except:
                mean_value=df[column_cleaning].mean()
                df[column_cleaning].fillna(mean_value,inplace=True)
        elif df2.loc["method",list(df2)[0]]=="mode":
            mode_value=df[column_cleaning].mode()
            df[column_cleaning].fillna(mode_value,inplace=True)
        else:
            return render(request,"Error_google.html",{"Error":"please enter valid method to fill the null values"})
        cols_data=data_creation.columns
        #print(cols_data)
        df=data_creation.data

        li=[]
        min_rows=int(df.shape[0]*0.2)
        for i in range(min_rows):
            li.append(list(df.loc[i][cols_data]))
        my_data={"data":li,"cols":cols_data}
        return render(request,"show_cleaning_dataset.html",my_data)
        
    except:
        return render(request,"Error_google.html",{"Error":"Seems your json file did not uploaded"})