from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import *
#from .models import FruitingBody
#from .models import LatinSynonyms
#from .models import Habitat
#from .models import Stipe
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FungiForm(forms.ModelForm):
		class Meta:
			model = Fungi
			fields  = "__all__"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserSearchForm(forms.Form):
    pass

class GroupForm(forms.Form):
    pass


class FruitingBodyEditForm(forms.ModelForm):
    class Meta:
        model = FruitingBody
        fields  = "__all__"



class ProductForm(forms.ModelForm):
    class Meta:
        model = Fungi
        fields = ('id','CommonName')
        #fields = ('name', 'price')

class ProductMetaForm(forms.ModelForm):
    class Meta:
        model = LatinSynonyms
        fields  = "__all__"
        #fields = ('LatinSynonym',)


class FungiForm(forms.ModelForm):
    class Meta:
        model = Fungi
        fields = "__all__"


FungiFormset = inlineformset_factory(
    Fungi,
    Habitat,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )


FungiHabitatFormset = inlineformset_factory(
    Fungi,
    Habitat,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiCapFormset = inlineformset_factory(
    Fungi,
    FruitingBody,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiStipeFormset = inlineformset_factory(
    Fungi,
    Stipe,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiCuisineFormset = inlineformset_factory(
    Fungi,
    Cuisine,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiFleshFormset = inlineformset_factory(
    Fungi,
    Flesh,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiSeasonsFormset = inlineformset_factory(
    Fungi,
    Seasons,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiSporesFormset = inlineformset_factory(
    Fungi,
    Spores,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiStatusFormset = inlineformset_factory(
    Fungi,
    Status,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiPoresFormset = inlineformset_factory(
    Fungi,
    PoresAndTubes,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiGillsFormset = inlineformset_factory(
    Fungi,
    Gills,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiCommentsFormset = inlineformset_factory(
    Fungi,
    FungiComments,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiTaxonomyFormset = inlineformset_factory(
    Fungi,
    Classification,
    extra=0,
    labels='',
    can_delete=False,
    fields='__all__'
    )
FungiNetLinksFormset = inlineformset_factory(
    Fungi,
    NetLinks,
    extra=1,
    labels='',
    can_delete=False,
    fields=('Website','Websiteurl')
    )

FungiNetLinksDeleteFormset = inlineformset_factory(
    Fungi,
    NetLinks,
    extra=0,
    labels='',
    can_delete=True,
    fields=('Website','Websiteurl')
    )

FungiRefsFormset = inlineformset_factory(
    Fungi,
    DetailSources,
    extra=1,
    labels='',
    can_delete=False,
    fields='__all__'
    )

FungiRefsDeleteFormset = inlineformset_factory(
    Fungi,
    DetailSources,
    extra=0,
    labels='',
    can_delete=True,
    fields='__all__'
    )

FungiLatinSynomymsFormset = inlineformset_factory(
    Fungi,
    LatinSynonyms,
    extra=1,
    labels='',
    can_delete=False,
    fields=('LatinSynonym','LatinSynonymSource')
    )

FungiLatinSynomymsDeleteFormset = inlineformset_factory(
    Fungi,
    LatinSynonyms,
    extra=0,
    labels='',
    can_delete=True,
    fields=('LatinSynonym',)
    )

FungiSimilarFormset = inlineformset_factory(
    Fungi,
    SimilarFungi,
    extra=1,
    labels='',
    can_delete=False,
    fields=('SimilarFungiId','SimilarFungiName')
    )

FungiSimilarDeleteFormset = inlineformset_factory(
    Fungi,
    SimilarFungi,
    extra=0,
    labels='',
    can_delete=True,
    fields='__all__'
    )

FungiCommonNamesFormset = inlineformset_factory(
    Fungi,
    OtherCommonNames,
    extra=1,
    labels='',
    can_delete=False,
    fields=('AltCommonName',)
    )

FungiCommonNamesDeleteFormset = inlineformset_factory(
    Fungi,
    OtherCommonNames,
    extra=0,
    labels='',
    can_delete=True,
    fields=('AltCommonName',)
    )

GlossaryFormset = modelformset_factory(
    Glossary,
    extra=1,
    labels='',
    can_delete=True,
    fields='__all__'
    )

FungiFormset = modelformset_factory(
    Fungi,
    extra=1,
    labels='',
    can_delete=True,
    fields='__all__'
    )