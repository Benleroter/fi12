from fungi.models import *


def FungiChoices():
	FCL =[]
	FChoices = Fungi.objects.all().distinct()
	Data = ('NoData', 'NoData')
	FCL.append(Data)
	for i in FChoices:
		data = (i.CommonName, i.CommonName)
		FCL.append(data)
	return FCL

def FungiChoices2():
	FCL2 =[]
	FChoices = Fungi.objects.all().distinct()
	for i in FChoices:
		data = (i.id, i.CommonName+', '+str(i.id))
		FCL2.append(data)
	return FCL2

#from fungi.models import *
def LinkChoicesNames():
	LinkChoices =[]
	FChoices = NetLinks.objects.all().distinct()
	for i in Fchoices:
		data=(i.Website)
		LinkChoices.append(data)
	return LinkChoices




ReticulationChoices= [
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]

PoresPresentChoices = [
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]

GillsPresentChoices = [
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]

PoresMilkChoices = [
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]

RecordedInUKChoices = [	
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]


GillsMilkChoices = [
	("initial", ""),
	("Yes", "Yes"),
	("No", "No")
	]	



MonthFoundChoices= [
	("initial", ""),
    ("January" , "January"),
	("February" , "February"),
	("March" , "March"),
	("April" , "April"),
	("May" , "May"),
	("June" , "June"),
	("July" , "July"),
	("August" , "August"),
	("September" , "September"),
	("October" , "October"),
	("November" , "November"),
	("December" , "December"),
	("Spring","Spring"),
	("Summer", "Summer"),
	("Autumn","Autumn"),
	("Winter","Winter"),
	("Other", "Other")
    ]

CapTextureChoices = [
	("initial", ""),
	("Smooth", "Smooth"),
	("Various", "Various"),
	("Sticky", "Sticky"),
	("Velvety", "Velvety"),
	("Cracking", "Cracking"),
	("Zoned", "Zoned"),
	("Slimy", "Slimy"),
	("Fibrillose", "Fibrillose"),
	("Scaly", "Scaly"),
	("Granular, ", "Granular"),
	("Shaggy", "Shaggy"),
	("Wrinkled", "Wrinkled"),
	("Striate,", "Striate"),
	("Downy", "Downy")
	]

StipeRingChoices = [ 
	("initial", ""),
	("Yes", "Yes"),
	("No", "No"),
	("Ascending", "Ascending"),
	("Detachable", "Detachable"),
	("Descending", "Descending")
	]

CapRimChoices = [
	("initial", ""),
	("Ribbed/notched","Ribbed/notched"),
	("Long_grooves","Long_grooves"),
	("Short_grooves","Short_grooves"),
	("Fringed","Fringed"), 
	("Wavy", "Wavy"), 
	("Other", "Other")
	]

StipeTextureChoices = [
	("initial", ""),
	("Other", "Other"),
	("Various","Various"),
	("Shaggy","Shaggy"),
	("Reticulation","Reticulation"),
	("Fibrillose","Fibrillose"),
	("Scaly","Scaly"),
	("Smooth","Smooth"),
	("Snakeskin","Snakeskin")
	]

PhTypeChoices = [
	("initial", ""),
	("acidic", "acidic"),
	("alkaline", "alkaline"),
	("neutral", "neutral"),
	("Other", "Other"),
	("NoData", "NoData")
	]

StipeBaseChoices = [
	("initial", ""),
	("Various","Various"),
	("Tapering","Tapering"),
	("Rooting","Rootmg"),
	("Spindle","Spindle"),
	("Volva","Volva"),
	("Bulbous","Bulbous"),
	("Club_Shaped","Club_Shaped"),
	("NoData", "NoData")
	]


AttachmentChoices = [
		("initial", ""),
		("Free","Free"),
		("Distant_from_stem","Distant_from_stem"),
		("Adnate","Adnate"),
		("Adnexed","Adnexed"),
		("Decurrent","Decurrent"),
		("Sinuate","Sinuate"),
		("NoData", "NoData")
        ]

ArrangementChoices = [
		("initial", ""),
		("Crowded","Crowded"),
		("Distant","Distant"),
		("Forked","Forked"),
		("Different_lengths","Different_lengths"),
		("Decurrent","Decurrent"),
		("Sinuate","Sinuate"),
		("NoData", "NoData")
        ]

CulinaryRatingChoices = [
		("initial", ""),
		("deadly","deadly"),
		("dangerous","dangerous"),
		("not_good","not_good"),
		("excellent","excellent"),
		("good","good"),
		("edible","edible"),
		("Unknown","Unknown"),
		("other","other"),
		("Differing opinions","Differing opinions"),
		("NoData", "NoData")
		] 

RUK= [
		("initial", ""),
		("Yes","Yes"),
		("No","No"),
		("NoData", "NoData")
		]