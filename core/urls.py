"""core URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainsite.urls', namespace='mainsite')),
    path('comment/', include('comment.urls')),
    path('subscribe/', include('subscription.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(
            [
                # path("swagger", schema_view.with_ui("swagger", cache_timeout=0)),
                # path("", include("accounts.api.urls")),
                path('', include('mainsite.api.urls')),
                # path("", include("tags.api.urls")),
                # path('auth/oauth/', include('rest_framework_social_oauth2.urls'))
            ]
        )
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)