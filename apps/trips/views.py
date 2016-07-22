from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, View, ListView, FormView
from django.views.generic.detail import DetailView


from .forms import AddTripForm
from .models import Trip, Traveler

from django.contrib.auth.models import User

class HomePageView(TemplateView):
	template_name = 'trips/index.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(HomePageView, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['my_trips'] = Trip.objects.filter(user=self.request.user)
		context['other_trips'] = Trip.objects.exclude(user=self.request.user)
		print context['my_trips']
		return context

class AddTripView(FormView):
	template_name = 'trips/add.html'
	success_url = '/travels'
	form_class = AddTripForm
    # redirect_field_name = '/'
	def form_valid(self, form):
		form = form.save(commit=False)
		print self.request.user
		user = User.objects.get(pk=self.request.user.id)
		form.user = self.request.user
		form.save()
		# Trip.objects.create(user=user, location=form.location, start_date=form.start_date, end_date=form.end_date)
		return super(AddTripView, self).form_valid(form)

def jointrip(request, pk):
	trip = Trip.objects.get(pk =pk)
	newtraveler = Traveler.objects.create(Traveler_id=request.user, Trip_id=trip)
	print newtraveler
	return redirect('/travels')

class TripDetailView(DetailView):
	model = Trip
	template_name = "trips/details.html"
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TripDetailView, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['travelers'] = Traveler.objects.filter(Trip_id=self.object.pk)
		for item in context['travelers']:
			print item.Traveler_id
		return context
