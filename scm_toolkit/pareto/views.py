
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django import forms
import django_excel as excel
from pareto.models import abc_multiloc, abc_multiloc_analysis
import pandas as pd
from django.db import connection
from django_pandas.io import read_frame
from crum import get_current_user
import json
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
from django.conf import settings
from sqlalchemy import create_engine


user = settings.DATABASES['primary']['USER']
password = settings.DATABASES['primary']['PASSWORD']
database_name = settings.DATABASES['primary']['NAME']

database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)


class UploadFileForm(forms.Form):
	file = forms.FileField()
	
	
	
def import_sheet(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST,request.FILES)
		
		

			
		if form.is_valid():
			user_id=get_current_user()
			abc_multiloc.objects.filter(creator=user_id).delete()                                                                                                                                                                                                                               
			request.FILES['file'].save_to_database(
               name_columns_by_row=2,
               model=abc_multiloc,
               mapdict=['item_id', 'item_desc','loc_id','loc_desc','loc_type','sales'])
			
			data_table = abc(user_id)
			
			data_graph_x=abc_graph_x(user_id)
			
			
			
			
			if data_table:  
				data =  [
				['Year', 'Sales', 'Expenses'],
				[2004, 1000, 400],
				[2005, 1170, 460],
				[2006, 660, 1120],
				[2007, 1030, 540]
				]
				
				data1=data_graph_x
				print(data1)
				# DataSource object
				data_source = SimpleDataSource(data=data1)
				# Chart object
				chart = LineChart(data_source)
				#context = {'chart': chart}


				return render(
				request,
				'pareto/results.html',
				#context,
				{
				'form': form,
				'title': 'Excel file upload and download example',
				'header': ('Please choose input excel file:'),
				'data_table':data_table,
				'chart': chart
				}
				)
				
			else:
				return HttpResponse("Something is Wrong")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
		return render(
		request,
		'pareto/abc.html',
		{
		'form': form,
		'title': 'Excel file upload and download example',
		'header': ('Please choose any excel file:')
		})
		
def abc(user_id):
	qs = abc_multiloc.objects.filter(creator=user_id)
	df = read_frame(qs)
	df = df.sort_values(by=['loc_type','loc_id','sales'], ascending=[True,True,False])
	a=0
	cum_sum=[]
	ABC_Class=[]

	tot_sum=df.sales.sum()

	for index, row in df.iterrows():
		a=a+row['sales']
		cum_sum.append(100*(a/tot_sum))
   
	df['cum_sum'] = cum_sum

	for index, row in df.iterrows():
		if row['cum_sum'] <= 80:
			ABC_Class.append('A')
		if (row['cum_sum'] > 80 and row['cum_sum'] <= 95):
			ABC_Class.append('B')
		if (row['cum_sum'] > 95 and row['cum_sum'] <= 100):
			ABC_Class.append('C')

	df['ABC_Class'] = ABC_Class
	df = df.sort_values(by=['ABC_Class'], ascending=[True])
	
	abc_multiloc_analysis.objects.filter(creator=user_id).delete() 
	df.columns = df.columns.astype(str)
	df.reset_index().to_sql(abc_multiloc_analysis, con=engine, index=False,chunksize=None, dtype=None, if_exists='append')
	
	df.drop(['id','creator','last_editor'],inplace=True,axis=1,errors='ignore')
	
	print(df.head())
	
	#df.to_sql(HistoricalPrices, con=engine)
	
	html_table = df.to_html(index=False)

	return html_table

def abc_graph_x(user_id):
	qs = abc_multiloc.objects.filter(creator=user_id)
	df = read_frame(qs)
	df = df.sort_values(by=['loc_type','loc_id','sales'], ascending=[True,True,False])
	df.drop(['id','item_id', 'item_desc','loc_desc','loc_type','creator','last_editor'],inplace=True,axis=1,errors='ignore')
	data_graph_x = df.groupby( [ "loc_id"] ).sum()
	data_graph_x=data_graph_x.reset_index()
	data_graph_x=data_graph_x.as_matrix()
	print(data_graph_x)
	return data_graph_x																	
				  
				  
				  
				  
				  
				  


	