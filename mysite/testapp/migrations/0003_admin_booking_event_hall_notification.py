# Generated by Django 5.0.4 on 2024-04-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_userinfo1_delete_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminId', models.IntegerField()),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('eventId', models.IntegerField()),
                ('bookingTime', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventId', models.IntegerField()),
                ('eventName', models.CharField(max_length=50)),
                ('eventDateTime', models.DateTimeField()),
                ('venue', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallId', models.IntegerField()),
                ('hallName', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificationId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('msg', models.CharField(max_length=200)),
                ('sendTime', models.DateTimeField()),
            ],
        ),
    ]
