from django.contrib import admin
from .models import Image, Region

from django.utils.safestring import mark_safe



class RegionInline(admin.TabularInline):
    model = Region
    extra = 3


class ImageAdmin(admin.ModelAdmin):

    list_display = ('filename', 'scene_no', 'shot_no', 'frame_no', 'tag_list', 'image_preview')
    fieldsets = [
        (None, {'fields': ['filename', 'extension', 'directory']}),
        ('frame indexes', {'fields': ['scene_no', 'shot_no', 'frame_no']}),
        (None, {'fields': ('tags',)}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [RegionInline]
    list_filter = ['extension', 'tags__name', 'scene_no', 'shot_no', 'frame_no']
    search_fields = ['filename', 'scene_no', 'shot_no', 'frame_no', 'tags__name']


    def get_queryset(self, request):
        return super(ImageAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def image_preview(self, image):
        url = '/m/MissingLink_Groundtruth_PNG/' + image.directory + '/' + image.filename + image.extension

        #change_url = urlresolvers.reverse('admin:posts_post_change', args=(post.id,))

        link = '<a href="%s">preview</a>' % url
        return mark_safe(link)

    image_preview.short_description = 'Preview'


admin.site.register(Image, ImageAdmin)
