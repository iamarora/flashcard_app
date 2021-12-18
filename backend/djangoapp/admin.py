import datetime
import pytz

from django.contrib.auth.models import User, Group
from django.contrib import admin
from djangoapp.models import Words


class WordsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def time_to_appear_next(self, obj):
        time_to_appear_next = 'Available now'
        if obj.bin_number == 11 or obj.incorrect_counter >= 10:
            time_to_appear_next = 'Never'

        now = datetime.datetime.now(pytz.utc)
        if obj.available_time and obj.available_time > now:
            time_to_appear_next = obj.available_time - now
        return time_to_appear_next

    list_display  = (
        'word', 'bin_number', 'time_to_appear_next', 'incorrect_counter', 'is_removed',
    )
    search_fields = ('word', )

# Register your models here.
admin.site.register(Words, WordsAdmin)


# De-Register models not required.
admin.site.unregister(Group)
admin.site.unregister(User)
