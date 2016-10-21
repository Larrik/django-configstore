# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=50)),
                ('data', models.TextField(db_column=b'data')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='configuration',
            unique_together=set([('key', 'site')]),
        ),
    ]
