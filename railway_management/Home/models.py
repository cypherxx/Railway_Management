from django.db import models

# Create your models here

class BogieVkp1(models.Model):
    bogie_id = models.CharField(primary_key=True, max_length=10)
    train = models.ForeignKey('TrainVkp1', models.DO_NOTHING, blank=True, null=True)
    no_of_seats = models.IntegerField()
    bogie_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bogie_vkp1'

class BookingsVkp4(models.Model):
    pnr = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_age = models.IntegerField()
    p_gender = models.CharField(max_length=10, blank=True, null=True)
    p_source = models.CharField(max_length=50)
    p_destination = models.CharField(max_length=50)
    journey_date = models.DateField()
    seat = models.ForeignKey('SeatVkp1', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bookings_vkp4'

class RouteStationVkp1(models.Model):
    station = models.ForeignKey('StationVkp1', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('RouteVkp1', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'route_station_vkp1'

class RouteVkp1(models.Model):
    route_id = models.CharField(primary_key=True, max_length=10)
    no_of_stations = models.IntegerField()
    train = models.ForeignKey('TrainVkp1', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'route_vkp1'


class SeatVkp1(models.Model):
    seat_id = models.CharField(primary_key=True, max_length=10)
    bogie = models.ForeignKey(BogieVkp1, models.DO_NOTHING, blank=True, null=True)
    seat_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seat_vkp1'


class StationVkp1(models.Model):
    station_id = models.CharField(primary_key=True, max_length=10)
    stations_name = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'station_vkp1'


class TrainVkp1(models.Model):
    train_id = models.CharField(primary_key=True, max_length=10)
    train_name = models.CharField(max_length=50)
    train_type = models.CharField(max_length=50, blank=True, null=True)
    no_of_bogies = models.IntegerField()
    source_name = models.CharField(max_length=50)
    dest_name = models.CharField(max_length=50)
    departure_time = models.CharField(max_length=20, blank=True, null=True)
    arrival_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'train_vkp1'