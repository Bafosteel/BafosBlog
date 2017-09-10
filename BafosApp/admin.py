from django.contrib import admin
from .models import BlogPost,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

    list_display = ('name', 'slug')


class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

    list_display = ('created_date', 'published_date', 'title', 'draft')
    list_display_links = ('title',)
    list_filter = ('created_date', 'published_date', 'draft')
    date_hierarchy = 'created_date'
    search_fields = ('title', 'tease', 'body')

    exclude = ('created_date',)
    fieldsets = (
        (None, {'fields': ('slug', 'title', 'tease', 'body')}),
        ('Properties', {'fields': ('draft', 'published_date', 'category')}),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogEntryAdmin)