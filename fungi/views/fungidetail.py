from django.views.generic import DetailView
from usersettings.models import Show
# from fungi.models import Fungi
from fungi.models import *
# from django.db.models import Q
from django.contrib.auth.models import User  # AnonymousUser
# from bs4 import BeautifulSoup
# from bs4.element import NavigableString
# import re
# from django.utils.safestring import mark_safe
# from django.template import Context, Template
# import collections
from fungi.views.insertlinks import InsertLinks


class FungiDetail(DetailView):
    model = Fungi
    template_name = 'detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(FungiDetail, self).get_context_data(**kwargs)
        CurrentFungi = context['fungi']

        def DataPresent(Fungi_attribute):
            count = 0
            DP = 'True'
            context_var = [f for f in Fungi_attribute._meta.get_fields() if f.name not in ['id', 'DataPresent', 'Fungi', 'slug']]
            for i in context_var:
                count += count
                field_value = getattr(Fungi_attribute, i.name, None)
                if field_value == None:
                    field_value = 'NoData'
                if field_value == 'NoData' or field_value == 0.00 or field_value == 'no comments' or field_value == 'NoData' or field_value == 0 or field_value == '0':
                    DP = False
                else:
                    DP = 'True'
                    break
            return DP

        #retrieving user id's to get filter preferences

        if self.request.user.is_authenticated:
            U = self.request.user
            #uid = request.user
            print('uid-0', U)
            UserShowSettings = Show.objects.get(user_id=U.id)
        else:
            U = User.objects.get(username='GuestUser')
            print('uid-1', U)
            UserShowSettings = Show.objects.get(user_id=U.id)

        #LINKS
        RetrievedObjects = NetLinks.objects.filter(Fungi_id= self.object).distinct().order_by('OrderToDisplay')
        if RetrievedObjects:
            context['NetLinks'] = RetrievedObjects

        #PICTURES
        RetrievedObjects = Picture.objects.get(Fungi_id= self.object)
        context['Picture'] = RetrievedObjects

        #HABITAT
        HabitatSourcesList = []
        PID = Habitat.objects.get(Fungi_id= self.object)
        print('PID, Habitat: ', PID)
        if DataPresent(PID):
            DataToDisplay = False
            context['ShowHabitatFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowHabitat:
                RetrievedObjects = Habitat.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Habitat":
                        HabitatSourcesList.append(i.Source)
                context['HabitatSourcesList'] = HabitatSourcesList
                #print('context....RetrievedObjects.Associations:::', RetrievedObjects.Associations)
                #print('context....Associations::::', context['Associations'])


                if RetrievedObjects.Associations == 'NoData':
                   context['Associations'] = RetrievedObjects.Associations
                else:
                    context['Associations'] = InsertLinks(RetrievedObjects.Associations)[0]
                    context['AssociationsLinks'] = InsertLinks(RetrievedObjects.Associations)[1]
                    #print('context....Associations::::', context['Associations'])

                #print('context....RetrievedObjects.AssociationsXXX:::', RetrievedObjects.Associations)

                context['Ph'] = RetrievedObjects.Ph

                if RetrievedObjects.Soil == 'NoData':
                    context['Soil'] = RetrievedObjects.Soil
                else:
                    context['Soil'] = InsertLinks(RetrievedObjects.Soil)[0]
                    context['SoilLinks'] = InsertLinks(RetrievedObjects.Soil)[1]

                if RetrievedObjects.Substrate == 'NoData':
                    context['Substrate'] = RetrievedObjects.Substrate
                else:
                    context['Substrate'] = InsertLinks(RetrievedObjects.Substrate)[0]
                    context['SubstrateLinks'] = InsertLinks(RetrievedObjects.Substrate)[1]
                    #print('context....Substrate::::', context['Substrate'])

                #print('context....RetrievedObjects.SubstrateXXXXXX:::', RetrievedObjects.Substrate)

                if RetrievedObjects.Environment == 'NoData':
                    context['Environment'] = RetrievedObjects.Environment
                else:
                    context['Environment'] = InsertLinks(RetrievedObjects.Environment)[0]
                    context['EnvironmentLinks'] = InsertLinks(RetrievedObjects.Environment)[1]

                if RetrievedObjects.Comments == 'no comments':
                    context['HabitatComments'] = RetrievedObjects.Comments
                else:
                    context['HabitatComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['HabitatCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowHabitatFlag'] = 'Yes'
                context['DataToDisplay'] = True
            else:
                context['ShowHabitatFlag'] = 'No'

            #print('context....Associations::::',  context['Associations'])

        #FUNGI COMMENTS
        print('self.object. FungiComments', self.object)
        FungiCommentsSourcesList = []
        PID = FungiComments.objects.get(Fungi_id= self.object)
        #print('PID, FungiComments: ', PID)
        #print('DataPresent(PID)11111111', DataPresent(PID))
        if DataPresent(PID):
            print('DataPresent(PID)2222222222', DataPresent(PID))
            context['FungiCommentsFlag'] = 'Yes'
            #print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            if UserShowSettings.ShowFungiComments:
                RetrievedObjects = FungiComments.objects.get(Fungi_id= self.object)
                print('RetrievedObjects:', RetrievedObjects)
                #print('Fungi_id:::', Fungi.id)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', i.Detail)
                    #print('iiiiiiiiiiiiiii', i)
                    #if i.Detail == "FungiComments":
                    if i.Detail == "Comments":    
                        FungiCommentsSourcesList.append(i.Source)
                        #print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', i.Detail)
                context['FungiCommentsSourcesList'] = FungiCommentsSourcesList
                #print('FungiComments, RetrievedObjects', RetrievedObjects)

                if RetrievedObjects.Comments == 'no comments':
                    context['FungiComments'] = RetrievedObjects.Comments
                else:
                    context['FungiComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['FungiCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                #print('context[FungiComments] ', context['FungiComments'] )

                context['FungiCommentsFlag'] = 'Yes'
                #print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
                context['DataToDisplay'] = True
            else:
                context['FungiCommentsFlag'] = 'No'
                print('AAAAAAAAAAA')
        else:
            context['FungiCommentsFlag'] = 'No'
            #print('BBBBBBBBBBBB')

        #print('context[FungiCommentsFlag]KKKKK',context['FungiCommentsFlag'])

        #DETAILSOURCES
        PID = DetailSources.objects.filter(Fungi_id= self.object).first()
        #If DetailSources have all been deleted need default 'NoData' record in DB
        if PID == None:
            DetailSources.objects.create(Fungi=CurrentFungi)
            PID = DetailSources.objects.filter(Fungi_id= self.object).first()

        if DataPresent(PID):
            context['DetailSourcesFlag'] = 'Yes'
            if UserShowSettings.DetailSources:
                RetrievedObjects = DetailSources.objects.filter(Fungi_id= self.object)
                context['refcount']=RetrievedObjects.count
                context['DetailSourcesFlag'] ='Yes'
                context['DataToDisplay'] = 'True'
            else:
                context['DetailSourcesFlag'] = 'No'
        else:
            context['DetailSourcesFlag'] = 'No'

        #COMMONNAMES
        OtherCommonNamesSourcesList = []
        PID = OtherCommonNames.objects.filter(Fungi_id= self.object).first()
        #If Common Names have all been deleted need default 'NoData' record in DB
        if PID == None:
            print('PID == None:')
            OtherCommonNames.objects.create(Fungi=CurrentFungi)
            PID = OtherCommonNames.objects.filter(Fungi_id= self.object).first()

        #print('PID, OtherCommonNames: ', PID)
        if DataPresent(PID):
            context['ShowCommonNameFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowOtherCommonNames:
                RetrievedObjects = OtherCommonNames.objects.filter(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "OtherCommonNames":
                        OtherCommonNamesSourcesList.append(i.Source)
                context['OtherCommonNamesSourcesList'] = OtherCommonNamesSourcesList
                #print('OtherCommonNames, RetrievedObjects', RetrievedObjects)
                if RetrievedObjects:
                    context['OtherCommonNames'] = RetrievedObjects
                    context['ShowCommonNameFlag'] = 'Yes'
                else:
                    context['ShowCommonNameFlag'] = 'No'
        else:
            context['ShowCommonNameFlag'] = 'No'

        #GROUP
        GroupList = []
        PID =Fungi.objects.order_by('Group').values('Group').distinct()
        for i in PID:
            #print('i',i['Group'])
            GroupList.append(i['Group'])

        #SIMILARTO
        SimilarFungiSourcesList = []
        PID = SimilarFungi.objects.filter(Fungi_id= self.object).first()
        #If Similar Fungi have all been deleted need default 'NoData' record in DB
        if PID == None:
            SimilarFungi.objects.create(Fungi=CurrentFungi)
            PID = SimilarFungi.objects.filter(Fungi_id= self.object).first()

        if DataPresent(PID):
            context['ShowSimilarFungiFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSimilarFungi:
                RetrievedObjects = SimilarFungi.objects.filter(Fungi_id= self.object).distinct()
                #print('SimilarFungi: RetrievedObjects',RetrievedObjects)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "SimilarFungi":
                        SimilarFungiSourcesList.append(i.Source)
                        print('i.Source', i.Source)
                        print('i.Source-iii', i)
                context['SimilarFungiSourcesList'] = SimilarFungiSourcesList
                print('LatinSynonymsSourcesList-9999', SimilarFungiSourcesList)
                context['SimilarFungiNames'] = RetrievedObjects
                context['ShowSimilarFungiFlag'] = 'Yes'
            else:
                context['ShowSimilarFungiFlag'] = 'No'
        else:
            context['ShowSimilarFungiFlag'] = 'No'

        #LATIN SYNONYMS
        LatinSynonymsSourcesList = []
        PID = LatinSynonyms.objects.filter(Fungi_id= self.object).first()
        #If Latin Synonyms have all been deleted need default 'NoData' record in DB
        if PID == None:
            LatinSynonyms.objects.create(Fungi=CurrentFungi)
            PID = LatinSynonyms.objects.filter(Fungi_id= self.object).first()

        if DataPresent(PID):
            context['ShowLatinSynonymsFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowLatinSynonyms:
                RetrievedObjects = LatinSynonyms.objects.filter(Fungi_id= self.object).distinct()
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "LatinSynonyms":
                        LatinSynonymsSourcesList.append(i.Source)
                context['LatinSynonymsSourcesList'] = LatinSynonymsSourcesList
                context['LatinSynonyms'] = RetrievedObjects
                context['ShowLatinSynonymsFlag'] = 'Yes'
            else:
                context['ShowLatinSynonymsFlag'] = 'No'
        else:
            context['ShowLatinSynonymsFlag'] = 'No'

        #CLASSIFICATION
        ClassificationSourcesList = []
        PID = Classification.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Classification.objects.get(Fungi_id= self.object)):
            context['ShowClassificationFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowClassification:
                RetrievedObjects = Classification.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Classification":
                        ClassificationSourcesList.append(i.Source)
                context['ClassificationSourcesList'] = ClassificationSourcesList
                #print('ClassificationSourcesList-9999', ClassificationSourcesList)
                context['Kingdom'] = RetrievedObjects.Kingdom
                context['Phyum'] = RetrievedObjects.Phyum
                context['SubPhyum'] = RetrievedObjects.SubPhyum
                context['Class'] = RetrievedObjects.Class
                context['SubClass'] = RetrievedObjects.SubClass
                context['Order'] = RetrievedObjects.Order
                context['Family'] = RetrievedObjects.Family
                context['Genus'] = RetrievedObjects.Genus

                context['ShowClassificationFlag'] = 'Yes'
            else:
                context['ShowClassificationFlag'] = 'No'
        else:
            context['ShowClassificationFlag'] = 'No'

        #FRUITINGBODY
        FruitingBodySourcesList = []
        PID = FruitingBody.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowFruitingBodyFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowFruitingBody:
                RetrievedObjects = FruitingBody.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "FruitingBody":
                        FruitingBodySourcesList.append(i.Source)
                context['FruitingBodySourcesList'] = FruitingBodySourcesList
                #print('FruitingBodySourcesList-9999', ClassificationSourcesList)

                if RetrievedObjects.Colour == 'NoData':
                    context['CapColour'] = RetrievedObjects.Colour
                else:
                    context['CapColour'] = InsertLinks(RetrievedObjects.Colour)[0]
                    context['CapColourLinks'] = InsertLinks(RetrievedObjects.Colour)[1]

                #if RetrievedObjects.ShapeDescription == 'NoData':
                #   context['CapShapeDescription'] = RetrievedObjects.ShapeDescription
                #else:
                #   context['CapShapeDescription'] = InsertLinks(RetrievedObjects.ShapeDescription)[0]
                #   context['CapShapeDescriptionLinks'] = InsertLinks(RetrievedObjects.ShapeDescription)[1]


                if RetrievedObjects.Shape == 'NoData':
                    context['CapShape'] = RetrievedObjects.Shape
                else:
                    context['CapShape'] = InsertLinks(RetrievedObjects.Shape)[0]
                    context['CapShapeLinks'] = InsertLinks(RetrievedObjects.Shape)[1]

                if RetrievedObjects.Rim == 'NoData':
                    context['CapRim'] = RetrievedObjects.Rim
                else:
                    context['CapRim'] = InsertLinks(RetrievedObjects.Rim)[0]
                    context['CapRimLinks'] = InsertLinks(RetrievedObjects.Rim)[1]

                #if RetrievedObjects.RimDescription == 'NoData':
                #    context['CapRimDescription'] = RetrievedObjects.RimDescription
                #else:
                #   context['CapRimDescription'] = InsertLinks(RetrievedObjects.RimDescription)[0]
                #   context['CapRimDescriptionLinks'] = InsertLinks(RetrievedObjects.RimDescription)[1]

                if RetrievedObjects.CapTexture == 'NoData':
                    context['CapTexture'] = RetrievedObjects.CapTexture
                else:
                    context['CapTexture'] = InsertLinks(RetrievedObjects.CapTexture)[0]
                    context['CapTextureLinks'] = InsertLinks(RetrievedObjects.CapTexture)[1]

                #if RetrievedObjects.CapTextureDescription == 'NoData':
                #   context['CapTextureDescription'] = RetrievedObjects.CapTextureDescription
                #else:
                #   context['CapTextureDescription'] = InsertLinks(RetrievedObjects.CapTextureDescription)[0]
                #    context['CapTextureDescriptionLinks'] = InsertLinks(RetrievedObjects.CapTextureDescription)[1]

                if RetrievedObjects.BruiseColour == 'NoData':
                    context['CapBruiseColour'] = RetrievedObjects.BruiseColour
                else:
                    context['CapBruiseColour'] = InsertLinks(RetrievedObjects.BruiseColour)[0]
                    context['CapBruiseColourLinks'] = InsertLinks(RetrievedObjects.BruiseColour)[1]

                if RetrievedObjects.CutColour == 'NoData':
                    context['CapCutColour'] = RetrievedObjects.CutColour
                else:
                    context['CapCutColour'] = InsertLinks(RetrievedObjects.CutColour)[0]
                    context['CapCutColourLinks'] = InsertLinks(RetrievedObjects.CutColour)[1]




                if float(RetrievedObjects.WidthMin) > 0.00 and float(RetrievedObjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = float(RetrievedObjects.WidthMin)
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)
                if float(RetrievedObjects.WidthMin) == 0.00 and float(RetrievedObjects.WidthMax) == 0.00:
                    context['CapWidthMin'] = float(RetrievedObjects.WidthMin)
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)
                if float(RetrievedObjects.WidthMin) == 0.00 and float(RetrievedObjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = "up to"
                    context['CapWidthMax'] = float(RetrievedObjects.WidthMax)

                if RetrievedObjects.Comments == 'no comments':
                    context['CapComments'] = RetrievedObjects.Comments
                else:
                    context['CapComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['CapCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowFruitingBodyFlag'] = 'Yes'
            else:
                context['ShowFruitingBodyFlag'] = 'No'
        else:
            context['ShowFruitingBodyFlag'] = 'No'

        #STIPE
        StipeSourcesList = []
        PID = Stipe.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Stipe.objects.get(Fungi_id= self.object)):
            context['ShowStipeFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowStipe:
                RetrievedObjects = Stipe.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Stipe":
                        StipeSourcesList.append(i.Source)
                context['StipeSourcesList'] = StipeSourcesList
                #print('StipeSourcesList-9999', StipeSourcesList)
                #print('Stipe, RetrievedObjects', RetrievedObjects)

                if RetrievedObjects.Colour == 'NoData':
                    context['StipeColour'] = RetrievedObjects.Colour
                else:
                    context['StipeColour'] = InsertLinks(RetrievedObjects.Colour)[0]
                    context['StipeColourLinks'] = InsertLinks(RetrievedObjects.Colour)[1]

                if RetrievedObjects.Texture == 'NoData':
                    context['StipeTexture'] = RetrievedObjects.Texture
                else:
                    context['StipeTexture'] = InsertLinks(RetrievedObjects.Texture)[0]
                    context['StipeTextureLinks'] = InsertLinks(RetrievedObjects.Texture)[1]

                if RetrievedObjects.TextureDescription == 'NoData':
                    context['TextureDescription'] = RetrievedObjects.TextureDescription
                else:
                    context['TextureDescription'] = InsertLinks(RetrievedObjects.TextureDescription)[0]
                    context['TextureDescriptionLinks'] = InsertLinks(RetrievedObjects.TextureDescription)[1]

                if RetrievedObjects.BruiseColour == 'NoData':
                    context['StipeBruiseColour'] = RetrievedObjects.BruiseColour
                else:
                    context['StipeBruiseColour'] = InsertLinks(RetrievedObjects.BruiseColour)[0]
                    context['StipeBruiseColourLinks'] = InsertLinks(RetrievedObjects.BruiseColour)[1]

                if RetrievedObjects.CutColour == 'NoData':
                    context['StipeCutColour'] = RetrievedObjects.CutColour
                else:
                    context['StipeCutColour'] = InsertLinks(RetrievedObjects.CutColour)[0]
                    context['StipeCutColourLinks'] = InsertLinks(RetrievedObjects.CutColour)[1]

                if float(RetrievedObjects.ThicknessMin) > 0.00 and float(RetrievedObjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = float(RetrievedObjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)
                if float(RetrievedObjects.ThicknessMin) == 0.00 and float(RetrievedObjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = "up to"
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)
                if float(RetrievedObjects.ThicknessMin) == 0.00 and float(RetrievedObjects.ThicknessMax) == 0.00:
                    context['StipeThicknessMin'] =float(RetrievedObjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(RetrievedObjects.ThicknessMax)

                if RetrievedObjects.LengthMin > 0.00 and RetrievedObjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = round(RetrievedObjects.LengthMin,2)
                    context['StipeLengthMax'] = round(RetrievedObjects.LengthMax,2)
                if RetrievedObjects.LengthMin == 0.00 and RetrievedObjects.LengthMax == 0.00:
                    context['StipeLengthMin'] = round(RetrievedObjects.LengthMin,2)
                    context['StipeLengthMax'] = round(RetrievedObjects.LengthMax,2)
                if RetrievedObjects.LengthMin == 0.00 and RetrievedObjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = "up to"
                    context['StipeLengthMax'] = float(RetrievedObjects.LengthMax)

                if RetrievedObjects.ShapeDescription == 'NoData':
                    context['ShapeDescription'] = RetrievedObjects.ShapeDescription
                else:
                    context['ShapeDescription'] = InsertLinks(RetrievedObjects.ShapeDescription)[0]
                    context['ShapeDescriptionLinks'] = InsertLinks(RetrievedObjects.ShapeDescription)[1]

                if RetrievedObjects.Ring == 'NoData':
                    context['StipeRing'] = RetrievedObjects.Ring
                else:
                    context['StipeRing'] = InsertLinks(RetrievedObjects.Ring)[0]
                    context['StipeRingLinks'] = InsertLinks(RetrievedObjects.Ring)[1]

                if RetrievedObjects.RingDescription == 'NoData':
                    context['RingDescription'] = RetrievedObjects.RingDescription
                else:
                    context['RingDescription'] = InsertLinks(RetrievedObjects.RingDescription)[0]
                    context['RingDescriptionLinks'] = InsertLinks(RetrievedObjects.RingDescription)[1]

                context['Reticulation'] = RetrievedObjects.ReticulationPresent

                if RetrievedObjects.ReticulationColour == 'NoData':
                    context['ReticulationColour'] = RetrievedObjects.ReticulationColour
                else:
                    context['ReticulationColour'] = InsertLinks(RetrievedObjects.ReticulationColour)[0]
                    context['ReticulationColourLinks'] = InsertLinks(RetrievedObjects.ReticulationColour)[1]

                context['ReticulationDescription'] = RetrievedObjects.ReticulationDescription

                if RetrievedObjects.ReticulationDescription == 'NoData':
                    context['ReticulationDescription'] = RetrievedObjects.ReticulationDescription
                else:
                    context['ReticulationDescription'] = InsertLinks(RetrievedObjects.ReticulationDescription)[0]
                    context['ReticulationDescriptionLinks'] = InsertLinks(RetrievedObjects.ReticulationDescription)[1]

                if RetrievedObjects.Base == 'NoData':
                    context['Base'] = RetrievedObjects.Base
                else:
                    context['Base'] = InsertLinks(RetrievedObjects.Base)[0]
                    context['BaseLinks'] = InsertLinks(RetrievedObjects.Base)[1]

                if RetrievedObjects.BaseDescription == 'NoData':
                    context['BaseDescription'] = RetrievedObjects.BaseDescription
                else:
                    context['BaseDescription'] = InsertLinks(RetrievedObjects.BaseDescription)[0]
                    context['BaseDescriptionLinks'] = InsertLinks(RetrievedObjects.BaseDescription)[1]

                if RetrievedObjects.Comments == 'no comments':
                    context['StipeComments'] = RetrievedObjects.Comments
                else:
                    context['StipeComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['StipeCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowStipeFlag'] = 'Yes'
            else:
                context['ShowStipeFlag'] = 'No'
        else:
            context['ShowStipeFlag'] = 'No'

        #PORES
        PoresAndTubesSourcesList = []
        PID = PoresAndTubes.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(PoresAndTubes.objects.get(Fungi_id= self.object)):
            context['ShowPoresAndTubesFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowPoresAndTubes:
                RetrievedObjects = PoresAndTubes.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "PoresAndTubes":
                        PoresAndTubesSourcesList.append(i.Source)
                context['PoresAndTubesSourcesList'] = PoresAndTubesSourcesList
                #print('PoresAndTubesSourcesList-9999', PoresAndTubesSourcesList)
                context['PoresPresent'] = RetrievedObjects.PoresPresent


                if RetrievedObjects.PoreColour == 'NoData':
                    context['PoreColour'] = RetrievedObjects.PoreColour
                else:
                    context['PoreColour'] = InsertLinks(RetrievedObjects.PoreColour)[0]
                    context['PoreColourLinks'] = InsertLinks(RetrievedObjects.PoreColour)[1]

                if RetrievedObjects.PoreShape == 'NoData':
                    context['PoreShape'] = RetrievedObjects.PoreShape
                else:
                    context['PoreShape'] = InsertLinks(RetrievedObjects.PoreShape)[0]
                    context['PoreShapeLinks'] = InsertLinks(RetrievedObjects.PoreShape)[1]

                if RetrievedObjects.PoreBruiseColour == 'NoData':
                    context['PoreBruiseColour'] = RetrievedObjects.PoreBruiseColour
                else:
                    context['PoreBruiseColour'] = InsertLinks(RetrievedObjects.PoreBruiseColour)[0]
                    context['PoreBruiseColourLinks'] = InsertLinks(RetrievedObjects.PoreBruiseColour)[1]

                if RetrievedObjects.TubeColour == 'NoData':
                    context['TubeColour'] = RetrievedObjects.TubeColour
                else:
                    context['TubeColour'] = InsertLinks(RetrievedObjects.TubeColour)[0]
                    context['TubeColourLinks'] = InsertLinks(RetrievedObjects.TubeColour)[1]

                if RetrievedObjects.TubeShape == 'NoData':
                    context['TubeShape'] = RetrievedObjects.TubeShape
                else:
                    context['TubeShape'] = InsertLinks(RetrievedObjects.TubeShape)[0]
                    context['TubeShapeLinks'] = InsertLinks(RetrievedObjects.TubeShape)[1]

                if RetrievedObjects.TubeBruiseColour == 'NoData':
                    context['TubeBruiseColour'] = RetrievedObjects.TubeBruiseColour
                else:
                    context['TubeBruiseColour'] = InsertLinks(RetrievedObjects.TubeBruiseColour)[0]
                    context['TubeBruiseColourLinks'] = InsertLinks(RetrievedObjects.TubeBruiseColour)[1]

                context['PoreMilk'] = RetrievedObjects.Milk

                if RetrievedObjects.Comments == 'no comments':
                    context['PoreComments'] = RetrievedObjects.Comments
                else:
                    context['PoreComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['PoreCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowPoresAndTubesFlag'] = 'Yes'
            else:
                context['ShowPoresAndTubesFlag'] = 'No'
        else:
            context['ShowPoresAndTubesFlag'] = 'No'

        #GILLS
        GillsSourcesList = []
        PID = Gills.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Gills.objects.get(Fungi_id= self.object)):
            context['ShowGillsFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowGills:
                RetrievedObjects = Gills.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Gills":
                        GillsSourcesList.append(i.Source)
                context['GillsSourcesList'] = GillsSourcesList

                if RetrievedObjects.Colour == 'NoData':
                    context['GillsColour'] = RetrievedObjects.Colour
                else:
                    context['GillsColour'] = InsertLinks(RetrievedObjects.Colour)[0]
                    context['GillsColourLinks'] = InsertLinks(RetrievedObjects.Colour)[1]

                context['GillsPresent'] = RetrievedObjects.GillsPresent

                if RetrievedObjects.BruiseColour == 'NoData':
                    context['GillsBruiseColour'] = RetrievedObjects.BruiseColour
                else:
                    context['GillsBruiseColour'] = InsertLinks(RetrievedObjects.BruiseColour)[0]
                    context['GillsBruiseColourLinks'] = InsertLinks(RetrievedObjects.BruiseColour)[1]

                if RetrievedObjects.CutColour == 'NoData':
                    context['GillsCutColour'] = RetrievedObjects.CutColour
                else:
                    context['GillsCutColour'] = InsertLinks(RetrievedObjects.CutColour)[0]
                    context['GillsCutColourLinks'] = InsertLinks(RetrievedObjects.CutColour)[1]

                if RetrievedObjects.Attachment == 'NoData':
                    context['GillsAttachment'] = RetrievedObjects.Attachment
                else:
                    context['GillsAttachment'] = InsertLinks(RetrievedObjects.Attachment)[0]
                    context['GillsAttachmentLinks'] = InsertLinks(RetrievedObjects.Attachment)[1]

                if RetrievedObjects.Arrangement == 'NoData':
                    context['GillsArrangement'] = RetrievedObjects.Arrangement
                else:
                    context['GillsArrangement'] = InsertLinks(RetrievedObjects.Arrangement)[0]
                    context['GillsArrangementLinks'] = InsertLinks(RetrievedObjects.Arrangement)[1]

                context['GillsMilk'] = RetrievedObjects.Milk

                if RetrievedObjects.Comments == 'no comments':
                    context['GillsComments'] = RetrievedObjects.Comments
                else:
                    context['GillsComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['GillsCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowGillsFlag'] = 'Yes'
            else:
                context['ShowGillsFlag'] = 'No'
        else:
            context['ShowGillsFlag'] = 'No'

        #SPORES
        SporesSourcesList = []
        PID = Spores.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Spores.objects.get(Fungi_id= self.object)):
            context['ShowSporesFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSpores:
                RetrievedObjects = Spores.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Spores":
                        SporesSourcesList.append(i.Source)
                context['SporesSourcesList'] = SporesSourcesList
                #print('SporesSourcesList-9999', SporesSourcesList)

                if RetrievedObjects.Colour == 'NoData':
                    context['SporesColour'] = RetrievedObjects.Colour
                else:
                    context['SporesColour'] = InsertLinks(RetrievedObjects.Colour)[0]
                    context['SporesColourLinks'] = InsertLinks(RetrievedObjects.Colour)[1]

                if RetrievedObjects.Comments == 'no comments':
                    context['SporesComments'] = RetrievedObjects.Comments
                else:
                    context['SporesComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['SporesCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowSporesFlag'] = 'Yes'
            else:
                context['ShowSporesFlag'] = 'No'
        else:
            context['ShowSporesFlag'] = 'No'


        #FLESH
        FleshSourcesList = []
        PID = Flesh.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Flesh.objects.get(Fungi_id= self.object)):
            context['ShowFleshFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowFlesh:
                RetrievedObjects = Flesh.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Flesh":
                        FleshSourcesList.append(i.Source)
                        print('SOURCE',i.Source)
                context['FleshSourcesList'] = FleshSourcesList

                if RetrievedObjects.FleshCapColour == 'NoData':
                    context['FleshCapColour'] = RetrievedObjects.FleshCapColour
                else:
                    context['FleshCapColour'] = InsertLinks(RetrievedObjects.FleshCapColour)[0]
                    context['FleshCapColourLinks'] = InsertLinks(RetrievedObjects.FleshCapColour)[1]

                if RetrievedObjects.FleshCapBruiseColour == 'NoData':
                    context['FleshCapBruiseColour'] = RetrievedObjects.FleshCapBruiseColour
                else:
                    context['FleshCapBruiseColour'] = InsertLinks(RetrievedObjects.FleshCapBruiseColour)[0]
                    context['FleshCapBruiseColourLinks'] = InsertLinks(RetrievedObjects.FleshCapBruiseColour)[1]

                if RetrievedObjects.FleshCapCutColour == 'NoData':
                    context['FleshCapCutColour'] = RetrievedObjects.FleshCapCutColour
                else:
                    context['FleshCapCutColour'] = InsertLinks(RetrievedObjects.FleshCapCutColour)[0]
                    context['FleshCapCutColourLinks'] = InsertLinks(RetrievedObjects.FleshCapCutColour)[1]

                if RetrievedObjects.FleshStipeColour == 'NoData':
                    context['FleshStipeColour'] = RetrievedObjects.FleshStipeColour
                else:
                    context['FleshStipeColour'] = InsertLinks(RetrievedObjects.FleshStipeColour)[0]
                    context['FleshStipeColourLinks'] = InsertLinks(RetrievedObjects.FleshStipeColour)[1]

                if RetrievedObjects.FleshStipeBruiseColour == 'NoData':
                    context['FleshStipeBruiseColour'] = RetrievedObjects.FleshStipeBruiseColour
                else:
                    context['FleshStipeBruiseColour'] = InsertLinks(RetrievedObjects.FleshStipeBruiseColour)[0]
                    context['FleshStipeBruiseColourLinks'] = InsertLinks(RetrievedObjects.FleshStipeBruiseColour)[1]

                if RetrievedObjects.FleshStipeCutColour == 'NoData':
                    context['FleshStipeCutColour'] = RetrievedObjects.FleshStipeCutColour
                else:
                    context['FleshStipeCutColour'] = InsertLinks(RetrievedObjects.FleshStipeCutColour)[0]
                    context['FleshStipeCutColourLinks'] = InsertLinks(RetrievedObjects.FleshStipeCutColour)[1]

                if RetrievedObjects.Comments == 'no comments':
                    context['FleshComments'] = RetrievedObjects.Comments
                else:
                    context['FleshComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                    context['FleshCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]

                context['ShowFleshFlag'] = 'Yes'
            else:
                context['ShowFleshFlag'] = 'No'
        else:
            context['ShowFleshFlag'] = 'No'

        #STATUS
        StatusSourcesList = []
        PID = Status.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
        #if DataPresent(Status.objects.get(Fungi_id= self.object)):
            context['ShowStatusFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowStatus:
                RetrievedObjects =  Status.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Status":
                         StatusSourcesList.append(i.Source)
                context['StatusSourcesList'] = StatusSourcesList
                context['StatusData'] = RetrievedObjects.StatusData
                context['WhereFound'] = RetrievedObjects.WhereFound
                context['StatusComments'] = RetrievedObjects.StatusComments
                context['ShowStatusFlag'] = 'Yes'

            else:
                context['ShowStatusFlag'] = 'No'
        else:
            context['ShowStatusFlag'] = 'No'

        #SEASON
        SeasonsSourcesList = []
        PID = Seasons.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowSeasonFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowSeasons:
                RetrievedObjects = Seasons.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Seasons":
                        SeasonsSourcesList.append(i.Source)
                context['SeasonsSourcesList'] = SeasonsSourcesList
                #print('SeasonsSourcesList-9999', SeasonsSourcesList)
                if RetrievedObjects.Season != 'NoData':
                    From = RetrievedObjects.Season[0:RetrievedObjects.Season.index(',')]
                    To = RetrievedObjects.Season[(RetrievedObjects.Season.rfind(','))+1:len(RetrievedObjects.Season)]
                    FruitingSeason = From+' - '+To
                    context['FruitingSeason'] = FruitingSeason
                    context['SeasonComments'] = RetrievedObjects.Comments
                    context['ShowSeasonFlag'] = 'Yes'
            else:
                context['ShowSeasonFlag'] = 'No'
        else:
            context['ShowSeasonFlag'] = 'No'

        #CUISINE
        CuisineSourcesList = []
        PID = Cuisine.objects.filter(Fungi_id= self.object).first()
        if DataPresent(PID):
            context['ShowCuisineFlag'] = 'Yes'
            context['DataToDisplay'] = True
            if UserShowSettings.ShowCuisine:
                RetrievedObjects = Cuisine.objects.get(Fungi_id= self.object)
                for i in DetailSources.objects.filter(Fungi_id= self.object):
                    if i.Detail == "Cuisine":
                        CuisineSourcesList.append(i.Source)
                context['CuisineSourcesList'] = CuisineSourcesList
                #print('CuisineSourcesList-9999', CuisineSourcesList)
                #context['FleshComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                context['PoisonType'] = RetrievedObjects.PoisonType
                context['CulinaryRating'] = RetrievedObjects.CulinaryRating
                context['Odour']= RetrievedObjects.Odour
                context['Taste'] = RetrievedObjects.Taste
                context['CuisineComments'] = InsertLinks(RetrievedObjects.Comments)[0]
                context['CuisineCommentsLinks'] = InsertLinks(RetrievedObjects.Comments)[1]
                context['ShowCuisineFlag'] = 'Yes'
            else:
                context['ShowCuisineFlag'] = 'No'
        else:
            context['ShowCuisineFlag'] = 'No'

        #print('context....Associations::::', context['Associations'])
        #print('context....Substrate::::', context['Substrate'])
        if U.is_superuser:
            #print('User is superuser')
            context['DataToDisplay'] = True


        return context

