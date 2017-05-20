from django.contrib import admin
from .models import Group
from .models import Member
from .models import Chat
from .models import Note

admin.site.register(Group)
admin.site.register(Member)
admin.site.register(Chat)
admin.site.register(Note)