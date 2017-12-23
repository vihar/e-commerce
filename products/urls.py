from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='index'),
    url(r'^categorie/$',
        views.categorie_view, name='categorie'),
    url(r'^precurated-boxes/$',
        views.pre_boxes, name='pre_boxes'),
    url(r'^about/$',
        views.about_us, name='about'),
    url(r'^faqs/$',
        views.faqs, name='faqs'),
    url(r'^contact/$',
        views.contact, name='contact'),
    url(r'^souvenirs/$',
        views.souvenirs, name='souvenirs'),
    url(r'^curated-box/$',
        views.curatedbox, name='curatedbox'),


    url(r'^categorie/(?P<slug>[-\w]+)/$',
        views.categorie_detail, name='categorie_item_details'),
    url(r'^item/(?P<pk>[0-9]+)/$',
        views.ItemDetail.as_view(), name='snippet_detail'),
]
