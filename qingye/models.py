from django.db import models
from datetime import datetime

# Create your models here.
#用户信息表
class userInfo(models.Model):
    userid=models.AutoField(primary_key=True, verbose_name="用户名称")
    username=models.CharField(max_length=20, verbose_name="用户姓名")
    password=models.CharField(max_length=20, verbose_name="密码")
    phonenum=models.CharField(max_length=20, verbose_name="电话号码")
    emailaddr=models.CharField(max_length=200, verbose_name="邮箱地址")
    roleid=models.ForeignKey("roleInfo", verbose_name="角色名称", on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    class Meta():
        db_table='userinfo'
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

#角色信息表
class roleInfo(models.Model):
    roleid=models.AutoField(primary_key=True, verbose_name="角色编号")
    rolename=models.CharField(max_length=20, verbose_name="角色名称")
    def __str__(self):
        return self.rolename
    class Meta():
        db_table="roleinfo"
        verbose_name="角色信息"
        verbose_name_plural=verbose_name

#英语类别表
class engtypeInfo(models.Model):
    engtypeid=models.AutoField(primary_key=True, verbose_name="类别编号")
    engtypename=models.CharField(max_length=200, verbose_name="类别名称")
    def __str__(self):
        return self.engtypename
    class Meta():
        db_table="engtypeinfo"
        verbose_name="英语类别信息"
        verbose_name_plural=verbose_name

#英语模块表
class engmoduInfo(models.Model):
    engmoduid=models.AutoField(primary_key=True,verbose_name="模块编号")
    engmoduname=models.CharField(max_length=20, verbose_name="模块名称")
    teacher=models.CharField(max_length=200, verbose_name="教师名称")
    coursetime=models.CharField(max_length=200, verbose_name="上课时间")
    limitnum=models.IntegerField(default=1000, null=True, blank=True, verbose_name="限购人数")
    costfee=models.IntegerField(default=199, null=True, blank=True, verbose_name="购买金额")
    engtypeid=models.ForeignKey("engtypeInfo", verbose_name="类别名称", on_delete=models.CASCADE)
    def __str__(self):
        return self.engmoduname+" "+"（"+self.engtypeid.engtypename+"）"
    class Meta():
        db_table="engmoduinfo"
        verbose_name="英语模块信息"
        verbose_name_plural=verbose_name

#课程视频信息
class videoInfo(models.Model):
    videoid=models.AutoField(primary_key=True, verbose_name="视频编号")
    videoname=models.CharField(max_length=200, verbose_name="视频名称")
    engmoduid=models.ForeignKey("engmoduInfo", verbose_name="模块名称", on_delete=models.CASCADE)
    videopath=models.TextField(null=True, blank=True)
    duration=models.CharField(max_length=20)
    def __str__(self):
        return self.videoname
    class Meta():
        db_table="videoinfo"
        verbose_name="学习视频信息"
        verbose_name_plural=verbose_name


#已购课程信息
class everbuyInfo(models.Model):
    everbuyid=models.AutoField(primary_key=True, verbose_name="已购编号")
    userid=models.ForeignKey("userInfo", verbose_name="用户名称", on_delete=models.CASCADE)
    engmoduid=models.ForeignKey("engmoduInfo", verbose_name="英语模块名称", on_delete=models.CASCADE)
    buytime=models.DateTimeField(default=datetime.now(), null=True, blank=True, verbose_name="购买时间")
    def __str__(self):
        return str(self.everbuyid)
    class Meta():
        db_table="everbuyinfo"
        verbose_name="已购课程"
        verbose_name_plural=verbose_name