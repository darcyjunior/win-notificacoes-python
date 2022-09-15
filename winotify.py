# https://pypi.org/project/winotify/
# pip install winotify

from winotify import Notification, audio

toast = Notification(app_id="windows app",
                     title="Winotify Test Toast",
                     msg="New Notification!",
                     icon=r"https://conceito.digital/wp-content/uploads/2020/06/Logotipo_Conceito-02_205x110.png")

toast.show()
