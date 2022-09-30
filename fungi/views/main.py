from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from fungi.models import Fungi, LatinSynonyms
from fungi.views.filteredfungi import FungiToSearch
from fungi.models import *
from usersettings.models import Show, ShowSearchFields
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView
from django import forms
from fungi.forms import UserRegisterForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView

from django.contrib.auth.models import AnonymousUser

from django.forms import modelformset_factory, inlineformset_factory
#from .models import Fungi
#from fungi.forms import ProductForm, ProductMetaInlineFormset

#from fungi.forms import FungiLatinSynomymsFormset
from fungi.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.user.is_authenticated:
        uid = request.user
        print('uid', uid)
        UserShowSettings = Show.objects.get(user_id=request.user)
    else:
        uid = User.objects.get(username='GuestUser') 
        print('uid',uid)
        UserShowSettings = Show.objects.get(user_id= uid)
    
    context = {
        'fungis' : Fungi.objects.all(),
        }
    return render(request, 'home.html', context) 

def Links(request):
    return render(request, 'links.html')

def AllSources(request):
    sources = NetLinks.objects.order_by().values('Website').distinct()
    print('sourcesquery', sources.query)    

    context = {
       'sources' : NetLinks.objects.order_by('Website').values('Website').distinct()
    }
    return render(request, 'sources.html', context)

AddMode = False

def AllGroups(request):
    groups = Fungi.objects.order_by('Group').values('Group').distinct()
    context = {
        'groups': Fungi.objects.order_by('Group').values('Group').distinct()
    }
    return render(request, 'groups.html', context)

    
def AllFungi(request):
    if request.user.is_authenticated:
        print('uid:', request.user)
        uid = request.user
        UserShowSettings = Show.objects.get(user_id= request.user)
    else:
        uid = User.objects.get(username='GuestUser') 
        UserShowSettings = Show.objects.get(user_id= uid)

    #Show or don't show non-UK Species and/or Macromycetes
    FungiToRender = FungiToSearch(Fungi, UserShowSettings.ShowOnlyUKOccurences, UserShowSettings.ShowMacromycetes)
    print('FUNGI', Fungi)
    context = {
        'fungis' : FungiToRender[0],
        'fungicount' : FungiToRender[1],
        'ResultText' : FungiToRender[2]
        }
    return render(request, 'allfungi.html', context)

def ShowGlossary(request):
    PID =Glossary.objects.all()
    context = {
        'Glossary' : PID
    }
    #print('Glossary context:', context)
    return render(request, 'glossary.html', context)

class ShowGlossaryEntry(DetailView):
    model = Glossary
    template_name = 'glossarydetail.html'

def searchsuccess(request):
    return render(request, 'search_results.html')

def nosearchresults(request):
    return render(request, 'nosearchresults.html')    

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

class LatinSynomymsList(ListView):
    model = LatinSynonyms
    fields = '__all__'
    template_name = 'latinsynonyms_list.html'
    content_object_name = 'synonyms'

    def get_queryset(self):
        fungi = get_object_or_404(Fungi, CommonName=self.kwargs.get('CommonName'))
        print('fungi', fungi)
        return Fungi.objects.filter(CommonName=fungi)

class ProductListView(ListView):
    pass

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'product_form.html'
    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['product_meta_formset'] = ProductMetaInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        product_meta_formset = ProductMetaInlineFormset(self.request.POST)
        if form.is_valid() and product_meta_formset.is_valid():
            return self.form_valid(form, product_meta_formset)
        else:
            return self.form_invalid(form, product_meta_formset)
    def form_valid(self, form, product_meta_formset):
        self.object = form.save(commit=False)
        self.object.save()
        # saving ProductMeta Instances
        product_metas = product_meta_formset.save(commit=False)
        for meta in product_metas:
            meta.product = self.object
            meta.save()
        return redirect(reverse("product:product_list"))

    def form_invalid(self, form, product_meta_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  product_meta_formset=product_meta_formset
                                  )
        )

