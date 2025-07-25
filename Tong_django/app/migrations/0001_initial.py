# Generated by Django 5.2 on 2025-05-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                ("content", models.CharField(max_length=512, verbose_name="评论内容")),
                (
                    "parent_id",
                    models.IntegerField(
                        db_comment="为空即顶级评论", null=True, verbose_name="父评论ID"
                    ),
                ),
                ("post_id", models.IntegerField(verbose_name="评论帖子ID")),
                ("user_id", models.IntegerField(verbose_name="评论用户ID")),
            ],
            options={
                "verbose_name": "评论模型",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                ("content", models.TextField(max_length=2000, verbose_name="帖子内容")),
                (
                    "type",
                    models.SmallIntegerField(
                        db_comment="0文字(默认)-1图片-2视频",
                        default=0,
                        verbose_name="帖子类型",
                    ),
                ),
                ("page_view", models.IntegerField(default=0, verbose_name="浏览量")),
                ("images", models.TextField(null=True, verbose_name="帖子图片")),
                (
                    "videos",
                    models.CharField(
                        max_length=255, null=True, verbose_name="帖子视频"
                    ),
                ),
                (
                    "location",
                    models.CharField(max_length=128, null=True, verbose_name="定位"),
                ),
                ("is_top", models.BooleanField(default=False, verbose_name="是否置顶")),
                (
                    "status",
                    models.BooleanField(
                        db_comment="True发布False草稿",
                        default=True,
                        verbose_name="发布状态",
                    ),
                ),
                ("user_id", models.IntegerField(verbose_name="发布用户ID")),
            ],
            options={
                "verbose_name": "文章模型",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "openid",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="微信用户openid"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=16, null=True, verbose_name="用户名"),
                ),
                (
                    "avatar_url",
                    models.CharField(
                        max_length=255, null=True, verbose_name="头像路径"
                    ),
                ),
                (
                    "introduction",
                    models.CharField(
                        max_length=128, null=True, verbose_name="个人介绍"
                    ),
                ),
                (
                    "sex",
                    models.BooleanField(
                        db_comment="True男False女", null=True, verbose_name="性别"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=11, null=True, unique=True, verbose_name="手机号"
                    ),
                ),
                ("birthday", models.DateField(null=True, verbose_name="生日")),
            ],
            options={
                "verbose_name": "用户模型",
            },
        ),
    ]
