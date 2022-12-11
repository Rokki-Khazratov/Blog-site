from django.contrib import admin
from .models import Carousel, NewsUrl, Section, Services, NewsUrl

# Register your models here.
admin.site.register(Carousel)
admin.site.register(Section)
admin.site.register(Services)
admin.site.register(NewsUrl)