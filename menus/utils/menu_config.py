import rumps


def build_rumps_menu(structure, parent=None):
    if parent is None:
        parent = []
    for item in structure:
        if len(item) == 3:
            title, content, is_selected = item
        else:
            title, content = item
            is_selected = False
        if title is None:
            # Add a separator
            if isinstance(parent, list):
                parent.append(None)
            else:
                parent.add(None)

        elif isinstance(content, list):
            submenu = rumps.MenuItem(title)
            build_rumps_menu(content, submenu)
            if isinstance(parent, list):
                parent.append(submenu)
            else:
                parent.add(submenu)
        else:
            item = rumps.MenuItem(title, content)
            item.state = is_selected
            if isinstance(parent, list):
                parent.append(item)
            else:
                parent.add(item)
    return parent
