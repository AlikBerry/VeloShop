# Generated by Django 2.2.6 on 2019-11-01 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xmtb_app', '0002_auto_20191101_2004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Products', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmtb_app.Brands'),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmtb_app.Categories'),
        ),
        migrations.AddField(
            model_name='products',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmtb_app.Cities'),
        ),
        migrations.AddField(
            model_name='products',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='heading',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='products',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='tel_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Subcategories',
        ),
    ]
