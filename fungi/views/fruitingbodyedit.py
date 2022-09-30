from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, ListView
from fungi.forms  import FruitingBodyEditForm
from fungi.models import FruitingBody, Fungi

class FruitingBodyEdit(DetailView):
	model = FruitingBody
	template_name = 'fruitingbody_detail.html'

class FungiList(ListView):
	model = Fungi
	template_name = 'fungi_list.html'
	context_object_name = 'fungis'
	paginate_by = 6

class FruitingBodyUpdate(UpdateView):
	model = FruitingBody
	fields = [
		"Colour", 
		#"ColourDescription",
		#"ShapeDescription",
		"Shape",
		"Rim", 
		#"RimDescription",
		"CapTexture",
		#'"CapTextureDescription",
		"BruiseColour", 
		"CutColour",
		"WidthMin",
		"WidthMax",
		"Comments"
		]
	template_name = 'fruitingbody_form.html'

'''
class FruitingBodyUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = FruitingBody
	fields = ['Colour','ShapeDescription']
	template_name = 'fruitingbody_detail.html'

	def form_valid(self, form):
		print('request', self)
		form.instance.FruitingBody = self.request.FruitingBody
		return super().form_valid(form)

	def test_func(self):
		FruitingBody = self.get_object()
		print('FruitingBody', FruitingBody)
		print('self.request.fungi', self.request.fungi)
		if self.request.fungi == FruitingBody.Fungi:
			return True
		return False



def FruitingBodyEdit(request):

	if request.method == 'POST':
		u_form = FruitingBodyEditForm(request.POST, instance=request.fungi.FruitingBody)
		if u_form.is_valid():
			print('FruitingBodyEdit1')
			u_form.save()
			messages.success(request, f'Fruiting Body has been updated')
			return redirect('FruitingBodyEdit')
	else:
		print('FruitingBodyEdit2')
		u_form = FruitingBodyEditForm(instance=request.fungi)

	context = {'u_form': u_form}

	return render(request, 'fruitingbody_detail.html', context)
'''