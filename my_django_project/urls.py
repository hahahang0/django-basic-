"""
URL configuration for my_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
# from django.urls import path,inlucde
from drf_spectacular.views import(SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('amazon/',include('amazon.urls')),
    path('library/',include('library.urls')),
    path('accounts/',include('accounts.urls')),
    path('api/',include('books.urls')),
    path('api/',include('products.urls')),
    path('api/',include('dictionary.urls')),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui"
    ),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        ),
        name="redoc"
    ),
    path('journals/',include('journals.urls'),name="journals"),
    # path('api/schema/',SpectacularAPIView.as_view(),name="Schema"),
    # path('api/docs/',SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui"),
    # path('api/redoc/',SpectacularRedocView.as_view(url_name="schema"),name="redoc"),
    
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
