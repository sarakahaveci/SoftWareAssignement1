from django.conf.urls import url

from .view import show_todo, get_todo

urlpatterns = [
    url(r'^$', show_todo),

]
