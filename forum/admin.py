from django.contrib import admin
from .models import thread, comment
# Register your models here.


class threadAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    exclude = ('upvote',)


class commentAdmin(admin.ModelAdmin):
    exclude = ('comment_upvote',)


admin.site.register(thread, threadAdmin)
admin.site.register(comment, commentAdmin)
