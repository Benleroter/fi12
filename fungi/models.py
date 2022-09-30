from django.db import models
from django.contrib.auth.models import User
#from PIL.Image import Image
import PIL.Image
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models import signals
#from fungi.views import choices

GillsPresentChoices = [
	("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
]

UKSpeciesChoices = [
	("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
]

MacromycetesChoices = [
	("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
]
PoresPresentChoices = [
	("NoData","NoData"),
	("Yes", "Yes"),
	("No", "No")
	]

RingPresentChoices = [
	("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
	]

MilkPresentChoices = [
    ("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
	]

RecordedInUKChoices = [
    ("NoData", "NoData"),
	("Yes", "Yes"),
	("No", "No")
	]


ReferenceSourceDetailChoices = [
	("Habitat", "Habitat"),
	("FruitingBody", "FruitingBody"),
	("Stipe","Stipe"),
	("Cuisine","Cuisine"),
	("Flesh","Flesh"),
	("SimilarFungi","SimilarFungi"),
	("OtherCommonNames","OtherCommonNames"),
	("LatinSynonyms","LatinSynonyms"),
	("Spores","Spores"),
	("Seasons","Seasons"),
	("Status","Status"),
	("PoresAndTubes","PoresAndTubes"),
	("Gills","Gills"),
	("Comments","Comments"),
	("Classification","Classification")


]


class Fungi(models.Model):
	CommonName = models.CharField(max_length=255, blank=False, null=False,default='Common Name')
	LatinName = models.CharField(max_length=255, blank=False, null=False,default='Latin Name')
	#BMSList = models.CharField(max_length=8,blank=True,null=True, default='BMS')
	#NBNList = models.CharField(max_length=8,blank=True,null=True, default='NBN')
	#GenusEnglish =  models.CharField(max_length=255,blank=True,null=True, default='NoData')
	#GenusLatin =  models.CharField(max_length=255,blank=True,null=True, default='NoData')
	#UKSpecies = models.CharField(max_length=8,blank=True,null=True, default='NoData')
	UKSpecies = models.CharField(max_length=20, choices=UKSpeciesChoices, blank=True, null=True, default='Yes', verbose_name='Recorded in UK')
	Macromycetes = models.CharField(max_length=8, choices=MacromycetesChoices,  blank=True,null=True, default='Yes')
	Group = models.CharField(max_length=255,blank=True,null=True, default='not assigned')
	Comments = models.CharField(max_length=1024,blank=True,null=True, default='NoData')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Fungi'
		verbose_name = "Fungi"
		verbose_name_plural = "Fungi"
		#ordering = ['LatinName']

		app_label  = "fungi"

	def __str__(self):
		return self.CommonName+", "+self.LatinName+', ID:'+str(self.id)

	'''
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi)
		return super().save(*args, **kwargs)
	'''
	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})


	#def get_absolute_url(self):
	#	return  reverse('FungiDetail-Page', kwargs={'pk': self.pk})

	#Following function creates all child records with default data
	def save(self, *args, **kwargs):
		is_new = not self.pk
		super().save(*args, **kwargs)
		if is_new:
			#print('self.id', self.id)
			OtherCommonNames.objects.create(Fungi=self)
			LatinSynonyms.objects.create(Fungi=self)
			FruitingBody.objects.create(Fungi=self)
			Stipe.objects.create(Fungi=self)
			PoresAndTubes.objects.create(Fungi=self)
			Gills.objects.create(Fungi=self)
			Spores.objects.create(Fungi=self)
			Picture.objects.create(Fungi=self)
			Habitat.objects.create(Fungi=self)
			Cuisine.objects.create(Fungi=self)
			Flesh.objects.create(Fungi=self)
			Classification.objects.create(Fungi=self)
			Seasons.objects.create(Fungi=self)
			NetLinks.objects.create(Fungi=self)
			SimilarFungi.objects.create(Fungi=self)
			Status.objects.create(Fungi=self)
			FungiComments.objects.create(Fungi=self) 
			DetailSources.objects.create(Fungi=self)

			if not self.slug:
				#print('not.slug')
				self.slug = slugify(self.id)
			#print('self.id', self.id)
			return super().save(*args, **kwargs)

class DetailSources(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_detail_sources')
	Source = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Detail = models.CharField(max_length=255, choices = ReferenceSourceDetailChoices, blank=True,null=True, default='NoData')
	#Detail = models.CharField(max_length=255, blank=True, null=True, default='NoData')

	class Meta:
		managed = True
		db_table =  'DetailSource'
		verbose_name = "DetailSources"
		verbose_name_plural = "DetailSources"	
		ordering = ['Fungi']
		app_label  = "fungi"
	def __str__(self):
		return self.Fungi.CommonName+', '+self.Source+', '+self.Detail
		#return self.Fungi.CommonName

class SimilarFungi(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_similar')
	SimilarFungiId = models.IntegerField(blank=True,  verbose_name='Similar Fungi id', null=True, default=0)
	SimilarFungiName = models.CharField(max_length=255, verbose_name='Similar Fungi Name',blank=True, null=True, default='NoData')
	slug = models.SlugField(null=True)    

	class Meta:
		managed = True
		db_table =  'SimilarFungi'
		verbose_name = "SimilarFungi"
		verbose_name_plural = "SimilarFungi"	
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return str(self.Fungi.id)+' , '+self.Fungi.CommonName+','+self.SimilarFungiName+','+str(self.SimilarFungiId)  

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})
		#return  reverse('FungiDetail-Page', kwargs={'Fungi_id': self.Fungi_id})


class LatinSynonyms(models.Model):
#class OtherLatinNames(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_latinnname')

	#SourceLinks = models.ForeignKey(DetailSources,max_length=255, blank=True, null=True, on_delete=models.CASCADE, related_name='SourcesLinks_LatinSynonyms')
	LatinSynonym = models.CharField(max_length=255, blank=True, null=True, verbose_name='Synonym', default='NoData')
	LatinSynonymSource = models.CharField(max_length=255, blank=True, null=True, verbose_name='Source', default='NoData')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		#db_table = 'OtherLatinNames'
		db_table = 'LatinSynonyms'
		verbose_name = "Latin Synonym"
		verbose_name_plural = "Latin Synonyms" 
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', '+self.LatinSynonym

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})
		#return  reverse('FungiDetail-Page', kwargs={'Fungi_id': self.Fungi_id})

class FungiComments(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_comments')
	Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'FungiComments'
		verbose_name = 'FungiComments'
		verbose_name_plural = 'FungiComments'
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', Comments: '+self.Comments


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})
		#return  reverse('FungiDetail-Page', kwargs={'Fungi_id': self.Fungi_id})



