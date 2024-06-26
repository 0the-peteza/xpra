#!/usr/bin/env python3
# This file is part of Xpra.
# Copyright (C) 2016 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.


def test_dbus(display, wid=1, flag=True):
    import dbus
    bus = dbus.SessionBus()
    server = 'org.xpra.Server%i' % display
    service = bus.get_object(server, "/org/xpra/Server")
    SetVideoRegionEnabled = service.get_dbus_method('SetVideoRegionEnabled', 'org.xpra.Server')
    print("calling %s.SetVideoRegionEnabled(%i, %s)" % (server, wid, flag))
    SetVideoRegionEnabled(wid, flag)


def main():
    import sys
    if len(sys.argv)!=4:
        print("usage: %s DISPLAY WID True|False" % sys.argv[0])
        return
    DISPLAY = int(sys.argv[1])
    wid = int(sys.argv[2])
    from xpra.scripts.config import str_to_bool
    flag = str_to_bool(sys.argv[3])
    test_dbus(DISPLAY, wid, flag)


if __name__ == "__main__":
    main()
