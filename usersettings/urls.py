from django.urls import path
from django.conf.urls import url
from . import views
#from .views import (CreateFilter,FilterView,EditFilter,CreateSearchFilter,EditSearchFields,SearchFieldsView)
#from .views import (EditFilter,SearchFieldsEdit) *
from .views import *
from . import views

app_name = 'usersettings'

urlpatterns = [
	path('filterhome/', views.filtershome, name='Filter-HomePage'),
    #path('show/<int:pk>/', FilterView.as_view(), name='view-show-filters'),
    #path('show/new/', CreateFilter.as_view(), name='add-filter'),
    #path('show/<int:pk>/update/', EditFilter.as_view(), name='edit-show-filter'),
    path('detailstoshow/<int:pk>/update/', EditFilter.as_view(), name='edit-show-filter'),

    #path('show/new/', CreateSearchFilter.as_view(), name='add-search-fields'),
    #path('searchshowfields/<int:pk>/', SearchFieldsView.as_view(), name='view-search-fields'),
    path('editsearchfields/<int:pk>/update/', SearchFieldsEdit.as_view(), name='edit-search-fields'),
    path('setmodes/<int:pk>/update/', SetModes.as_view(), name='set_modes'),
    #path('setgroups/<int:pk>/update/', SetGroups.as_view(), name='set_groups'),

    path('setgroups/<int:pk>/groups/edit/', views.UserGroupsEditView.as_view(), name='user_groups_edit'),
    path('addsetgroups/<int:pk>/', views.UserGroupsAddView.as_view(), name='user_group_add'),
 ]

