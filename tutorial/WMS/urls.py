from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.conf.urls import *

urlpatterns = [
	#展示页面URL
    url(r'^$',views.home),
    url(r'^login/$',login, {'template_name':'WMS/login.html'}),
    url(r'^goods/$',views.goods,name = 'goods'),
    url(r'^inS/$',views.inS,name = 'inS'),
    url(r'^outS/$',views.outS,name = 'OutS'),
    url(r'^total/$',views.total,name = 'Total'),
    #商品信息URL
    url(r'^addGoods/$',views.addGoods,name="addGoods"),
    url(r'^deleteGoods/(?P<id>\d+)/$',views.deleteGoods,name="goods_delete"),
    url(r'^updateGoods/(?P<id>\d+)/$',views.updateGoods,name="goods_update"),
    url(r'^resultGoods/$',views.searchGoods,name="goods_search"),
    #入库信息URL
    url(r'^addInS/$',views.addInS,name="addIns"),
  	url(r'^updateInS/(?P<id>\d+)/$',views.updateInS,name="InS_update"),
	url(r'^resultInS/$',views.searchInS,name="InS_search"),
    #出库信息URL
    url(r'^updateOutS/(?P<id>\d+)/$',views.updateOutS,name="OutS_update"),
	url(r'^resultOutS/$',views.searchOutS,name="OutS_search"),
    url(r'^deleteOutS/(?P<id>\d+)/$',views.deleteOutS,name="OutS_delete"),
    #盘库信息URL
    url(r'^addTotal/$',views.addTotal,name="addTotal"),
    url(r'^deleteTotal/(?P<id>\d+)/$',views.deleteTotal,name="total_delete"),
    url(r'^updateTotal/(?P<id>\d+)/$',views.updateTotal,name="total_update"),
    url(r'^resultTotal/$',views.searchTotal,name="total_search"),
    ]