from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, News, Service


# Static pages sitemap
class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'index',
            'about',
            'news',
            'blogs',
            'contact',
            'cost_calculator',
            'terms-and-conditions',
            'privacy-and-policy',
        ]

    def location(self, item):
        return reverse(item)


# Blog sitemap
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_date


# News sitemap
class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_date


# Service sitemap
class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()