class Seasons(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_seasons')
	Season = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Seasons'
		verbose_name = 'Seasons'
		verbose_name_plural = 'Seasons'
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+", "+self.Season

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})
		#return  reverse('FungiDetail-Page', kwargs={'Fungi_id': self.Fungi_id})






class Habitat(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_habitat')
	Associations = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Ph = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Soil = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Substrate = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Environment = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Habitat'
		verbose_name = "Habitat"
		verbose_name_plural = "Habitats"
		ordering = ['Fungi']
		app_label  = "fungi"
		
	def __str__(self):
		return self.Fungi.CommonName+", "+self.Associations+', '+"Fungi_ID:"+str(self.Fungi.id)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})


class FruitingBody(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_fruitingbody')
	#SourceLinks = models.ForeignKey(DetailSources,max_length=255, blank=True, null=True, on_delete=models.CASCADE, related_name='SourcesLinksUrl_fruitingbody')
	#DataPresent = models.BooleanField(default=False)
	Colour  = models.CharField(max_length=1028, blank=True, default='NoData', null=True)
	#ColourDescription = models.CharField(max_length=1028, blank=True, default='NoData', null=True)
	#ShapeDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Shape = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Rim = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	#RimDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CapTexture= models.CharField(max_length=255, blank=True, default='NoData', null=True)
	#CapTextureDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	WidthMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
	WidthMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)
	
	class Meta:
		managed = True
		db_table = 'FruitingBody'
		verbose_name = "FruitingBody"
		verbose_name_plural = "FruitingBodies"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return str(self.Fungi)+', WidthMin:'+str(self.WidthMin)+', WidthMax:'+str(self.WidthMax)+', colour: '+self.Colour+', id:'+str(self.Fungi.id)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})



