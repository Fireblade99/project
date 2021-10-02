from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider
# Register your models here.

class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'getImg',)
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'getImg',)
    readonly_fields = ('getImg',)

    def getImg(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'Нет изображения'
    getImg.short_description = 'Миниатюрный вид картинки'

admin.site.register(CmsSlider, CmsAdmin)