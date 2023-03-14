from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post , Page


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class imageAdmin (admin.ModelAdmin):
    list_display = ("featured")


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = ("content",)



admin.site.register(Post,PostAdmin)
