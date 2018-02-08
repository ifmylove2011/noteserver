from django.contrib import admin

from NoteModel.models import Note, Category, Attach


# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('_id', 'title', 'updateTime',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'count')


class AttachAdmin(admin.ModelAdmin):
    list_display = ('_id', 'filename', 'uploadTime')

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attach, AttachAdmin)
