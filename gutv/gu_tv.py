# -*- coding: utf-8 -*-

#
#  gu_tv.py
#  
#  Copyright The GOLDS-UFSC Telemetry Viewer Contributors.
#  
#  This file is part of GOLDS-UFSC Telemetry Viewer.
#
#  GOLDS-UFSC Telemetry Viewer is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  GOLDS-UFSC Telemetry Viewer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with GOLDS-UFSC Telemetry Viewer; if not, see
#  <http://www.gnu.org/licenses/>.
#  
#

import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

import gutv.version

# UI File
_UI_FILE_LOCAL                  = os.path.abspath(os.path.dirname(__file__)) + '/data/ui/gutv.glade'
_UI_FILE_LINUX_SYSTEM           = '/usr/share/gutv/gutv.glade'

# Icon File
_ICON_FILE_LOCAL                = os.path.abspath(os.path.dirname(__file__)) + '/data/img/gutv_256x256.png'
_ICON_FILE_LINUX_SYSTEM         = '/usr/share/icons/gutv_256x256.png'

# Logo File
_LOGO_FILE_LOCAL                = os.path.abspath(os.path.dirname(__file__)) + '/data/img/spacelab-logo-full-400x200.png'
_LOGO_FILE_LINUX_SYSTEM         = '/usr/share/spacelab_decoder/spacelab-logo-full-400x200.png'

class GUTV:

    def __init__(self):
        """
        Main class constructor.

        :return: None
        """
        self.builder = Gtk.Builder()

        # UI file from Glade
        if os.path.isfile(_UI_FILE_LOCAL):
            self.builder.add_from_file(_UI_FILE_LOCAL)
        else:
            self.builder.add_from_file(_UI_FILE_LINUX_SYSTEM)

        self.builder.connect_signals(self)

        self._build_widgets()

    def _build_widgets(self):
        # Main window
        self.window = self.builder.get_object("window_main")
        if os.path.isfile(_ICON_FILE_LOCAL):
            self.window.set_icon_from_file(_ICON_FILE_LOCAL)
        else:
            self.window.set_icon_from_file(_ICON_FILE_LINUX_SYSTEM)
        self.window.set_wmclass(self.window.get_title(), self.window.get_title())
        self.window.connect("destroy", Gtk.main_quit)

        # About dialog
        self.aboutdialog = self.builder.get_object("aboutdialog_gutv")
        self.aboutdialog.set_version(gutv.version.__version__)
        if os.path.isfile(_LOGO_FILE_LOCAL):
            self.aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(_LOGO_FILE_LOCAL))
        else:
            self.aboutdialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(_LOGO_FILE_LINUX_SYSTEM))

        # About toolbutton
        self.toolbutton_about = self.builder.get_object("toolbutton_about")
        self.toolbutton_about.connect("clicked", self.on_toolbutton_about_clicked)


    def run(self):
        self.window.show_all()

        Gtk.main()

        return 0

    def destroy(window, self):
        Gtk.main_quit()

    def on_toolbutton_about_clicked(self, toolbutton):
        response = self.aboutdialog.run()

        if response == Gtk.ResponseType.DELETE_EVENT:
            self.aboutdialog.hide()
