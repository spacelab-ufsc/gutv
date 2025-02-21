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
import json

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

import gutv.version
import gutv.convert

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

        # EPS tab
        self.label_eps_mcu_date             = self.builder.get_object("label_eps_mcu_date")
        self.label_eps_mcu_time             = self.builder.get_object("label_eps_mcu_time")
        self.label_eps_mcu_temp             = self.builder.get_object("label_eps_mcu_temp")
        self.label_eps_mcu_curr             = self.builder.get_object("label_eps_mcu_curr")
        self.label_eps_mcu_last_reset_cause = self.builder.get_object("label_eps_mcu_last_reset_cause")
        self.label_eps_mcu_reset_count      = self.builder.get_object("label_eps_mcu_reset_count")
        self.label_eps_sp_volt_mypx         = self.builder.get_object("label_eps_sp_volt_mypx")
        self.label_eps_sp_volt_mxpz         = self.builder.get_object("label_eps_sp_volt_mxpz")
        self.label_eps_sp_volt_mzpy         = self.builder.get_object("label_eps_sp_volt_mzpy")
        self.label_eps_sp_curr_mx           = self.builder.get_object("label_eps_sp_curr_mx")
        self.label_eps_sp_curr_px           = self.builder.get_object("label_eps_sp_curr_px")
        self.label_eps_sp_curr_my           = self.builder.get_object("label_eps_sp_curr_my")
        self.label_eps_sp_curr_py           = self.builder.get_object("label_eps_sp_curr_py")
        self.label_eps_sp_curr_mz           = self.builder.get_object("label_eps_sp_curr_mz")
        self.label_eps_sp_curr_pz           = self.builder.get_object("label_eps_sp_curr_pz")
        self.label_eps_mppt_dc_ch_1         = self.builder.get_object("label_eps_mppt_dc_ch_1")
        self.label_eps_mppt_dc_ch_2         = self.builder.get_object("label_eps_mppt_dc_ch_2")
        self.label_eps_mppt_dc_ch_3         = self.builder.get_object("label_eps_mppt_dc_ch_3")
        self.label_eps_mppt_mode_ch_1       = self.builder.get_object("label_eps_mppt_mode_ch_1")
        self.label_eps_mppt_mode_ch_2       = self.builder.get_object("label_eps_mppt_mode_ch_2")
        self.label_eps_mppt_mode_ch_3       = self.builder.get_object("label_eps_mppt_mode_ch_3")
        self.label_eps_mppt_output_volt     = self.builder.get_object("label_eps_mppt_output_volt")
        self.label_eps_rtd_ch_0             = self.builder.get_object("label_eps_rtd_ch_0")
        self.label_eps_rtd_ch_1             = self.builder.get_object("label_eps_rtd_ch_1")
        self.label_eps_rtd_ch_2             = self.builder.get_object("label_eps_rtd_ch_2")
        self.label_eps_rtd_ch_3             = self.builder.get_object("label_eps_rtd_ch_3")
        self.label_eps_rtd_ch_4             = self.builder.get_object("label_eps_rtd_ch_4")
        self.label_eps_rtd_ch_5             = self.builder.get_object("label_eps_rtd_ch_5")
        self.label_eps_rtd_ch_6             = self.builder.get_object("label_eps_rtd_ch_6")
        self.label_eps_bat_volt             = self.builder.get_object("label_eps_bat_volt")
        self.label_eps_bat_curr             = self.builder.get_object("label_eps_bat_curr")
        self.label_eps_bat_average_curr     = self.builder.get_object("label_eps_bat_average_curr")
        self.label_eps_bat_acc_curr         = self.builder.get_object("label_eps_bat_acc_curr")
        self.label_eps_bat_charge           = self.builder.get_object("label_eps_bat_charge")
        self.label_eps_bat_heater_1_dc      = self.builder.get_object("label_eps_bat_heater_1_dc")
        self.label_eps_bat_heater_2_dc      = self.builder.get_object("label_eps_bat_heater_2_dc")
        self.label_eps_bat_heater_1_mode    = self.builder.get_object("label_eps_bat_heater_1_mode")
        self.label_eps_bat_heater_2_mode    = self.builder.get_object("label_eps_bat_heater_2_mode")
        self.label_eps_bat_temp_monitor     = self.builder.get_object("label_eps_bat_temp_monitor")
        self.label_eps_bat_status           = self.builder.get_object("label_eps_bat_status")
        self.label_eps_bat_protection       = self.builder.get_object("label_eps_bat_protection")
        self.label_eps_bat_cycle_counter    = self.builder.get_object("label_eps_bat_cycle_counter")
        self.label_eps_bat_raac             = self.builder.get_object("label_eps_bat_raac")
        self.label_eps_bat_rsac             = self.builder.get_object("label_eps_bat_rsac")
        self.label_eps_bat_rarc             = self.builder.get_object("label_eps_bat_rarc")
        self.label_eps_bat_rsrc             = self.builder.get_object("label_eps_bat_rsrc")

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

    def _decode_pkt(self, pkt_json):
        data = json.loads(pkt_json)[0]

        if "eps_timestamp" in data:
            self.label_eps_mcu_date.set_text(convert.convert_epoch_to_date(int(data["eps_timestamp"])))
            self.label_eps_mcu_time.set_text(convert.convert_epoch_to_time(int(data["eps_timestamp"])))

        if "eps_mcu_temp" in data:
            self.label_eps_mcu_temp.set_text(str(convert.convert_temp_kelvin_to_celsius(int(data["eps_mcu_temp"]))) + " " + "°C")

        if "eps_mcu_curr" in data:
            self.label_eps_mcu_curr.set_text(data["eps_mcu_curr"] + " " + "mA")

        if "eps_mcu_last_rst_cause" in data:
            self.label_eps_mcu_last_reset_cause.set_text(data["eps_mcu_last_rst_cause"])

        if "eps_mcu_rst_counter" in data:
            self.label_eps_mcu_reset_count.set_text(data["eps_mcu_rst_counter"])

        if "eps_sp_volt_mypx" in data:
            self.label_eps_sp_volt_mypx.set_text()

        if "eps_sp_volt_mxpz" in data:
            self.label_eps_sp_volt_mxpz.set_text()

        if "eps_sp_volt_mzpy" in data:
            self.label_eps_sp_volt_mzpy.set_text()

        if "eps_sp_curr_mx" in data:
            self.label_eps_sp_curr_mx.set_text()

        if "eps_sp_curr_px" in data:
            self.label_eps_sp_curr_px.set_text()

        if "eps_sp_curr_my" in data:
            self.label_eps_sp_curr_my.set_text()

        if "eps_sp_curr_py" in data:
            self.label_eps_sp_curr_py.set_text()

        if "eps_sp_curr_mz" in data:
            self.label_eps_sp_curr_mz.set_text()

        if "eps_sp_curr_pz" in data:
            self.label_eps_sp_curr_pz.set_text()

        if "eps_mppt_1_dc" in data:
            self.label_eps_mppt_dc_ch_1.set_text()

        if "eps_mppt_2_dc" in data:
            self.label_eps_mppt_dc_ch_2.set_text()

        if "eps_mppt_3_dc" in data:
            self.label_eps_mppt_dc_ch_3.set_text()

        if "" in data:
            self.label_eps_mppt_mode_ch_1.set_text()

        if "" in data:
            self.label_eps_mppt_mode_ch_2.set_text()

        if "" in data:
            self.label_eps_mppt_mode_ch_3.set_text()

        if "" in data:
            self.label_eps_mppt_output_volt.set_text()

        if "" in data:
            self.label_eps_rtd_ch_0.set_text()

        if "" in data:
            self.label_eps_rtd_ch_1.set_text()

        if "" in data:
            self.label_eps_rtd_ch_2.set_text()

        if "" in data:
            self.label_eps_rtd_ch_3.set_text()

        if "" in data:
            self.label_eps_rtd_ch_4.set_text()

        if "" in data:
            self.label_eps_rtd_ch_5.set_text()

        if "" in data:
            self.label_eps_rtd_ch_6.set_text()

        if "" in data:
            self.label_eps_bat_volt.set_text()

        if "" in data:
            self.label_eps_bat_curr.set_text()

        if "" in data:
            self.label_eps_bat_average_curr.set_text()

        if "" in data:
            self.label_eps_bat_acc_curr.set_text()

        if "" in data:
            self.label_eps_bat_charge.set_text()

        if "" in data:
            self.label_eps_bat_heater_1_dc.set_text()

        if "" in data:
            self.label_eps_bat_heater_2_dc.set_text()

        if "" in data:
            self.label_eps_bat_heater_1_mode.set_text()

        if "" in data:
            self.label_eps_bat_heater_2_mode.set_text()

        if "" in data:
            self.label_eps_bat_temp_monitor.set_text()

        if "" in data:
            self.label_eps_bat_status.set_text()

        if "" in data:
            self.label_eps_bat_protection.set_text()

        if "" in data:
            self.label_eps_bat_cycle_counter.set_text()

        if "" in data:
            self.label_eps_bat_raac.set_text()

        if "" in data:
            self.label_eps_bat_rsac.set_text()

        if "" in data:
            self.label_eps_bat_rarc.set_text()

        if "" in data:
            self.label_eps_bat_rsrc.set_text()

    def _load_default_values_eps(self):
        self.label_eps_mcu_date.set_text("1970/01/01")
        self.label_eps_mcu_time.set_text("00:00:00")
        self.label_eps_mcu_temp.set_text("0 °C")
        self.label_eps_mcu_curr.set_text("0 mA")
        self.label_eps_mcu_last_reset_cause.set_text("0")
        self.label_eps_mcu_reset_count.set_text("0")
        self.label_eps_sp_volt_mypx.set_text("0 mV")
        self.label_eps_sp_volt_mxpz.set_text("0 mV")
        self.label_eps_sp_volt_mzpy.set_text("0 mV")
        self.label_eps_sp_curr_mx.set_text("0 mA")
        self.label_eps_sp_curr_px.set_text("0 mA")
        self.label_eps_sp_curr_my.set_text("0 mA")
        self.label_eps_sp_curr_py.set_text("0 mA")
        self.label_eps_sp_curr_mz.set_text("0 mA")
        self.label_eps_sp_curr_pz.set_text("0 mA")
        self.label_eps_mppt_dc_ch_1.set_text("0 %")
        self.label_eps_mppt_dc_ch_2.set_text("0 %")
        self.label_eps_mppt_dc_ch_3.set_text("0 %")
        self.label_eps_mppt_mode_ch_1.set_text("Automatic")
        self.label_eps_mppt_mode_ch_2.set_text("Automatic")
        self.label_eps_mppt_mode_ch_3.set_text("Automatic")
        self.label_eps_mppt_output_volt.set_text("0 mV")
        self.label_eps_rtd_ch_0.set_text("0 °C")
        self.label_eps_rtd_ch_1.set_text("0 °C")
        self.label_eps_rtd_ch_2.set_text("0 °C")
        self.label_eps_rtd_ch_3.set_text("0 °C")
        self.label_eps_rtd_ch_4.set_text("0 °C")
        self.label_eps_rtd_ch_5.set_text("0 °C")
        self.label_eps_rtd_ch_6.set_text("0 °C")
        self.label_eps_bat_volt.set_text("0 mV")
        self.label_eps_bat_curr.set_text("0 mA")
        self.label_eps_bat_average_curr.set_text("0 mA")
        self.label_eps_bat_acc_curr.set_text("0 mA")
        self.label_eps_bat_charge.set_text("0 mAh")
        self.label_eps_bat_heater_1_dc.set_text("0 %")
        self.label_eps_bat_heater_2_dc.set_text("0 %")
        self.label_eps_bat_heater_1_mode.set_text("Automatic")
        self.label_eps_bat_heater_2_mode.set_text("Automatic")
        self.label_eps_bat_temp_monitor.set_text("0 °C")
        self.label_eps_bat_status.set_text("-")
        self.label_eps_bat_protection.set_text("-")
        self.label_eps_bat_cycle_counter.set_text("0")
        self.label_eps_bat_raac.set_text("0 mAh")
        self.label_eps_bat_rsac.set_text("0 mAh")
        self.label_eps_bat_rarc.set_text("0 %")
        self.label_eps_bat_rsrc.set_text("0 %")
