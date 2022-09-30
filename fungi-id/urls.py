"""fungi-id URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from fungi import views
from fungi.views import *
from fungi.views.search import Search
from users  import views as user_views
from django.contrib.auth import views as auth_views
from usersettings.views import (EditFilter)
#from .views import ProductListView, ProductCreateView
#from fungi.views import FungiLatinSynonymsEditView

admin.autodiscover()
admin.site.enable_nav_sidebar = False

app_name = 'fungi-id'

urlpatterns = [


    path('', views.home, name='AllFungi-HomePage'),
    path('allfungi/', views.AllFungi, name='AllFungiList'),
    path('links/', views.Links, name='Links-Page'),
    path('about/', views.about, name='AllFungi-AboutPage'),
    path('home/', views.home, name='AllFungi-HomePage'),
    #path('detail/<int:pk>/', FungiDetail.as_view(), name='FungiDetail-Page'),
    path('detail/<int:slug>/', FungiDetail.as_view(), name='FungiDetail-Page'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('sources/', views.AllSources, name='DataSources'),
    path('allgroups/', views.AllGroups, name='fungi-group-list'),

    #UPDATING 
    path('fruitingbody/<int:slug>/update/', FruitingBodyUpdate.as_view(), name='fruitingbody-update'),
    path('habitat/<int:slug>/update/', HabitatUpdate.as_view(), name='habitat-update'),
    path('FungiComments/<int:slug>/update/',FungiCommentsUpdate.as_view(), name='fungicomments-update'),
    path('Stipe/<int:slug>/update/', StipeUpdate.as_view(), name='stipe-update'),
    path('PoresAndTubes/<int:slug>/update/', PoresAndTubesUpdate.as_view(), name='poresandtubes-update'),
    path('Gills/<int:slug>/update/', GillsUpdate.as_view(), name='gills-update'),
    path('Spores/<int:slug>/update/', SporesUpdate.as_view(), name='spores-update'),
    path('Cuisine/<int:slug>/update/', CuisineUpdate.as_view(), name='cuisine-update'),
    path('Flesh/<int:slug>/update/', FleshUpdate.as_view(), name='flesh-update'),
    path('Classification/<int:slug>/update/', ClassificationUpdate.as_view(), name='classification-update'),
    path('Seasons/<int:slug>/update/', SeasonsUpdate.as_view(), name='seasons-update'),
    path('Status/<int:slug>/update/', StatusUpdate.as_view(), name='status-update'),

    #path('OtherCommonNames/<int:slug>/update/', OtherCommonNamesUpdate.as_view(), name='othercommonnames-update'),
    #path('LatinSynonyms/<int:slug>/update/', LatinSynonymsUpdate.as_view(), name='latinsynonyms-update'),
    #path('SimilarFungi/<int:slug>/update/', SimilarFungiUpdate.as_view(), name='similarfungi-update'),

    path('NetLinks/<pk>/update/', NetLinksUpdate.as_view(), name='netlinks-update'),
    path('DetailSources/<pk>/update/', DetailSourcesUpdate.as_view(), name='detailssources-update'),    

    #path('LatinSynonyms/<pk>/', LatinSynomymsList.as_view(), name='latinsynonyms-list'),
    #path('LatinSynonyms/<pk>/', LatinSynonymsUpdate.as_view(), name='latinsynonyms-update'),
   
    path('fungi/<int:slug>/latinsynonyms/', views.FungiLatinSynomymsView.as_view(), name='fungi_latinsynonyms_edit_add'),
    path('fungi/<int:slug>/latinsynonyms/del/', views.FungiLatinSynomymsDeleteView.as_view(), name='fungi_latinsynonyms_del'),    

    path('fungi/<int:slug>/commonnames/', views.FungiCommonNamesView.as_view(), name='fungi_commonnames_edit_add'),
    path('fungi/<int:slug>/commonnames/del/', views.FungiCommonNamesDeleteView.as_view(), name='fungi_commonnames_del'),

    path('fungi/<int:slug>/similar/', views.FungiSimilarView.as_view(), name='fungi_similar_edit_add'),
    path('fungi/<int:slug>/similar/del/', views.FungiSimilarDeleteView.as_view(), name='fungi_similar_del'),

    path('fungi/<int:slug>/netlinks/', views.FungiLinksView.as_view(), name='fungi_netlinks_edit_add'),
    path('fungi/<int:slug>/netlinks/del/', views.FungiLinksDeleteView.as_view(), name='fungi_netlinks_del'),

    path('fungi/<int:slug>/refs/', views.FungiRefsView.as_view(), name='fungi_refs_edit_add'),
    path('fungi/<int:slug>/refs/del/', views.FungiRefsDeleteView.as_view(), name='fungi_refs_del'),

    path('groups/', GroupToDisplay, name='fungi-groups'),

    path('glossary/',ShowGlossary, name='glossary'),
    path('glossary/new', views.GlossaryTermView.as_view(), name='new_glossary_term'),
    path('glossary/<str:slug>/',ShowGlossaryEntry.as_view(), name='glossary_entry'),
    path('glossary/add', views.GlossaryFormView.as_view(), name='glossary_form'),


    path('fungi/', views.FungiListView.as_view(), name='list_fungi'),
    #path('fungi/<int:pk>/', views.FungiEditView.as_view(), name='fungi_edit'),
    
    #path('fungi/new/', views.FungiCreateView.as_view(), name='new_fungi'),
    path('fungi/new/', views.FungiCreateView.as_view(), name='new_fungi'),
    path('fungi/<int:pk>/edit', views.FungiEditView.as_view(), name='fungi_edit'),

    #path('fruitingbody/<pk>/update/', FruitingBodyUpdate.as_view(), name='fruitingbody-update'),
    #path('habitat/<pk>/update/', HabitatUpdate.as_view(), name='habitat-update'),
    #path('OtherCommonNames/<pk>/update/', OtherCommonNamesUpdate.as_view(), name='othercommonnames-update'),
    #path('FungiComments/<pk>/update/',FungiCommentsUpdate.as_view(), name='fungicomments-update'),
    #path('Stipe/<pk>/update/', StipeUpdate.as_view(), name='stipe-update'),
    #path('PoresAndTubes/<pk>/update/', PoresAndTubesUpdate.as_view(), name='poresandtubes-update'),
    #path('Gills/<pk>/update/', GillsUpdate.as_view(), name='gills-update'),
    #path('Status/<pk>/update/', StatusUpdate.as_view(), name='status-update'),
    #path('Spores/<pk>/update/', SporesUpdate.as_view(), name='spores-update'),
    #path('Cuisine/<pk>/update/', CuisineUpdate.as_view(), name='cuisine-update'),
    #path('Flesh/<pk>/update/', FleshUpdate.as_view(), name='flesh-update'),
    #path('Classification/<pk>/update/', ClassificationUpdate.as_view(), name='classification-update'),
    #path('Seasons/<pk>/update/', SeasonsUpdate.as_view(), name='seasons-update'),


    #EDITING AND ADDING DATA
    path('fungi/<int:pk>/habitat/edit/', views.FungiHabitatEditView.as_view(), name='fungi_habitat_edit'),
    path('fungi/<int:pk>/cap/edit/', views.FungiCapEditView.as_view(), name='fungi_cap_edit'),
    path('fungi/<int:pk>/stipe/edit/', views.FungiStipeEditView.as_view(), name='fungi_stipe_edit'),
    path('fungi/<int:pk>/cuisine/edit/', views.FungiCuisineEditView.as_view(), name='fungi_cuisine_edit'),
    path('fungi/<int:pk>/flesh/edit/', views.FungiFleshEditView.as_view(), name='fungi_flesh_edit'),
    path('fungi/<int:pk>/seasons/edit/', views.FungiSeasonsEditView.as_view(), name='fungi_seasons_edit'),
    path('fungi/<int:pk>/spores/edit/', views.FungiSporesEditView.as_view(), name='fungi_spores_edit'),
    path('fungi/<int:pk>/status/edit/', views.FungiStatusEditView.as_view(), name='fungi_status_edit'),
    path('fungi/<int:pk>/pores/edit/', views.FungiPoresEditView.as_view(), name='fungi_pores_edit'),
    path('fungi/<int:pk>/gills/edit/', views.FungiGillsEditView.as_view(), name='fungi_gills_edit'),
    path('fungi/<int:pk>/comments/edit/', views.FungiCommentsEditView.as_view(), name='fungi_comments_edit'),
    path('fungi/<int:pk>/taxonomy/edit/', views.FungiTaxonomyEditView.as_view(), name='fungi_taxonomy_edit'),
    
    #path('fungi/<int:pk>/latinsynonyms', views.FungiLatinSynomymsView.as_view(), name='fungi_latinsynonyms_edit_add'),
    #path('fungi/<int:pk>/latinsynonyms/del/', views.FungiLatinSynomymsDeleteView.as_view(), name='fungi_latinsynonyms_del'),
    

    
    




    #PASSWORD
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('usersettings/', include('usersettings.urls', namespace="usersettings")),
    
    #SEARCH
    path('searchresults/', Search, name='search-fungi'),
    path('searchsuccess/', views.searchsuccess, name='search-success'),
    path('nosearchresults/', views.nosearchresults, name='no-search-results'),

    #path('__debug__/', include(debug_toolbar.urls)),
]


urlpatterns += [url(r'^health/?', include('health_check.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

