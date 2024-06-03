import re

import rumps

from menus import settings
from menus.utils import adb


def send_text_to_device_popup(sender):
    response = rumps.Window(
        title='Text',
        message='Avoid special characters',
        ok='Submit',
        cancel='Cancel'
    ).run()
    if response.clicked:
        adb.input_text(response.text)


def open_link_popup(sender):
    response = rumps.Window(
        title='Deeplink',
        message='Enter the link',
        ok='Submit',
        cancel='Cancel'
    ).run()
    if response.clicked:
        link = response.text
        link = re.sub(r'^(http(s)?://)?(www\\.)?', 'https://', link)
        adb.open_link(link)


def input_text(text):
    adb.input_text(text)


def open_app(sender):
    adb.open_app(settings.package_name)


def force_app_stop(sender):
    adb.force_stop(settings.package_name)


def clear_app_cache(sender):
    adb.clear_cache(settings.package_name)


def clear_app_data(sender):
    adb.clear_data(settings.package_name)


def uninstall(sender):
    adb.uninstall(settings.package_name)


def screen_shoot(sender):
    adb.screen_shoot()


def open_google_subscription(sender):
    adb.open_link('https://play.google.com/store/account/subscriptions')
