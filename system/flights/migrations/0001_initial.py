# Generated by Django 2.0.5 on 2018-06-01 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('capacity', models.IntegerField(default=25)),
                ('official_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captainsName', models.CharField(max_length=150)),
                ('captainsSurname', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airplane', to='flights.Airplane')),
                ('final_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_airport', to='flights.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Passenger')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='passenger',
            unique_together={('name', 'surname')},
        ),
        migrations.AddField(
            model_name='flight',
            name='passengers',
            field=models.ManyToManyField(through='flights.Ticket', to='flights.Passenger'),
        ),
        migrations.AddField(
            model_name='flight',
            name='start_airport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_airport', to='flights.Airport'),
        ),
        migrations.AddField(
            model_name='crew',
            name='flight',
            field=models.ManyToManyField(related_name='crew', through='flights.Contract', to='flights.Flight'),
        ),
        migrations.AddField(
            model_name='contract',
            name='crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Crew'),
        ),
        migrations.AddField(
            model_name='contract',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight'),
        ),
        migrations.AlterUniqueTogether(
            name='airport',
            unique_together={('country', 'city')},
        ),
        migrations.AlterUniqueTogether(
            name='crew',
            unique_together={('captainsName', 'captainsSurname')},
        ),
    ]
