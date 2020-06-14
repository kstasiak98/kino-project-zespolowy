from django.contrib import admin
from backend.models import (Bilet, Cennik, Klient,
                            Produkt, Sala, Seans, ZajeteMiejsca,
                            Zamowienie, Film,)
# Register your models here.

admin.site.register(Bilet)
admin.site.register(Cennik)
admin.site.register(Klient)
admin.site.register(Produkt)
admin.site.register(Sala)
admin.site.register(Seans)
admin.site.register(ZajeteMiejsca)
admin.site.register(Zamowienie)
admin.site.register(Film)
