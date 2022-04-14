from django import forms
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth.models import User


UserGroupFormset = inlineformset_factory(
    User,
    ShowGroup,
    extra=0,
    labels='',
    can_delete=False,
    fields=('GroupCheck','Group')
    )

UserGroupAddFormset= inlineformset_factory(
    User,
    ShowGroup,
    extra=1,
    labels='',
    can_delete=True,
    fields=('Group',)
    )