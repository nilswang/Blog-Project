from django.contrib import admin
from blog.models import *
class CommentAdmin(admin.ModelAdmin):
    class Media:
        js = (
        '/static/js/kindeditor/kindeditor-all.js',
        '/static/js/kindeditor/lang/zh-CN.js',
        '/static/js/kindeditor/config.js',
        )
    search_fields = ('username',)
    fieldsets = (
        ['Main',
         {'fields':('content', 'username', 'email'),
           }],
        ['Advance',
         {'classes': ('collapse',), # CSS
             'fields':('url','user', 'article', 'pid',), }]
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content')
    search_fields = ('title',)
    fieldsets = (
        ['Main',
         {'fields':('title', 'desc', 'content'),
          }],
        ['Advance',
         {'classes': ('collapse',), # CSS
             'fields':('click_count', 'is_recommend', 'user',), }]
    )
    class Media:
        js = (
        '/static/js/kindeditor/kindeditor-all.js',
        '/static/js/kindeditor/lang/zh-CN.js',
        '/static/js/kindeditor/config.js',
    )

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url')



# Register your models her
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad, AdAdmin)