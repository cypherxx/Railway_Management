from django.db import models

# Create your models here

class BogieVkp1(models.Model):
    bogie_id = models.TextField(primary_key=True)  # This field type is a guess.
    train = models.ForeignKey('TrainVkp1', models.DO_NOTHING, blank=True, null=True)
    no_of_seats = models.IntegerField()
    bogie_type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'bogie_vkp1'


class BookingsVkp4(models.Model):
    pnr = models.IntegerField(primary_key=True)
    p_name = models.TextField()  # This field type is a guess.
    p_age = models.IntegerField()
    p_gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_source = models.TextField()  # This field type is a guess.
    p_destination = models.TextField()  # This field type is a guess.
    journey_date = models.TextField()  # This field type is a guess.
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
    route_id = models.TextField(primary_key=True)  # This field type is a guess.
    no_of_stations = models.IntegerField()
    train = models.ForeignKey('TrainVkp1', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'route_vkp1'


class SeatVkp1(models.Model):
    seat_id = models.TextField(primary_key=True)  # This field type is a guess.
    bogie = models.ForeignKey(BogieVkp1, models.DO_NOTHING, blank=True, null=True)
    seat_status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'seat_vkp1'


class StationVkp1(models.Model):
    station_id = models.TextField(primary_key=True)  # This field type is a guess.
    stations_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'station_vkp1'


class TrainVkp1(models.Model):
    train_id = models.TextField(primary_key=True)  # This field type is a guess.
    train_name = models.TextField()  # This field type is a guess.
    train_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_of_bogies = models.IntegerField()
    source_name = models.TextField()  # This field type is a guess.
    dest_name = models.TextField()  # This field type is a guess.
    departure_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    arrival_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'train_vkp1'