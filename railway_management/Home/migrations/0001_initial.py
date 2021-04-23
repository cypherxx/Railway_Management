# Generated by Django 3.1.7 on 2021-04-23 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BogieVkp1',
            fields=[
                ('bogie_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('no_of_seats', models.IntegerField()),
                ('bogie_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bogie_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StationVkp1',
            fields=[
                ('station_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stations_name', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'db_table': 'station_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TrainVkp1',
            fields=[
                ('train_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=50)),
                ('train_type', models.CharField(blank=True, max_length=50, null=True)),
                ('no_of_bogies', models.IntegerField()),
                ('source_name', models.CharField(max_length=50)),
                ('dest_name', models.CharField(max_length=50)),
                ('departure_time', models.CharField(blank=True, max_length=20, null=True)),
                ('arrival_time', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'train_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SeatVkp1',
            fields=[
                ('seat_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('seat_status', models.CharField(blank=True, max_length=50, null=True)),
                ('bogie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.bogievkp1')),
            ],
            options={
                'db_table': 'seat_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RouteVkp1',
            fields=[
                ('route_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('no_of_stations', models.IntegerField()),
                ('train', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.trainvkp1')),
            ],
            options={
                'db_table': 'route_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RouteStationVkp1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.routevkp1')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.stationvkp1')),
            ],
            options={
                'db_table': 'route_station_vkp1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BookingsVkp4',
            fields=[
                ('pnr', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_age', models.IntegerField()),
                ('p_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('p_source', models.CharField(max_length=50)),
                ('p_destination', models.CharField(max_length=50)),
                ('journey_date', models.DateField()),
                ('seat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.seatvkp1')),
            ],
            options={
                'db_table': 'bookings_vkp4',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='bogievkp1',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.trainvkp1'),
        ),
    ]
