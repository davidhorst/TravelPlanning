from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView

from  .forms import UserCreateForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserLoginView(FormView):

	template_name = 'accounts/user_login.html'
	success_url = '/travels'
	form_class = AuthenticationForm
    # redirect_field_name = '/'

	def form_valid(self, form):
		login(self.request, form.get_user())
	
		return super(UserLoginView, self).form_valid(form)

class UserRegisterView(CreateView):

	template_name = 'accounts/register.html'
	form_class = UserCreateForm
	success_url = '/travels'

	def post(self, request):
		
		form = UserCreateForm(request.POST)
		
		if form.is_valid():
			user = form.save()

			#log user in
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])

			if user is not None:
				login(request, user)

			# return to home
			return redirect(reverse('travels:home'))
		
		else:
		
			return render(request, 'accounts/register.html', {'form': form})

def logoutView(request):

	logout(request)

	return redirect('/')