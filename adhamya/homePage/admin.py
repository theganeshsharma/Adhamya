from django.contrib import admin
from . models import *


admin.site.register(Member)
admin.site.register(Events)
admin.site.register(NewsFeed)
admin.site.register(Subscribers)
admin.site.register(Fest)

admin.site.register(Participation)

# Register your models here.
