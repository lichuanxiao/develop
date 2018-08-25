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
    DEPLOY_ENV_CHOICES = (
    (TEST,"测试环境"),
    (YL,"演练环境"),
    (HD,"灰度环境"),
    (SC,"生产环境"),
    )

    iterative_version = models.CharField(max_length=8, verbose_name="迭代版本")
    release_title = models.CharField(max_length=60, verbose_name="上线标题")
    deploy_evn = models.CharField(max_length=5, choices=DEPLOY_ENV_CHOICES, default=YL)
    
