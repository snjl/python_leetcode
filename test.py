import apprise
apobj = apprise.Apprise()
apobj.add('windows://')
apobj.notify(
    title=('站 %s 有%s条更新' % (1, 2)),
    body=('首条标题：%s，时间：%s' % (1, 2)),

)
import platform
print('windows' in platform.system().lower())
try:
    2 == 0
except Exception as e:
    print(e)

