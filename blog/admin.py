from django.contrib import admin

from .models import Publicacion
from .models import Carro
from .models import Tiket


admin.site.register(Publicacion)
admin.site.register(Carro)
admin.site.register(Tiket)
