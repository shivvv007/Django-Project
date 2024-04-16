from django.contrib import admin

from .models import Record
from .models import Vendor


admin.site.register(Record)
admin.site.register(Vendor)