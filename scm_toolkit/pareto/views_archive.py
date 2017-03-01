
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django import forms
import django_excel as excel
from pareto.models import abc_multi_loc
import pandas as pd
from django.db import connection
from django_pandas.io import read_frame


class UploadFileForm(forms.Form):
	file = forms.FileField()
	
	
	
def import_sheet(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST,request.FILES)
		
			
		if form.is_valid():
			user_id=1
			abc_multi_loc.objects.filter(user_id=user_id).delete()
			request.FILES['file'].save_to_database(
               name_columns_by_row=2,
               model=abc_multi_loc,
               mapdict=['user_id', 'Item_id', 'item_desc','loc_id','loc_desc','loc_type','sales'])
			 
			
			
			
			html_graph=abc()
			if html_graph:   
				return render(
				request,
				'pareto/abc.html',
				{
				'form': form,
				'title': 'Excel file upload and download example',
				'header': ('Please choose any excel file:'),
				'html_graph':html_graph
				})
			else:
				return HttpResponse("OK2")
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
		
def abc():
	qs = abc_multi_loc.objects.all()
	df = read_frame(qs)
	
	df = df.sort_values(by=['loc_type','loc_id','sales'], ascending=[True,True,False])

	a=0
	cum_sum=[]
	ABC_class=[]

	tot_sum=df.sales.sum()

	for index, row in df.iterrows():
		a=a+row['sales']
		cum_sum.append(100*(a/tot_sum))
   
	df['cum_sum'] = cum_sum

	for index, row in df.iterrows():
		if row['cum_sum'] <= 80:
			ABC_class.append('A')
		if (row['cum_sum'] > 80 and row['cum_sum'] <= 95):
			ABC_class.append('B')
		if (row['cum_sum'] > 95 and row['cum_sum'] <= 100):
			ABC_class.append('C')

	df['ABC_class'] = ABC_class
	html_table = df.to_html(index=False)

	return html_table