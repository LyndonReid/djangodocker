"""offerhistory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from offers.views import home_view, search_view, allmakes_list_view, Offersbymodel_list_detail_view, Model_list_view, Offersbymodelandoffertype_list_detail_view,getModelsAjax, setModelAjax, setLocationAjax, about_view
from django.urls import path,re_path, include
from django.views.generic.base import TemplateView




from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    #path('search2/makepage_list', MakePageListView.as_view()),
    #path('search2/makepage_detail', MakePageDetailView.as_view()),
    #path('search2/makepage_detail/<str:carmake>', MakePageDetailView.as_view()),
    
    path('admin/', admin.site.urls),
    path('', home_view),
    path('about/', about_view),
    path('', search_view),
    path('makes/', allmakes_list_view),
    path('make/<str:carmake>', Model_list_view.as_view()),
    path('make/<str:carmake>/model/<str:carmodel>', Offersbymodel_list_detail_view.as_view()),
    path('make/<str:carmake>/model/<str:carmodel>/<str:offertype>', Offersbymodelandoffertype_list_detail_view.as_view()),
    path('getModelsAjax', getModelsAjax ),
    path('setModelAjax', setModelAjax ),
    path('setLocationAjax', setLocationAjax ),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
    #path('pages/', include(wagtail_urls)),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)