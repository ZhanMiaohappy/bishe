import xadmin
from .models import *
from xadmin import views

#配置用户信息表信息
class userInfoAdmin(object):
    list_display=[
        "userid", "username", "phonenum", "emailaddr", "roleid"
    ]
    list_per_page = 5  # 每页显示的个数
    show_detail_fields = ["username", "roleid"]  # 设置详情标识
    ordering = ("userid",)

#配置角色信息
class roleInfoAdmin(object):
    list_display=["roleid", "rolename"]
    show_detail_fields = ["roleid", "rolename"]  # 设置详情标识
    ordering = ("roleid",)

#配置英语类别表
class engtypeInfoAdmin(object):
    list_display=["engtypeid", "engtypename"]
    show_detail_fields = ["engtypeid", "engtypename"]  # 设置详情标识
    ordering = ("engtypeid",)

#配置英语模块表
class engmoduInfoAdmin(object):
    list_display=["engmoduid", "engmoduname", "teacher", "coursetime",
                  "limitnum", "costfee", "engtypeid" ]
    show_detail_fields = ["engmoduname", "engtypeid"]  # 设置详情标识
    ordering = ("engmoduid",)

#配置课程视频信息
class videoInfoAdmin(object):
    list_display=["videoid", "videoname", "engmoduid",
                  "videopath", "duration"]
    show_detail_fields = ["videoid", "videoname"]  # 设置详情标识
    ordering = ("videoid",)

#配置已购课程信息
class everbuyInfoAdmin(object):
    list_display=["everbuyid", "userid", "engmoduid",
                  "buytime"]
    show_detail_fields = ["everbuyid", "engmoduid"]  # 设置详情标识
    ordering = ("everbuyid",)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '在线英语学习系统'     #首页头
    site_footer = ''             #首页尾
    menu_style = 'default'           # "accordion

xadmin.site.register(userInfo, userInfoAdmin)
xadmin.site.register(engtypeInfo, engtypeInfoAdmin)
xadmin.site.register(engmoduInfo, engmoduInfoAdmin)
xadmin.site.register(videoInfo, videoInfoAdmin)
xadmin.site.register(everbuyInfo, everbuyInfoAdmin)
xadmin.site.register(roleInfo, roleInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
