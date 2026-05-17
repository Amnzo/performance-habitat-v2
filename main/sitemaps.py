import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article, Project


class StaticSitemap(Sitemap):
    def items(self):
        return [
            ('index',    1.0,  'daily',   datetime.date(2025, 1, 1)),
            ('blog',     0.9,  'weekly',  datetime.date(2025, 1, 1)),
            ('services', 0.8,  'monthly', datetime.date(2025, 1, 1)),
            ('projects', 0.8,  'monthly', datetime.date(2025, 1, 1)),
            ('contact',  0.5,  'yearly',  datetime.date(2025, 1, 1)),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]

    def lastmod(self, item):
        return item[3]


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.85

    def items(self):
        return Article.objects.filter(is_published=True).order_by('-date_publication')

    def lastmod(self, obj):
        return obj.date_modification

    def location(self, obj):
        return reverse('blog_detail', kwargs={'slug': obj.slug})


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.75

    def items(self):
        return Project.objects.all().order_by('-date')

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return reverse('project_detail', kwargs={'slug': obj.slug})
