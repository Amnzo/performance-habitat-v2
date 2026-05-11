import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article


class StaticSitemap(Sitemap):
    def items(self):
        return [
            ('index',    1.0,  'daily'),
            ('blog',     0.9,  'weekly'),
            ('services', 0.8,  'monthly'),
            ('projects', 0.8,  'monthly'),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]

    def lastmod(self, item):
        return datetime.date.today()


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.85

    def items(self):
        return Article.objects.filter(is_published=True).order_by('-date_publication')

    def lastmod(self, obj):
        return obj.date_publication

    def location(self, obj):
        return f'/blog/{obj.slug}/'
