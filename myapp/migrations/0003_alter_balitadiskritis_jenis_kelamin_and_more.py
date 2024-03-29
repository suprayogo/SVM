# Generated by Django 4.1 on 2024-01-01 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_balitadiskritis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balitadiskritis',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=10),
        ),
        migrations.AlterField(
            model_name='balitadiskritis',
            name='status_gizi',
            field=models.CharField(choices=[('Gizi Buruk', 'Gizi Buruk'), ('Gizi Kurang', 'Gizi Kurang'), ('Gizi Normal', 'Gizi Normal'), ('Gizi Lebih', 'Gizi Lebih')], max_length=20),
        ),
        migrations.AlterField(
            model_name='balitadiskritis',
            name='usia',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='BalitaPengujian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atribut_tambahan_pengujian', models.CharField(max_length=255)),
                ('balita_diskritis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.balitadiskritis')),
            ],
        ),
        migrations.CreateModel(
            name='BalitaPelatihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atribut_tambahan_pelatihan', models.CharField(max_length=255)),
                ('balita_diskritis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.balitadiskritis')),
            ],
        ),
    ]
