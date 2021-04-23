from django.contrib import admin
from .models import TrainVkp1,SeatVkp1,StationVkp1,RouteStationVkp1,RouteVkp1,BookingsVkp4,BogieVkp1
# Register your models here.
admin.site.register(BogieVkp1)
admin.site.register(BookingsVkp4)
admin.site.register(RouteStationVkp1)
admin.site.register(RouteVkp1)
admin.site.register(SeatVkp1)
admin.site.register(StationVkp1)
admin.site.register(TrainVkp1)