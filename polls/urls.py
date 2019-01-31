from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from polls.models import Poll
from polls.views import vote, results

urlpatterns = (
    re_path(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
   re_path(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
   re_path(r'^(?P<pk>\d+)/results/$',
           DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
           name='poll_results'),
   re_path(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
)