class Stipe(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Stipe')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	LengthMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
	LengthMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)#
	ThicknessMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
	ThicknessMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
	ShapeDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Shape = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	ReticulationPresent = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	ReticulationColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	ReticulationDescription = models.CharField(max_length=2048, blank=True, null=True, default='NoData')	
	Base = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	BaseDescription = models.CharField(max_length=255, blank=True, default='NoData', null=True)
	Texture = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	TextureDescription= models.CharField(max_length=255, blank=True, null=True, default='NoData')
	#Ring = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Ring = models.CharField(max_length=20, choices=RingPresentChoices, blank=True, null=True, default='NoData')
	RingDescription = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	slug = models.SlugField(null=True)

	Volva = models.CharField(max_length=255, blank=True, default='NoData', null=True)



	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

	class Meta:
		managed = True
		db_table = 'Stipe'
		verbose_name = "Stipe"
		verbose_name_plural = "Stipes"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return str(self.Fungi)+', LM:'+str(self.LengthMax)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})





class PoresAndTubes(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_pores')
	#PoresPresent = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	PoresPresent = models.CharField(max_length=20, choices = PoresPresentChoices, blank=True,null=True, default='No')
	PoreColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	PoreShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	PoreBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	TubeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	#Milk = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Milk = models.CharField(max_length=20, choices=MilkPresentChoices, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'PoresAndTubes'
		verbose_name = "Pores and Tubes"
		verbose_name_plural = "Pores and Tubes"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName     

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class Gills(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_gills')
	GillsPresent = models.CharField(max_length=20, choices = GillsPresentChoices, blank=True,null=True, default='No')
	#GillsPresent = models.CharField(max_length=255, blank=True,null=True, default='NoData')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	BruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	CutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Attachment = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Arrangement = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Milk = models.CharField(max_length=20, choices=MilkPresentChoices, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Gills'
		verbose_name = "Gills"
		verbose_name_plural = "Gills"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+", Colour: "+self.Colour   

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})




