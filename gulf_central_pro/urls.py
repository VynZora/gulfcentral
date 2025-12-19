"""gulf_central_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# project-level urls.py (e.g., gulf_central_pro/urls.py)
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from gulf_central.sitemaps import StaticViewSitemap, BlogSitemap, NewsSitemap, ServiceSitemap

# Sitemaps dictionary
sitemaps = {
    'static': StaticViewSitemap,
    'blogs': BlogSitemap,
    'news': NewsSitemap,
    'services': ServiceSitemap,
}

# Robots.txt view
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /dashboard",
        "Disallow: /login",
        "Disallow: /logout_user",
        "",
        # Change this to your production domain when deploying
        "Sitemap: http://127.0.0.1:8000/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    # path('admin/', admin.site.urls),

    # Robots.txt should be first
    path('robots.txt', robots_txt, name='robots_txt'),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # Include your app URLs
    path('', include('gulf_central.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 page
handler404 = 'gulf_central.views.page_404'
