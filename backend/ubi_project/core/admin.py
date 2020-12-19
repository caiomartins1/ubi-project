from django.contrib import admin
from .models import Client, Content, ContentUpselling, ContentHighlight, \
                    ContentSibling

# Register your models here.
admin.site.register(Client)
admin.site.register(Content)
admin.site.register(ContentSibling)
admin.site.register(ContentUpselling)
admin.site.register(ContentHighlight)
