from django.contrib import admin
from WMS.models import Goods,inStorage,outStorage,Total

class GoodsAdmin(admin.ModelAdmin):
	list_display = ('goods_id','goods_name','goods_type')
	search_fields = ('goods_name','goods_type')
	ordering = ('id',)

class inAdmin(admin.ModelAdmin):
	list_display = ('goods_id','goods_name')
	search_fields = ('goods_name','in_id')
	ordering = ('id',)

class outAdmin(admin.ModelAdmin):
	list_display = ('goods_id','goods_name')
	search_fields = ('goods_name','out_id')
	ordering = ('id',)

class TotalAdmin(admin.ModelAdmin):
	list_display = ('goods_id','goods_name','profit')
	search_fields = ('goods_name',)
	ordering = ('id',)

admin.site.register(Goods,GoodsAdmin)
admin.site.register(inStorage,inAdmin)
admin.site.register(outStorage,outAdmin)
admin.site.register(Total,TotalAdmin)
	
# Register your models here.
