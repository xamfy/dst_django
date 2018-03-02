from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Data
from .forms import SearchForm

# class IndexView(TemplateView):
# 	template_name = "data/home.html"

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['dst'] = Data.objects.all()
# 		return context
def search(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			dst = Data.objects.filter(date=form.cleaned_data.get('date'))
			return render(request, 'data/home.html', {'form':form, 'dst':dst})
			
	else:
		form = SearchForm()
	
	return render(request, 'data/home.html', {'form':form})