from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("wiki/<str:name>/", views.entry, name="entry"),
    path("search/", views.search_bar, name="search_bar"),
    path("add_new_entry", views.add_new_entry, name="add_new_entry"),
    path("wiki/edit_page", views.edit_page, name="edit_page"),
    path("wiki/update_changes", views.update_changes, name="update_changes"),
    path("random_entry", views.random_entry, name="random_entry")
]
