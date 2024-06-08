from functools import partial

from menu import settings
from menu.utils import adb


def load_android_devices():
    devices = adb.device_series()
    for device_id in devices:
        settings.devices_selection[device_id] = device_id not in settings.devices_selection or \
                                                settings.devices_selection[device_id]

    def on_selection_changed(sender, d_id):
        settings.devices_selection[d_id] = not settings.devices_selection[d_id]
        settings.MainMenu.load_menu()

    return [(adb.device_model(x), partial(on_selection_changed, d_id=x), settings.devices_selection[x])
            for x in adb.device_series()]
