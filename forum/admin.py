from django.contrib import admin
from .models import thread
# Register your models here.


class threadAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    exclude = ('upvote',)


admin.site.register(thread, threadAdmin)
