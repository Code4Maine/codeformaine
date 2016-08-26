from django.conf.urls import include, url
from brigade import views as brigade_views


# custom views
urlpatterns = [
    url(r'^', include('brigade.worker_urls')),
    url(r'^', include('brigade.project_urls')),
    url(r'^', include('brigade.idea_urls')),
    url(r'^events/add/',
        view=brigade_views.EventCreateView.as_view(),
        name="event-create"),

    url(r'^events/(?P<slug>[-\w]+)/',
        view=brigade_views.EventDetailView.as_view(),
        name="event-detail"),

    url(r'^events/$',
        view=brigade_views.EventListView.as_view(),
        name="event-list"),

    url(r'^topic/add/',
        view=brigade_views.TopicCreateView.as_view(),
        name="topic-create"),

    url(r'^topic/(?P<slug>[-\w]+)/',
        view=brigade_views.TopicDetailView.as_view(),
        name="topic-detail"),

    url(r'^topic/$',
        view=brigade_views.TopicListView.as_view(),
        name="topic-list"),

    url(r'^technology/add/',
        view=brigade_views.TechnologyCreateView.as_view(),
        name="technology-create"),

    url(r'^technology/(?P<slug>[-\w]+)/',
        view=brigade_views.TechnologyDetailView.as_view(),
        name="technology-detail"),

    url(r'^technology/$',
        view=brigade_views.TechnologyListView.as_view(),
        name="technology-list"),

    url(r'^$',
        view=brigade_views.DashboardView.as_view(),
        name="dashboard",),
]
