from menus import settings
from menus.utils import adb

is_recording = False


def load_screen_record_menu():
    global is_recording
    if is_recording is True:
        return ('🟥 Stop Record', android_screen_record_stop)
    else:
        return ('🟢 Start Record', android_screen_record_start)


def android_screen_record_start(sender):
    global is_recording
    if adb.screen_record_start() is True:
        is_recording = True
        settings.MainMenu.title = "(🔴) Recording..."
        settings.MainMenu.load_menu()


def android_screen_record_stop(sender):
    global is_recording
    adb.screen_record_stop()
    settings.MainMenu.title = settings.app_title
    is_recording = False
    settings.MainMenu.load_menu()
