"""pollutrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from pollutrack import views

from pollution import views as poll_views
from images import views as image_views
from event import views as event_views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^pollution/list/$',
        poll_views.ListPollutionSources.as_view()),
    url(r'^pollution/get/$',
        poll_views.GetPollutionSources.as_view()),
    url(r'^pollution/create/$',
        poll_views.CreatePollutionSource.as_view(),
        name='create-pollution'),
    url(r'^pollution/approve/$',
        poll_views.AddApproval.as_view(),
        name='approve-pollution'),
    url(r'^event/list/$',
        event_views.ListEvents.as_view(),
        name='event-list'),

    url(r'^images/upload/$',
        image_views.UploadImage.as_view(),
        name='upload-image'),

    url(r'^admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
