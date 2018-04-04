"""traineau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),

    # url(r'^update_timeText/$', views.init_data, name='update_timeText'),

    url(r'^get_initial_data/$', views.get_initial_data, name='get_initial_data'),

    url(r'^prod_one/$', views.ProdL1, name='prod_one'),
    url(r'^prod_two/$', views.ProdL2, name='prod_two'),
    url(r'^prod_three/$', views.ProdL3, name='prod_three'),
    url(r'^prod_four/$', views.ProdL4, name='prod_four'),
    url(r'^prod_five/$', views.fProdASS, name='prod_five'),

    url(r'^prod_six/$', views.fProdSKI1, name='prod_six'),
    url(r'^prod_seven/$', views.fProdSKI2, name='prod_seven'),

    url(r'^prod_eight/$', views.fProdSEAT, name='prod_eight'),
    url(r'^nc_one/$', views.NC1, name='nc_one'),
    url(r'^nc_two/$', views.NC2, name='nc_two'),
    url(r'^nc_three/$', views.NC3, name='nc_three'),
    url(r'^nc_four/$', views.NC4, name='nc_four'),
    url(r'^nc_five/$', views.fNCASS, name='nc_five'),

    url(r'^nc_six/$', views.fNCSKI1, name='nc_six'),
    url(r'^nc_seven/$', views.fNCSKI2, name='nc_seven'),

    url(r'^nc_eight/$', views.fNCSEAT, name='nc_eight'),
    url(r'^resume_job/$', views.resume_job, name='resume_job'),
     url(r'^pause_job/$', views.pause_job, name='pause_job'),
    url(r'^start_job/$', views.start_job, name='start_job'),
    url(r'^stop_job/$', views.stop_job, name='stop_job'),

    url(r'^setting/$', views.setting, name='setting'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^update_data/$', views.update_data, name='update_data'),
    url(r'^getStartUpdate/$', views.getStartUpdate, name='getStartUpdate'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^temps_de_cycle/$', views.temps_de_cycle, name='temps_de_cycle'),
    url(r'^temps_de_passage/$', views.temps_de_passage, name='temps_de_passage'),


    
]
