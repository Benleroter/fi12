from django.contrib import admin
from .models import Show, ShowSearchFields, UserModes, ShowGroup

admin.site.register(Show)
admin.site.register(ShowSearchFields)
admin.site.register(UserModes)
admin.site.register(ShowGroup)
