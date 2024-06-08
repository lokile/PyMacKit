#!/bin/bash

killall PyMacKit

rm -fr ./build
rm -fr dist
python setup.py py2app

LAUNCH_SCRIPT="$PWD/dist/PyMacKit.sh"

# Create the launch script with AppleScript embedded
cat <<EOF > "$LAUNCH_SCRIPT"
#!/bin/bash
open "$PWD/dist/PyMacKit.app"
EOF

# Make the script executable
chmod +x "$LAUNCH_SCRIPT"

# Use osascript to add the launch script as a login item
osascript <<EOF
tell application "System Events"
    set existingItems to path of every login item
    if ("$LAUNCH_SCRIPT" is not in existingItems) then
        make new login item at end with properties {path:"$LAUNCH_SCRIPT", hidden:false}
    end if
end tell
EOF

$LAUNCH_SCRIPT