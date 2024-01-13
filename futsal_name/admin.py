from django.contrib import admin
from . models import  Futsal, FutsalbookingUser, Futsalbookingdetail

# Register your models here.
#admin.site.register(Futsal)
admin.site.register(FutsalbookingUser)

#admin.site.register(Futsalbookingdetail)

@admin.register(Futsal)
class FutsalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'web', 'email_address','zip_code', 'phone',)
    ordering = ('name', )
    search_fields = ('name', 'address',)


@admin.register(Futsalbookingdetail)
class FutsalbookingdetailAdmin(admin.ModelAdmin):
    fields = (('name','futsal'), 'booking_date', 'location', 'incharge', 'phone', 'rate',)
    list_display = ('name','futsal','booking_date','location','incharge','phone','rate',)
    list_filter = ('name','futsal','booking_date','location','incharge','phone','rate',)
    ordering = ('name','futsal','booking_date',)