def index(request, fungi_id):
    fungi = Fungi.objects.get(pk=fungi_id)
    LanguageFormset = inlineformset_factory(Fungi, LatinSynonyms, can_delete=False, extra=0, labels=None, fields=('LatinSynonym',))

    if request.method == 'POST':
        formset = LanguageFormset(request.POST, instance=fungi)
        if formset.is_valid():
            formset.save()
            return redirect('index', fungi_id=Fungi.id)

    #formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = LanguageFormset(instance=fungi)

    return render(request, 'index.html', {'formset' : formset})


class FungiListView(ListView):
    model = Fungi
    template_name = 'fungi_list2.html'

class FungiDetailView(DetailView):
    model = Fungi
    template_name = 'Fungi_detail.html'

class FungiEditView(UpdateView):
    model = Fungi
    template_name = 'fungi_edit.html'
    #fields ='__all__'
    fields = ['CommonName', 'LatinName','Group','UKSpecies','Macromycetes','Comments']
        


class FungiCreateView(CreateView):
    model = Fungi
    template_name = 'fungi_create.html'
    #fields = ['CommonName','LatinName','Group']
    #exclude = ['slug']
    #fields ='__all__'
    fields = ['CommonName', 'LatinName', 'Group','UKSpecies','Macromycetes','Comments']
    def form_valid(self, form):

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The Fungi has been added'
        )

        return super().form_valid(form)

class GlossaryTermView(CreateView):
    model = Glossary
    template_name = 'glossary_term_create.html'
    fields ='__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The new term has been added'
        )

        return super().form_valid(form)




#class GlossaryTermUpdateView(UpdateView):

class FungiView(CreateView):
    model = Fungi
    template_name = 'fungi_edit2.html'
    fields ='__all__'

    def form_valid(self, form):

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The fungi has been edited'
        )

        return super().form_valid(form)



class FungiLatinSynomymsView(SingleObjectMixin, FormView):

    model = Fungi
    template_name = 'fungi_latinsynonyms_edit_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiLatinSynomymsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiLatinSynomymsDeleteView(SingleObjectMixin, FormView):

    model = Fungi
    template_name = 'fungi_latinsynonyms_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiLatinSynomymsDeleteFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})
'''
class FungiEditView(SingleObjectMixin, FormView):

    model = Fungi
    template_name = 'fungi_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})
'''

class FungiHabitatEditView(SingleObjectMixin, FormView):

    model = Fungi
    template_name = 'fungi_habitat_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiHabitatFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})
        

class FungiCapEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_cap_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCapFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiStipeEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_stipe_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiStipeFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiCuisineEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_cuisine_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCuisineFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiFleshEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_flesh_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiFleshFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiSimilarView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_similar_edit_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSimilarFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})           
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiSimilarDeleteView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_similar_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSimilarDeleteFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})   
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})     

class FungiCommonNamesView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_commonnames_edit_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCommonNamesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiCommonNamesDeleteView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_commonnames_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCommonNamesDeleteFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiSeasonsEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_seasons_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSeasonsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})  
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})      

class FungiSporesEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_spores_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSporesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})   
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug}) 

class FungiStatusEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_status_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiStatusFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiPoresEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_pores_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiPoresFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiGillsEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_gills_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiGillsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiCommentsEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_comments_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCommentsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})




class FungiTaxonomyEditView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_taxonomy_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiTaxonomyFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiLinksView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_netlinks_edit_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiNetLinksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiLinksDeleteView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_netlinks_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiNetLinksDeleteFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiRefsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_refs_edit_add.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiRefsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class FungiRefsDeleteView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_refs_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiRefsDeleteFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk}) 
        return reverse('FungiDetail-Page',kwargs={'slug':self.object.slug})

class GlossaryFormView(FormView):
    template_name = 'glossary_term_create.html'
    form_class = GlossaryFormset
    success_url = '/'

    def form_valid(self, form):
        form.save()

        return HttpResponseRedirect(self.get_success_url())