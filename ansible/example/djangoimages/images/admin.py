from django.contrib import admin
from .models import Image, Region


class RegionInline(admin.TabularInline):
    model = Region
    extra = 3


class ImageAdmin(admin.ModelAdmin):

    list_display = ('filename', 'directory', 'pub_date', 'was_published_recently', 'tag_list')
    fieldsets = [
        (None, {'fields': ['filename']}),
        ('dir', {'fields': ['directory']}),
        (None, {'fields': ('tags',)}),

        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [RegionInline]
    list_filter = ['pub_date']
    search_fields = ['filename', 'tags__name']

    def get_queryset(self, request):
        return super(ImageAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Image, ImageAdmin)
