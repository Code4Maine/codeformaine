from django.conf.urls import url
from brigade import views as brigade_views

urlpatterns = [
    url(r'^ideas/add/',
        view=brigade_views.ProjectIdeaCreateView.as_view(),
        name="projectidea-create"),
    url(r'^ideas/(?P<slug>[-\w]+)/edit/',
        view=brigade_views.ProjectIdeaUpdateView.as_view(),
        name="projectidea-update"),
    url(r'^ideas.json',
        view=brigade_views.ProjectIdeaListJSONView.as_view(),
        name="projectidea-list-json"),
    url(r'^ideas/(?P<slug>[-\w]+)/',
        view=brigade_views.ProjectIdeaDetailView.as_view(),
        name="projectidea-detail"),
    url(r'^ideas/$',
        view=brigade_views.ProjectIdeaListView.as_view(),
        name="projectidea-list")
]


    #url(r'^ideas.csv',
    #    view=brigade_views.ProjectIdeaListCSVView.as_view(),
    #    name="projectidea-list-csv"),
