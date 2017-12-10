from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='index'),
    url(r'^categorie/$',
        views.categorie_view, name='categorie'),
    url(r'^categorie/(?P<slug>[-\w]+)/$',
        views.categorie_detail, name='categorie_item_details'),
    url(r'^item/(?P<pk>[0-9]+)/$',
        views.ItemDetail.as_view(), name='snippet_detail'),
]
