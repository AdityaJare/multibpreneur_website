from django.contrib import admin
from .models import BlogPost, BusinessInquiry, ContactInquiry, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publication_date')
    list_filter = ('status', 'categories', 'tags', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publication_date'
    filter_horizontal = ('categories', 'tags')

@admin.register(BusinessInquiry)
class BusinessInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'submission_date')
    list_filter = ('status', 'submission_date')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'submission_date'
    readonly_fields = ('submission_date',)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'submission_date')
    list_filter = ('status', 'submission_date')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'submission_date'
    readonly_fields = ('submission_date',)
