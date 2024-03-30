from django.contrib import admin
from .models import Member,images,NewsItem

admin.site.register(images)
admin.site.register(NewsItem)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name','position','img']
    search_fields = ['name','position']
    list_filter = ['position']




