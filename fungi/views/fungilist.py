from django.shortcuts import render
from fungi.forms import FruitingBodyEditForm, FungiForm

def FungiList2(request):
	if request.method=="POST":
		form=FruitingBodyEditForm(request.POST)
		if form.is_valid():
			form(save)
			return redirect('FungiList')

	else:
		form = FruitingBodyEditForm()

	context = {
		'fbform': form
	}

	return render(request, 'fungi_list.html', context)


def FungiList(request):
	if request.method=="POST":
		form=FungiForm(request.POST)
		if form.is_valid():
			form(save)
			return redirect('FungiList')

	else:
		form = FungiForm()

	context = {
		'fbform': form
	}

	return render(request, 'fungi_list.html', context)