from django.forms import ModelForm
from WMS.models import Goods,inStorage,outStorage,Total

class addGoodsForm(ModelForm):
	class Meta:
		model = Goods
		fields = '__all__'

class addInSForm(ModelForm):
	class Meta:
		model = inStorage
		fields = '__all__'

class addOutSForm(ModelForm):
	class Meta:
		model = outStorage
		fields = '__all__'

class addTotalForm(ModelForm):
	class Meta:
		model = Total
		fields = '__all__'

