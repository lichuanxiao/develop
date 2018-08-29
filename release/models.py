from django.db import models

# Create your models here.


class Relese(models.Model):
    """
    发布详情
    发布标题:
    发布编号：primary_key=True
    迭代版本：
    发布类型：常规上线、补丁
    发布时间:
    发布功能：1.2.3---
    附件:
    注：排序-发布时间
    """
    TEST = 'TEST'
    YL = 'YL'
    HD = 'HD'
    SC = 'SC'
    DEPLOY_ENV_CHOICES = (
    (TEST,"测试环境"),
    (YL,"演练环境"),
    (HD,"灰度环境"),
    (SC,"生产环境"),
    )

    RELEASE_TYPE_CHOICES = (
        ("nomal", "常规上线"),
        ("fixbug", "修复BUG"),
    )
    iterative_version = models.CharField(max_length=8, verbose_name="迭代版本")
    release_title = models.CharField(max_length=60, verbose_name="上线标题")
    release_num = models.CharField(max_length=12, verbose_name="上线编号", unique=True)
    release_type = models.CharField(max_length=10, verbose_name="发布类型", choices=RELEASE_TYPE_CHOICES, default="nomal")
    deploy_evn = models.CharField(max_length=4, choices=DEPLOY_ENV_CHOICES, default=YL)
    deploy_time = models.DateTimeField(auto_now_add=True)
    release_func = models.TextField()
    release_Attachments = models.FileField(upload_to="attachments/%Y/%m/%d/")


    class Meta:
        ordering = ["deploy_time"]
        verbose_name = "发布详情"


    def __str__(self):
        return self.release_title


class ReleaseProjectList(models.Model):
    """
    发布项目清单
    项目:
    项目组:
    发布编号:--关联发布信息表的编号
    项目产品版本:
    项目代码版本:
    注：排序方式-项目产品版本
    """
    project_id = models.IntegerField(verbose_name="项目 ID")
    group_id = models.IntegerField(verbose_name="项目组 ID")
    release_id = models.IntegerField(verbose_name="发布编号 ID")
    project_version = models.CharField(max_length=10, verbose_name="项目产品版本")
    project_version = models.CharField(max_length=40, verbose_name="项目代码版本")
    

    class Mate:
        verbose_name = "发布项目清单"
        ordering = ["project_version"]


class GroupInfo(models.Model):
    """
    项目组信息
    """
    group_name = models.CharField(max_length=30, verbose_name="组名", unique=True)
    group_url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=200, verbose_name='组描述', null=True, blank=True)

    def __str__(self):
        return self.group_name
    

class ProjectInfo(models.Model):
    """
    项目表，主要记录每个项目的详细信息
    """
    project_name = models.CharField(max_length=30, verbose_name="项目名称", unique=True)
    project_description = models.CharField(max_length=200, verbose_name="项目详细描述")
    project_url = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.project_name
