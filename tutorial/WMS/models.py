from django.db import models

class Goods(models.Model):
	goods_id = models.CharField('商品编号',max_length = 10)
	goods_name = models.CharField('商品名称',max_length = 10)
	goods_type = models.CharField('商品类别',max_length = 10)
	plan_in_cost = models.DecimalField('计划进货价格',max_digits = 11,decimal_places = 2)
	plan_out_cost = models.DecimalField('计划出货价格',max_digits = 11,decimal_places = 2)
	storage = models.IntegerField('原始库存')
	def __str__(self):
		return u'%s %s' %(self.goods_id,self.goods_name)
		
class inStorage(models.Model):
	in_id = models.CharField('入库单号',max_length = 10)
	in_date = models.DateField('入库日期')
	goods_id = models.CharField('商品编号',max_length = 10)
	goods_name = models.CharField('商品名称',max_length = 10)
	in_number = models.IntegerField('进货数量')
	in_cost = models.DecimalField('进货价格',max_digits = 11,decimal_places = 2)
	in_amount = models.DecimalField('进货总价',max_digits = 11,decimal_places = 2)
	def __str__(self):
		return u'%s %s' %(self.goods_id,self.goods_name)

class outStorage(models.Model):
	out_id = models.CharField('出库单号',max_length = 10)
	out_date = models.DateField('出库日期')
	goods_id = models.CharField('商品编号',max_length = 10)
	goods_name = models.CharField('商品名称',max_length = 10)
	out_number = models.IntegerField('出货数量')
	out_cost = models.DecimalField('出货价格',max_digits = 11,decimal_places = 2)
	out_amount = models.DecimalField('出货总价',max_digits = 11,decimal_places = 2)
	def __str__(self):
		return u'%s %s' %(self.goods_id,self.goods_name)
		
class Total(models.Model):
	goods_id = models.CharField('商品编号',max_length = 10)
	goods_name = models.CharField('商品名称',max_length = 10)
	last_month = models.CharField('上月盘存',max_length = 10)
	inNum = models.CharField('本月入库',max_length = 10)
	outNum = models.CharField('本月出库',max_length = 10)
	remain = models.CharField('结余',max_length = 10)
	profit = models.CharField('盈亏数量',max_length = 10)
	def __str__(self):
		return u'%s %s' %(self.goods_id,self.goods_name)