from django.shortcuts import render
from django.views.generic import ListView
from commerce.models import Product
from django.db.models import Q
# Create your views here.

class SearchView(ListView):
	template_name = "search/s_home.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q', None)
		if query is not None:
			lookups = Q(name__icontains=query) | Q(author__icontains=query)
			return Product.objects.filter(lookups).distinct()
		return Product.objects.all()