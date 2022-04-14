from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, ListView
from fungi.forms  import FruitingBodyEditForm
from fungi.models import *

class FruitingBodyEdit(DetailView):
	model = FruitingBody
	template_name = 'fruitingbody_detail.html'

class FungiList(ListView):
	model = Fungi
	template_name = 'fungi_list.html'
	context_object_name = 'fungis'
	paginate_by = 6

class FruitingBodyUpdate(UpdateView):
	model = FruitingBody
	fields = [
		"Colour", 
		"ColourDescription",
		"ShapeDescription", 
		"Rim", 
		"RimDescription", 
		"CapTexture",
		"CapTextureDescription",
		"BruiseColour", 
		"CutColour",
		"WidthMin",
		"WidthMax",
		"Comments"
		]
	template_name = 'fruitingbody_form.html'

class HabitatUpdate(UpdateView):
	model = Habitat
	fields = [
		"Associations",
		"Ph",
		"Soil",
		"Substrate", 
		"Comments" 
		]
	template_name = 'habitat_form.html'


class OtherCommonNamesUpdate(UpdateView):
	model = OtherCommonNames
	fields = ['AltCommonName']
	template_name = 'othercommonnames_form.html'

class LatinSynonymsUpdate(UpdateView):
	model = LatinSynonyms
	fields = ['LatinSynonym']
	template_name = 'latinsynonyms_form.html'
	#success_url="/latinsynonyms-list"

class FungiCommentsUpdate(UpdateView):
	model = FungiComments
	fields = ['Comments']
	template_name = 'fungicomments_form.html'

class StipeUpdate(UpdateView):
	model = Stipe
	fields = [
		"Colour",
		"BruiseColour", 
		"CutColour", 
		"LengthMin", 
		"LengthMax", 
		"ThicknessMin", 
		"ThicknessMax", 
		"ShapeDescription",
		"ReticulationPresent", 
		"ReticulationColour",
		"ReticulationDescription",	
		"Base",
		"BaseDescription",
		"TextureDescription",
		"Ring", 
		"RingDescription", 
	    "Volva", 
		"Comments",
	]
	template_name = 'stipe_form.html'

class PoresAndTubesUpdate(UpdateView):
	model = PoresAndTubes
	fields = [
		"PoresPresent", 
		"PoreColour", 
		"PoreShape",
		"PoreBruiseColour", 
		"TubeColour", 
		"TubeShape",
		"TubeBruiseColour", 
		"Milk",
		"Comments" 
	]
	template_name = 'poresandtubes_form.html'
	#success_url="/"

class GillsUpdate(UpdateView):
	model = Gills
	fields = [
		"GillsPresent", 
		"Colour", 
		"BruiseColour", 
		"CutColour", 
		"Attachment", 
		"Arrangement", 
		"Milk", 
		"Comments"
	]
	template_name = 'gills_form.html'

class SporesUpdate(UpdateView):
	model = Spores
	fields = ["Colour","Comments"	]
	template_name = 'spores_form.html'

class CuisineUpdate(UpdateView):
	model = Cuisine
	fields = [
		"PoisonType",
		"CulinaryRating",
		"Odour",
		"Taste",
		"Comments"
	]
	template_name = 'cuisine_form.html'

class FleshUpdate(UpdateView):
	model = Flesh
	fields = [
		"FleshCapColour",
		"FleshCapBruiseColour", 
		"FleshCapCutColour", 
		"FleshStipeColour",
		"FleshStipeBruiseColour", 
		"FleshStipeCutColour", 
		"Comments" 
	]
	template_name = 'flesh_form.html'

class ClassificationUpdate(UpdateView):
	model = Classification
	fields = [
		"Kingdom", 
		"Phyum", 
		"SubPhyum", 
		"Class", 
		"SubClass", 
		"Order", 
		"Family", 
		"Genus" 
]
	template_name = 'classification_form.html'

class SeasonsUpdate(UpdateView):
	model = Seasons
	fields = ['Season', 'Comments']
	template_name = 'seasons_form.html'

class NetLinksUpdate(UpdateView):
	model = NetLinks
	fields = []
	template_name = 'netlinks_form.html'

class SimilarFungiUpdate(UpdateView):
	model = SimilarFungi
	fields = ['SimilarFungiId','SimilarFungiName']
	template_name = 'similarfungi_form.html'

class StatusUpdate(UpdateView):
	model = Status
	fields = [
		"StatusData", 
		"WhereFound", 
		"RecordedInUK", 
		"UKOccurences",
		"StatusComments"
]
	template_name = 'status_form.html'

class DetailSourcesUpdate(UpdateView):
	model = DetailSources
	fields = []
	template_name = 'detailsources_form.html'