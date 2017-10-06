import os

tmp = os.popen('upower -i $(upower -e | grep BAT) | grep --color=never -E "percentage"').read()
check = os.popen('upower -i $(upower -e | grep BAT) | grep --color=never -E "state"').read()
check = check.strip().find("discharging")  # check if battery is being charged or not
tmp = tmp[-4:-2]

if int(tmp) < 10 and check != -1:
  os.system('DISPLAY=:0 notify-send "Low battery" \"Only '+tmp+'% remaining.\"')
# else: os.system('DISPLAY=:0 notify-send "Peace!" \"A whole lot i.e. '+tmp+'% remaining.\"')

