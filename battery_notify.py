import os
tmp = os.popen('upower -i $(upower -e | grep BAT) | grep --color=never -E "percentage"').read()
# print tmp
tmp = tmp[-5:-2]
flag=True
try:
    a = int(tmp[1])
    if a>=1:
        flag=False
except:
    pass
if int(tmp[2])<=9 and flag and tmp!='100':
  os.system('DISPLAY=:0 notify-send "Low battery" \"Only '+tmp[2]+'% remaining.\"')
# else: os.system('DISPLAY=:0 notify-send "Peace!" \"A whole lot i.e. '+tmp+'% remaining.\"')

