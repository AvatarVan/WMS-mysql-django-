from django.shortcuts import render,redirect,get_object_or_404
from WMS.models import Goods,inStorage,outStorage,Total
from django.http import HttpResponseRedirect
from django.urls import reverse
from WMS.forms import addGoodsForm,addInSForm,addOutSForm,addTotalForm

# 展示页面views
def home(request):
	return render(request,'WMS/home.html')

def goods(request):
	goods_list = Goods.objects.all()
	return render(request,'WMS/goods.html',{'content':goods_list})

def inS(request):
	inS_list = inStorage.objects.all()
	return render(request,'WMS/inS.html',{'content':inS_list})

def outS(request):
	outS_list = outStorage.objects.all()
	return render(request,'WMS/outS.html',{'content':outS_list})

def total(request):
	total_list = Total.objects.all()
	return render(request,'WMS/total.html',{'content':total_list})	

# 商品信息CRUD逻辑
def addGoods(request):
	if request.method == 'POST':
		form = addGoodsForm(request.POST)
		if form.is_valid():
			goods = form.save()
			return HttpResponseRedirect(reverse("goods"))
	return  render(request,'WMS/addGoods.html',{'content':addGoodsForm()})

def deleteGoods(request,id):
	goods = get_object_or_404(Goods,pk = int(id))
	goods.delete()
	return HttpResponseRedirect(reverse("goods"))

def updateGoods(request,id):
	goods = get_object_or_404(Goods,pk = int(id))
	if request.method == 'POST':
		form = addGoodsForm(request.POST,instance = goods)
		if form.is_valid():
			goods = form.save()
			return HttpResponseRedirect(reverse("goods"))
	return render(request,'WMS/updateGoods.html',{'content':addGoodsForm(instance=goods)})

def searchGoods(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q :
		error_msg:"请输入关键字"
		return render(request,'WMS/resultGoods.html',{'error_msg':error_msg})
	search_list = Goods.objects.filter(goods_name__icontains=q)
	return render(request,'WMS/resultGoods.html',{'error_msg':error_msg,'content':search_list})

#入库信息CRUD逻辑
def addInS(request):
	if request.method == 'POST':
		form = addInSForm(request.POST)
		if form.is_valid():
			inS = form.save()
			return HttpResponseRedirect(reverse("inS"))
	return  render(request,'WMS/addInS.html',{'content':addInSForm()})

def updateInS(request,id):
	ins = get_object_or_404(inStorage,pk = int(id))
	if request.method == 'POST':
		form = addInSForm(request.POST,instance = ins)
		if form.is_valid():
			ins = form.save()
			return HttpResponseRedirect(reverse("inS"))
	return render(request,'WMS/updateInS.html',{'content':addInSForm(instance=ins)})

def searchInS(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q :
		error_msg:"请输入关键字"
		return render(request,'WMS/resultInS.html',{'error_msg':error_msg})
	search_list = inStorage.objects.filter(goods_name__icontains=q)
	return render(request,'WMS/resultInS.html',{'error_msg':error_msg,'content':search_list})

#出库信息CRUD逻辑
def updateOutS(request,id):
	outs = get_object_or_404(outStorage,pk = int(id))
	if request.method == 'POST':
		form = addOutSForm(request.POST,instance = outs)
		if form.is_valid():
			outs = form.save()
			return HttpResponseRedirect(reverse("OutS"))
	return render(request,'WMS/updateOutS.html',{'content':addOutSForm(instance=outs)})

def searchOutS(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q :
		error_msg:"请输入关键字"
		return render(request,'WMS/resultOutS.html',{'error_msg':error_msg})
	search_list = outStorage.objects.filter(goods_name__icontains=q)
	return render(request,'WMS/resultOutS.html',{'error_msg':error_msg,'content':search_list})

def deleteOutS(request,id):
	outs = get_object_or_404(outStorage,pk = int(id))
	outs.delete()
	return HttpResponseRedirect(reverse("OutS"))

#盘库信息CRUD逻辑
def addTotal(request):
	if request.method == 'POST':
		form = addTotalForm(request.POST)
		if form.is_valid():
			total = form.save()
			return HttpResponseRedirect(reverse("Total"))
	return  render(request,'WMS/addTotal.html',{'content':addTotalForm()})

def deleteTotal(request,id):
	total = get_object_or_404(Total,pk = int(id))
	total.delete()
	return HttpResponseRedirect(reverse("Total"))

def updateTotal(request,id):
	total = get_object_or_404(Total,pk = int(id))
	if request.method == 'POST':
		form = addTotalForm(request.POST,instance = total)
		if form.is_valid():
			total = form.save()
			return HttpResponseRedirect(reverse("Total"))
	return render(request,'WMS/updateTotal.html',{'content':addTotalForm(instance=total)})

def searchTotal(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q :
		error_msg:"请输入关键字"
		return render(request,'WMS/resultTotal.html',{'error_msg':error_msg})
	search_list = Total.objects.filter(goods_name__icontains=q)
	return render(request,'WMS/resultTotal.html',{'error_msg':error_msg,'content':search_list})
