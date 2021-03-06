# Generated by Django 2.0.7 on 2018-08-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, unique=True, verbose_name='组名')),
                ('group_url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='组描述')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, unique=True, verbose_name='项目名称')),
                ('project_description', models.CharField(max_length=200, verbose_name='项目详细描述')),
                ('project_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseProjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(verbose_name='项目 ID')),
                ('group_id', models.IntegerField(verbose_name='项目组 ID')),
                ('release_id', models.IntegerField(verbose_name='发布编号 ID')),
                ('project_version', models.CharField(max_length=40, verbose_name='项目代码版本')),
            ],
        ),
        migrations.CreateModel(
            name='Relese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iterative_version', models.CharField(max_length=8, verbose_name='迭代版本')),
                ('release_title', models.CharField(max_length=60, verbose_name='上线标题')),
                ('release_num', models.CharField(max_length=12, unique=True, verbose_name='上线编号')),
                ('release_type', models.CharField(choices=[('nomal', '常规上线'), ('fixbug', '修复BUG')], default='nomal', max_length=10, verbose_name='发布类型')),
                ('deploy_evn', models.CharField(choices=[('TEST', '测试环境'), ('YL', '演练环境'), ('HD', '灰度环境'), ('SC', '生产环境')], default='YL', max_length=4)),
                ('deploy_time', models.DateTimeField(auto_now_add=True)),
                ('release_func', models.TextField()),
                ('release_Attachments', models.FileField(upload_to='attachments/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': '发布详情',
                'ordering': ['deploy_time'],
            },
        ),
    ]
