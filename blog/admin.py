from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = "بر اساس کلیدهای پرتکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('python', 'پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


# class CommentInLine(admin.StackedInline):
class CommentInLine(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'status', 'updated', 'show_image')
    list_editable = ('title',)
    list_filter = ('status', 'published', FilterByTitle)
    search_fields = ('title', 'body')
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)
