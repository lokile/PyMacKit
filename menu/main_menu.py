import rumps

from menu import settings
from menu.sub_menu.android_devices_menu import load_android_devices
from menu.sub_menu.screen_record_menu import load_screen_record_menu
from menu.utils import menu_actions as actions
from menu.utils.menu_config import build_rumps_menu


class PyMacKit(rumps.App):
    def __init__(self):
        super(PyMacKit, self).__init__(settings.app_title, quit_button=None)
        self.load_menu()

    def load_menu(self, sender=None):
        config_menu = [
            ('🍥 Refresh', self.load_menu),
            ("✅ Selected Devices", load_android_devices()),
            (None, None),
            ('📲 SnapScreen', actions.screen_shoot),
            load_screen_record_menu(),

            (None, None),
            ('Open App', actions.open_app),
            ('Force Stop', actions.force_app_stop),
            (None, None),
            ('🫥 Uninstall', [
                ('Clear cache', actions.clear_app_cache),
                (None, None),
                ('Clear data', actions.clear_app_data),
                ('Uninstall', actions.uninstall)
            ]),
            (None, None),
            ('🌀 Open Link', actions.open_link_popup),
            ('✏️ Text to devices', actions.send_text_to_device_popup),
            (None, None),
            ("Quit", rumps.quit_application)
        ]

        self.menu.clear()
        self.menu = build_rumps_menu(config_menu)
