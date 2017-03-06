from django.conf.urls import patterns, include, url
from apps.hello.views import HomeView
from apps.request_history.views import RequestHistoryView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^request_history$',RequestHistoryView.as_view(),name='request_history'),
    url(r'^add_data$','apps.hello.views.my_add_data_form',name='add_data'),
)
