# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DragNDropChangelistExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
                ('subtitle', models.CharField(max_length=b'50', blank=True)),
                ('boolean', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': "Drag n' drop changelist example",
                'verbose_name_plural': "Drag n' drop changelist example",
            },
        ),
        migrations.CreateModel(
            name='InlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
            ],
            options={
                'verbose_name': 'Inline example',
                'verbose_name_plural': 'Inline example',
            },
        ),
        migrations.CreateModel(
            name='InlineExampleExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field1', models.CharField(max_length=b'50', blank=True)),
                ('field2', models.CharField(max_length=b'50', blank=True)),
                ('field3', models.CharField(max_length=b'50', blank=True)),
                ('inline', models.OneToOneField(to='demo_application.InlineExample')),
            ],
            options={
                'verbose_name': 'One-To-One inline example',
                'verbose_name_plural': 'One-To-One inline example',
            },
        ),
        migrations.CreateModel(
            name='ModalStackedInlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
                ('description', models.TextField(blank=True)),
                ('choice', models.CharField(max_length=b'20', choices=[(b'choice1', b'Choice 1'), (b'choice2', b'Choice 2')])),
                ('date', models.DateField(default=datetime.date.today)),
                ('inline', models.ForeignKey(to='demo_application.InlineExample')),
            ],
            options={
                'verbose_name': 'Modal stacked inline example',
                'verbose_name_plural': 'Modal stacked inline example',
            },
        ),
        migrations.CreateModel(
            name='NestedInlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Nested inline',
                'verbose_name_plural': 'Nested inline',
            },
        ),
        migrations.CreateModel(
            name='PopupInlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
                ('inline', models.ForeignKey(to='demo_application.InlineExample')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Ajax/Popup inline example',
                'verbose_name_plural': 'Ajax/Popup inline example',
            },
        ),
        migrations.CreateModel(
            name='SideBarMenuExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'<strong>The affix</strong> example title. Help text may include HTML.', max_length=b'50')),
                ('field1', models.CharField(max_length=b'50', blank=True)),
                ('field2', models.CharField(help_text=b'Small input field', max_length=b'50', blank=True)),
                ('field3', models.CharField(help_text=b'Medium input field', max_length=b'50', blank=True)),
                ('field4', models.CharField(help_text=b'Large input field (default)', max_length=b'50', blank=True)),
                ('field5', models.CharField(help_text=b'XLarge input field', max_length=b'50', blank=True)),
                ('field6', models.CharField(help_text=b'XXLarge input field', max_length=b'50', blank=True)),
                ('field7', models.CharField(max_length=b'50', blank=True)),
                ('field8', models.CharField(max_length=b'50', blank=True)),
                ('field9', models.CharField(max_length=b'50', blank=True)),
            ],
            options={
                'verbose_name': 'Side-Bar menu example',
                'verbose_name_plural': 'Side-Bar menu example',
            },
        ),
        migrations.CreateModel(
            name='StackedInlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
                ('field1', models.CharField(max_length=b'50', blank=True)),
                ('choice', models.CharField(max_length=b'20', choices=[(b'choice1', b'Choice 1'), (b'choice2', b'Choice 2')])),
                ('inline', models.ForeignKey(to='demo_application.InlineExample')),
            ],
            options={
                'verbose_name': 'Stacked inline example',
                'verbose_name_plural': 'Stacked inline example',
            },
        ),
        migrations.CreateModel(
            name='TabularInlineExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'50')),
                ('choice', models.CharField(max_length=b'20', choices=[(b'choice1', b'Choice 1'), (b'choice2', b'Choice 2')])),
                ('inline', models.ForeignKey(to='demo_application.InlineExample')),
            ],
            options={
                'verbose_name': 'Tabular inline example',
                'verbose_name_plural': 'Tabular inline example',
            },
        ),
        migrations.CreateModel(
            name='WidgetsExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autocomplete', models.CharField(help_text=b'This widget suggests values based on other records', max_length=50)),
                ('text_area', models.TextField(blank=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('radio_select', models.CharField(default=b'choice1', max_length=20, choices=[(b'choice1', b'Choice 1'), (b'choice2', b'Choice 2'), (b'choice3', b'Choice 3')])),
                ('boolean', models.BooleanField(default=False)),
                ('boolean2', models.BooleanField(default=False, help_text=b'You can change the switch labels, size and colors, like in the fields below.')),
                ('boolean3', models.BooleanField(default=False)),
                ('boolean4', models.BooleanField(default=False)),
                ('foreign_key', models.ForeignKey(related_name='fk1', blank=True, to='demo_application.SideBarMenuExample', help_text=b'add dialog opens in fancybox', null=True)),
                ('foreign_key2', models.ForeignKey(related_name='fk2', blank=True, to='demo_application.SideBarMenuExample', help_text=b'raw_id opens in fancybox as well', null=True)),
                ('foreign_key3', models.ForeignKey(related_name='fk3', blank=True, to='demo_application.SideBarMenuExample', help_text=b"select2 alternative for foreign keys. This adds a search box to quickly find the records you're looking for.", null=True)),
                ('multiple_select', models.ManyToManyField(help_text=b'<p>Default multiple select with horizontal filtering.</p>', to='demo_application.SideBarMenuExample', null=True, blank=True)),
                ('multiple_select2', models.ManyToManyField(help_text=b'<p>Same as above, but with the Select2MultipleWidget widget.</p><p class="small text-info">The annoying "Hold down Control..." message that django automatically appends to this help text will be at last removed in django 1.6!</p>', to='demo_application.DragNDropChangelistExample', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Widgets example',
                'verbose_name_plural': 'Widgets example',
            },
        ),
        migrations.AddField(
            model_name='nestedinlineexample',
            name='popupinline',
            field=models.ForeignKey(to='demo_application.PopupInlineExample'),
        ),
    ]
