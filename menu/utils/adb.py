import os
import re
import subprocess
import time
from datetime import datetime

from libraries import commands
from menu import settings


def device_series():
    devices = commands.run('adb devices', False).split('\n')
    devices = [x.strip() for x in devices if x.strip() != '' and 'offline' not in x]
    devices = [x for x in devices if len(re.split(r'[\s\t]', x)) == 2]
    devices = [x.replace('device', '').strip() for x in devices]

    return devices


def device_model(serial):
    return commands.run(f'adb -s {serial} shell getprop ro.product.model', False).strip()


def execute_to_all(action):
    devices = device_series()
    executed = False
    for device_id in devices:
        if device_id not in settings.devices_selection or settings.devices_selection[device_id] is True:
            action(device_id)
            executed = True
    return executed


def open_app(package_name):
    def action(device_id):
        return commands.run(f'adb -s {device_id} shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1')

    execute_to_all(action)


def uninstall(package_name):
    def action(device_id):
        commands.system_command(f'adb -s {device_id} uninstall {package_name}')

    execute_to_all(action)


def force_stop(package_name):
    def action(device_id):
        commands.system_command(f'adb -s {device_id} shell am force-stop {package_name}')

    execute_to_all(action)


def clear_data(package_name):
    def action(device_id):
        commands.system_command(f'adb -s {device_id} shell pm clear {package_name}')

    execute_to_all(action)


def clear_cache(package_name):
    def action(device_id):
        commands.system_command(f'adb -s {device_id} shell run-as {package_name} rm -fr cache')

    execute_to_all(action)


def open_link(link):
    link = escape_text(link)

    def action(device_id):
        commands.system_command(f'adb -s {device_id} shell am start -a android.intent.action.VIEW -d "{link}"')

    execute_to_all(action)


def open_activity(package_name, activity):
    def action(device_id):
        commands.system_command(f'adb -s {device_id} shell am start -n {package_name}/{activity}')

    execute_to_all(action)


def escape_text(processing_text):
    shell_special_chars = ['"', '`', ';', '&', '|', '*', '?', '<', '>', '^', '(', ')', '{', '}', '$', '!', '\\']
    for char in shell_special_chars:
        if char in processing_text:
            processing_text = processing_text.replace(char, f'\\{char}')

    return processing_text.replace(' ', '%s')


def input_text(text):
    text = escape_text(text)
    texts = text.split('\n')

    def action(device_id):
        for t in texts:
            commands.system_command(f'adb -s {device_id} shell input text {t}')
            commands.system_command(f'adb shell input keyevent 66')

    execute_to_all(action)


def screen_shoot(dest=settings.pc_output_path):
    dest = re.sub(r'/+$', '', dest)
    dest = dest.replace('~', os.path.expanduser('~'))
    dest = os.path.abspath(dest)

    def action(device_id):
        model = device_model(device_id)
        commands.system_command(f'mkdir -p {dest}/{model}')
        name = f'screenshot-{model}-{datetime.now().strftime("%y%m%d-%H%M%S")}.png'
        commands.system_command(f"adb -s {device_id} shell mkdir -p {settings.screen_shoot_device_path}")
        commands.system_command(f'adb -s {device_id} shell screencap -p "{settings.screen_shoot_device_path}/{name}"')
        commands.system_command(
            f'adb -s {device_id} pull "{settings.screen_shoot_device_path}/{name}" {dest}/{model}/.')
        commands.system_command(f'adb -s {device_id} shell rm "{settings.screen_shoot_device_path}/{name}"')

    if execute_to_all(action):
        commands.system_command(f'open {dest}')


def screen_record_stop(dest=settings.pc_output_path):
    dest = re.sub(r'/+$', '', dest)
    ps = commands.run('ps -ax', False)
    ps = ps.split('\n')
    for x in ps:
        if 'shell screenrecord' in x:
            pid = x.strip().split(' ')[0]
            os.kill(int(pid), 2)

    devices = device_series()
    if len(devices) == 0:
        return

    wait = 10
    print(f"waiting {wait}s")
    time.sleep(wait)

    def pull_recorded_video(device_id):
        model = device_model(device_id)
        commands.system_command(f'mkdir -p {dest}/{model}')
        commands.system_command(f'adb -s {device_id} pull {settings.record_device_path}/. {dest}/{model}/.')
        commands.system_command(f'adb -s {device_id} shell rm "{settings.record_device_path}/*"')

    for device_serial in devices:
        pull_recorded_video(device_serial)

    if len(devices) > 0:
        commands.system_command(f'open {dest}')


def screen_record_start():
    devices = device_series()
    if len(devices) == 0:
        return False

    def start_screen_record(device_serial):
        current = datetime.now().strftime("%y%m%d-%H%M%S")
        commands.run(f"adb -s {device_serial} shell mkdir -p {settings.record_device_path}")
        model = device_model(device_serial)
        command = f"adb -s {device_serial} shell screenrecord {settings.record_device_path}/record_{model}_{current}.mp4"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Recording started in the background, process ID:", process.pid)

    return execute_to_all(start_screen_record)
