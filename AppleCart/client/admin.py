from django.contrib import admin
from .models import User
from .models import Item
from .models import AppleCartadmin
from .models import Order
admin.site.register(User)
admin.site.register(Item)
admin.site.register(AppleCartadmin)
admin.site.register(Order)


