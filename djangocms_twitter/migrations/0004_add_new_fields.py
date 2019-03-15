# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-15 12:57
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_twitter', '0003_update_twitter_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='twittertimeline',
            name='chrome',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Control the frame around the linear timeline'),
        ),
        migrations.AddField(
            model_name='twittertimeline',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Height in pixels', null=True, verbose_name='height'),
        ),
        migrations.AddField(
            model_name='twittertimeline',
            name='link_color',
            field=colorfield.fields.ColorField(blank=True, default='#2B7BB9', max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='twittertimeline',
            name='show_replies',
            field=models.BooleanField(default=False, verbose_name='Show Tweet Replies'),
        ),
        migrations.AddField(
            model_name='twittertimeline',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=50, verbose_name='select theme'),
        ),
        migrations.AddField(
            model_name='twittertimeline',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Width in pixels', null=True, verbose_name='width'),
        ),
        migrations.AlterField(
            model_name='twittertimeline',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_twitter_twittertimeline', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='twittertimeline',
            name='title',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='twittertimeline',
            name='tweet_limit',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Number of entries to display', null=True, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='twittertimeline',
            name='twitter_url',
            field=models.CharField(help_text='Enter a Twitter URL (see https://publish.twitter.com) e.g. <br><ol><li>A collection: https://twitter.com/TwitterDev/timelines/539487832448843776</li><li>A tweet: https://twitter.com/Interior/status/463440424141459456</li><li>A profile: https://twitter.com/TwitterDev</li><li>A list: https://twitter.com/TwitterDev/lists/national-parks</li><li>A moment: https://twitter.com/i/moments/625792726546558977</li><li>A likes timeline: https://twitter.com/TwitterDev/likes</li></ol>', max_length=512, verbose_name='twitter url'),
        ),
    ]