class Flesh(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_flesh')
	FleshCapColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshCapBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshCapCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	FleshStipeCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Flesh'
		verbose_name = 'Flesh'
		verbose_name_plural = 'Flesh'
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class Spores(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_spores')
	Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Spores'
		verbose_name = "Spores"
		verbose_name_plural = "Spores"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+", spore print colour: "+self.Colour   

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class NetLinks(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_netlinks')
	Website = models.CharField(max_length=255, verbose_name='Site Name', blank=True, null=True, default='NoData')
	#Website = models.CharField(max_length=255, verbose_name='Site Name', choices=LinkChoicesNames(), blank=True, null=True, default='NoData')
	Websiteurl = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True, default='NoData')
	OrderToDisplay = models.IntegerField(blank=True, null=True, default=50)

	class Meta:
		managed = True
		db_table = 'NetLinks'
		verbose_name = "NetLinks"
		verbose_name_plural = "NetLinks"
		ordering = ['OrderToDisplay']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', '+self.Fungi.LatinName+', '+self.Website

class OtherCommonNames(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_commonname')
	AltCommonName = models.CharField(max_length=255, blank=True, verbose_name='', null=True, default='NoData')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table =  'OtherCommonNames'
		verbose_name = "Other Common Name"
		verbose_name_plural = "Other Common Names"	
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', '+self.AltCommonName  

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})


class Classification(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_taxonomy')
	#SourceLinks = models.ForeignKey(DetailSources,max_length=255, blank=True, null=True, on_delete=models.CASCADE, related_name='SourcesLinks_Classification')
	Kingdom = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Phyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	SubPhyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Class = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	SubClass = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Order = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Family = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	Genus = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	#Source = models.CharField(max_length=255, blank=False, null=False, default='NoData')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Classification'
		verbose_name = "Classification"
		verbose_name_plural = "Classification"
		ordering = ['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+", "+self.Fungi.LatinName+", "+self.Phyum+", "+self.Class+", "+self.Order+", "+self.Family+", "+self.Genus

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class Cuisine(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_cuisine')
	PoisonType = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	CulinaryRating = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Odour = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Taste = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Cuisine'
		verbose_name = 'Cuisine'
		verbose_name_plural = 'Cuisine'
		ordering =['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+", "+"Culinary rating: "+self.CulinaryRating

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class Picture(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_picture')
	image = models.ImageField(default='default.jpg', upload_to='images')
	
	class Meta:
		managed = True
		db_table = 'Pictures'
		verbose_name = "Picture"
		verbose_name_plural = "Pictures"
		ordering =['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', '+self.image.path

	def save(self, *args, **kwargs):
		super(Picture, self).save(*args, **kwargs)
		
		#fp = open("/pdf-ex/downloadwin7.png","rb")
		#img = PIL.Image.open(fp)
		#img.show()

		#image=PIL.Image.open('/home/pi/Desktop/scene.jpg')   #use this 
		#img = Image.open(self.image.path)
		
		img = PIL.Image.open(self.image.path)

		#if img.height > 20 or img.width > 20:
		output_size = (350, 350)
		img.thumbnail(output_size)
		img.save(self.image.path)

class Status(models.Model):
	Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Status')
	StatusData = models.CharField(max_length=255,blank=True,null=True, verbose_name='Status', default='NoData')
	WhereFound = models.CharField(max_length=255,blank=True,null=True,verbose_name='Where found', default='NoData')
	#RecordedInUK = models.CharField(max_length=255,blank=True,choices=RecordedInUKChoices,null=True, default='NoData')
	#UKOccurences = models.CharField(max_length=16, blank=True, null=True, default='0')
	StatusComments = models.CharField(max_length=2048, blank=True, null=True,verbose_name='Comments', default='no comments')
	slug = models.SlugField(null=True)

	class Meta:
		managed = True
		db_table = 'Status'
		verbose_name = 'Status'
		verbose_name_plural = 'Status'
		ordering =['Fungi']
		app_label  = "fungi"

	def __str__(self):
		return self.Fungi.CommonName+', status: '+self.StatusData+', Mainly found in: '+self.WhereFound

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.Fungi_id)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('FungiDetail-Page', kwargs={'slug':self.slug})

class Glossary(models.Model):
	Term = models.CharField(max_length=50,blank=True,null=True, default='NoData')
	term_lower_case = models.CharField(max_length=50,blank=True,null=True, verbose_name='term lc', default='NoData')
	Meaning = models.CharField(max_length=255,blank=True,null=True, default='NoData')
	slug = models.SlugField(null=True)
	Source =  models.CharField(max_length=255,blank=True,null=True, default='NoData')

	class Meta:
		managed = True
		db_table = 'Glossary'
		verbose_name = 'Glossary'
		verbose_name_plural = 'Glossary'
		ordering =['Term']
		app_label  = "fungi"

	def __str__(self):
		return 'Term: '+self.Term+', Meaning: '+self.Meaning+', slug:'+self.slug

	def get_absolute_url(self):
		return reverse('glossary_entry', kwargs={'slug': self.slug}) # new
		#return  reverse('FungiDetail-Page', kwargs={'pk': self.Fungi.pk})
		#return reverse('FungiDetail-Page', kwargs={'Term': self.Term}) # new
