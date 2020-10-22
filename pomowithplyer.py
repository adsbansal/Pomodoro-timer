import time
import datetime as dt
from plyer import notification

pomintues = 25
timenow = dt.datetime.now()
secspomo = pomintues * 60
delta = dt.timedelta(0, secspomo)
endtime = timenow + delta

notification.notify(
    title="Pomo has Started - HUSTLE!!",
    message="Time right now, {timrn}\nPomo will end after 25 Mins,"
            " {timethen}".format(timrn=timenow.strftime("%H:%M"), timethen=endtime.strftime("%H:%M")),
    app_icon="246x0w.ico",
    timeout=50

)

time.sleep(secspomo)

brie = 5
timenow = dt.datetime.now()
trans = dt.timedelta(0, brie * 60)
breaktime = timenow + trans

notification.notify(
    title="Break Time!!",
    message="ENJOY!!\nBreak time lasts till - {}".format(breaktime.strftime("%H:%M")),
    app_icon="246x0w.ico",
    timeout=10
)
time.sleep(brie * 60)

notification.notify(
    title="Pomo Ended",
    message="Start the app again if you want to do it again",
    app_icon="246x0w.ico",
    timeout=10
)
