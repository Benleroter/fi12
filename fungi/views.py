from django.shortcuts import render

def fungilist(request):
	if request.method="POST":
		form=FruitingBodyEditForm(request.POST)
		if form.is_valid():
			form(save)
			return redirect('fungilist')

	else:
		form = FruitingBodyEditForm()

	context = {
		'fbform': form
	}

	return render(request, 'fruitingbody_detail.html', context)