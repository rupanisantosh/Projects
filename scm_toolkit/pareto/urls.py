from django.conf.urls import url
from pareto import views


urlpatterns = [
    url(r'^$', views.import_sheet, name='import_sheet')
]