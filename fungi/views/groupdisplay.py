from django.shortcuts import render
from django import forms 
from fungi.views.choices import *
from fungi.models import Fungi
from fungi.forms import  GroupForm


#GROUP
GroupList = []
PID =Fungi.objects.order_by('Group').values('Group').distinct()
for i in PID:
    #print('i',i['Group'])
    GroupList.append(i['Group'])

#print('GroupList:',GroupList)

def GroupToDisplay(request):
    GroupSelection = {}
    GroupList = []
    PID =Fungi.objects.order_by('Group').values('Group').distinct()
    for i in PID:
    #print('i',i['Group'])
        GroupList.append(i['Group'])
    for p in GroupList:
            print('pppp:', p)
            GroupSelection['Group'] = forms.CharField(required=False, max_length=255, label=p, initial=False)
            #print('GroupSelection[Group]',GroupSelection)
    DynamicSearchForm = type('DynamicSearchForm', (GroupForm,), GroupSelection)
    form = DynamicSearchForm(request.POST)
    if form.is_valid():
        context = {
            'GroupSelection': GroupSelection ,
        }

        return render(request, 'groups.html', context)
    #return GroupSelection

