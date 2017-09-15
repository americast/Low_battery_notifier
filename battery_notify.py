import os
tmp = os.popen('upower -i $(upower -e | grep BAT) | grep --color=never -E "percentage"').read()
# print tmp
tmp = tmp[-4:-2]
flag=True
try:
    a = int(tmp[0])
    if a>=1:
        flag=False
except:
    pass
if int(tmp[1])<=9 and flag:
  os.system('DISPLAY=:0 notify-send "low battery"')
