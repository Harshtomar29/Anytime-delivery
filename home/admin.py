from django.contrib import admin

from home.models import Contact
from home.models import Courier

from home.models import Orders
from home.models import Reserve



# Register your models here.


admin.site.register(Contact)

admin.site.register(Courier)

admin.site.register(Orders)


admin.site.register(Reserve)

