from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from .models import *
#from .models import Show
#from .models import ShowSearchFields
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from usersettings.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect

def filtershome(request):
	all_users= get_user_model().objects.all()
	all_show = Show.objects.all()
	context = {
		'shows' : all_show,
		'usersexists' : all_users #not currently rendered
	}
	return render(request, 'filtershome.html', context)

class EditFilter(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	#testcb = forms.BooleanField()
	model = Show
	template_name = 'show_details_form.html'  # <app>/<model>_<viewtype>.html
	fields = [
	'ShowOtherCommonNames','ShowLatinSynonyms', 'ShowGroup',
	'ShowPoresAndTubes',	'ShowGills',	'ShowSpores','ShowFlesh','ShowHabitat','ShowCuisine',	'ShowFruitingBody',
	'ShowStipe','ShowSeasons','ShowSimilarFungi','ShowStatus','ShowFungiComments','ShowLatinNames',
	'ShowClassification', 'ShowOnlyUKOccurences','ShowMacromycetes'
	] 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-EditFilter'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		self.helper.add_input(Submit('submit', 'Submit'))

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False


class SetGroups(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ShowGroup
	template_name = 'groups_form.html'  # <app>/<model>_<viewtype>.html
	fields = ['Group','GroupCheck']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False


class SetModes(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = UserModes
	template_name = 'usermodes_form.html'  # <app>/<model>_<viewtype>.html
	#fields = ['ShowAddMode','ShowEditMode']
	fields = ['AddMode','EditMode']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False

		
class SearchFieldsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ShowSearchFields
	template_name = 'searchfields_form.html'  # <app>/<model>_<viewtype>.html
	fields = '__all__' 
	fields = [
	'ExactMatch',
	'CommonName',
	'LatinName',
	'Group',
	'HabitatAssociations',
	'MonthFound',
	'HabitatPh',
	'HabitatSubstrate',
	'HabitatSoil',
	#'fbType',
	'CapColour',
	'CapShape',
	'CapRim',
	'CapTexture',
	'CapBruiseColour',
	'CapCutColour',
	'CapWidth',
	'StipeColour',
	'StipeBruiseColour',
	'StipeCutColour',
	'StipeLength',
	'StipeThickness',
	'StipeShape',
	'StipeReticulationPresent',
	'StipeReticulationColour',
	'StipeBase',
	'StipeTexture',
	'StipeRing',
	'PoresPresent',
	'PoreColour',
	'PoreShape',
	'PoreBruiseColour',
	'TubeColour',
	'TubeShape',
	'TubeBruiseColour',
	'PoreMilk',
	'GillsPresent',
	'GillsColour',
	'GillsBruiseColour',
	'GillsCutColour',
	'GillsAttachment',
	'GillsArrangement',
	'GillsMilk',
	'FleshCapColour',
	'FleshCapBruiseColour',
	'FleshCapCutColour',
	'FleshStipeColour',
	'FleshStipeBruiseColour',
	'FleshStipeCutColour',
	'SporeColour',
	'OtherCommonNames',
	'LatinSynonyms',
	'Kingdom',
	'Phyum',
	'SubPhyum',	
	'Class',
	'SubClass',
	'Order',
	'Family',
	'Genus',	
	'PoisonType',
	'CulinaryRating',
	'Odour',
	'Taste',
	'StatusStatusData',
	'StatusWhereFound'
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False

class UserGroupsEditView(SingleObjectMixin, FormView):
    model = ShowGroup
    template_name = 'user_groups_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return UserGroupFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})

class UserGroupsAddView(SingleObjectMixin, FormView):
    model = ShowGroup
    template_name = 'user_groups_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return UserGroupAddFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('usersettings:user_groups_edit', kwargs={'pk': self.object.pk})        
       