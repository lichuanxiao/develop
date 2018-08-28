from django.db import models

# Create your models here.
class Relese(models.Model):
    """
    发布详情
    iterative_version: 迭代版本,标识本次发布属于哪个迭代
    release_title: 发布标题
    deploy: 标识该次发布部署的环境
    deploy_time：标识该次部署具体时间
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

    iterative_version = models.CharField(max_length=8, verbose_name="迭代版本")
    release_title = models.CharField(max_length=60, verbose_name="上线标题")
    deploy_evn = models.CharField(max_length=4, choices=DEPLOY_ENV_CHOICES, default=YL)
    deploy_time = models.DateTimeField(auto_now=True)
    release_func = models.TextField()
    


    def __str__(self):
        return self.release_title

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
    project_name = models.CharField(max_length=30, verbose_name="项目名称")
    group = models.ForeignKey(GroupInfo, to_field='group_name', on_delete=models.PROTECT)
