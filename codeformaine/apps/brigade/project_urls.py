from django.conf.urls import url
from brigade import views as brigade_views

urlpatterns = [
    url(r'^projects/add/',
        view=brigade_views.ProjectCreateView.as_view(),
        name="project-create"),
    url(r'^projects/(?P<slug>[-\w]+)/edit/',
        view=brigade_views.ProjectUpdateView.as_view(),
        name="project-update"),
    url(r'^projects/(?P<slug>[-\w]+)/join/',
        view=brigade_views.ProjectJoinView.as_view(),
        name="project-join"),
    url(r'^projects/(?P<slug>[-\w]+)/leave/',
        view=brigade_views.ProjectLeaveView.as_view(),
        name="project-leave"),
    url(r'^projects/(?P<slug>[-\w]+)/buzz/create/',
        view=brigade_views.BuzzCreateView.as_view(),
        name="buzz-create"),
    url(r'^projects/(?P<project_slug>[-\w]+)/buzz/(?P<slug>[-\w]+)/',
        view=brigade_views.BuzzDetailView.as_view(),
        name="buzz-detail"),
    url(r'^projects/(?P<project_slug>[-\w]+)/commit/(?P<slug>[-\w]+)/',
        view=brigade_views.ProjectCommitDetailView.as_view(),
        name="commit-detail"),
    url(r'^projects/(?P<slug>[-\w]+)/link/create/',
        view=brigade_views.LinkCreateView.as_view(),
        name="link-create"),
    url(r'^projects.json',
        view=brigade_views.ProjectListJSONView.as_view(),
        name="project-list-json"),
    url(r'^projects/(?P<slug>[-\w]+)/',
        view=brigade_views.ProjectDetailView.as_view(),
        name="project-detail"),
    url(r'^projects/$',
        view=brigade_views.ProjectListView.as_view(),
        name="project-list")
]

#url(r'^projects.csv',
#    view=brigade_views.ProjectListCSVView.as_view(),
#    name="project-list-csv"),

