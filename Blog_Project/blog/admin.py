from django.contrib import admin
from blog.models import *

# Register your models her
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)