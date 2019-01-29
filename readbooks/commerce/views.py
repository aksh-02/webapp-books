from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from .models import Product
from django.views.generic import DetailView, ListView
from PIL import Image
from cart.models import Cart


# Create your views here.
class CommerceHome(ListView):
	
	model = Product
	template_name = 'commerce/home.html'
	paginate_by = 36


@login_required
def add_book(request):
	form = BookForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		book = form.save(commit=False)
		book.seller = request.user
		book.save()
		return redirect('book-view', slug=book.slug)
	context = {
		'form' : form
	}
	return render(request, 'commerce/book_form.html', context)


class BookView(DetailView):
	
	model = Product
	template_name = 'commerce/book_view.html'

	def get_context_data(self, *args, **kwargs):
		context = super(BookView, self).get_context_data(*args, **kwargs)
		#cart_obj, new = Cart.objects.new_or_get(self.request)
		cart_obj = Cart.objects.get(user=self.request.user)
		context['cart'] = cart_obj
		return context