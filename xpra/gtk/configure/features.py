# This file is part of Xpra.
# Copyright (C) 2018-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import gi

from xpra.gtk.dialogs.base_gui_window import BaseGUIWindow
from xpra.gtk.widget import label
from xpra.log import Logger

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

log = Logger("util")


class ConfigureGUI(BaseGUIWindow):

    def __init__(self, parent:Gtk.Window|None=None):
        super().__init__(
            "Configure Xpra's Features",
            "features.png",
            wm_class=("xpra-configure-features-gui", "Xpra Configure Features GUI"),
            default_size=(640, 300),
            header_bar=(True, False),
            parent=parent,
        )

    def populate(self):
        self.add_widget(label("Configure Xpra Features", font="sans 20"))
        self.add_widget(label("This dialog allows you to turn on or off whole subsystems", font="sans 14"))



def main() -> int:
    from xpra.gtk.configure.main import run_gui
    return run_gui(ConfigureGUI)

if __name__ == "__main__":
    import sys
    sys.exit(main())
