import os
import subprocess


# return output but doesn't support background command
def run(command, is_print=True):
    commands = [x for x in command.split(' ') if x != '']
    result = subprocess.run(commands, stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    if is_print:
        print(output)
    return output


# supports background command
def system_command(script, is_print=True):
    if is_print:
        print(f"\n****** {script} ******")
    os.system(script)
