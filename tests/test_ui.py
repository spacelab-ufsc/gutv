#
#  test_ui.py
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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def test_ui():
    builder = Gtk.Builder()
    builder.add_from_file("gutv/data/ui/gutv.glade")

    # Main window
    window                          = builder.get_object("window_main")
    button_preferences              = builder.get_object("button_preferences")
    entry_address                   = builder.get_object("entry_address")
    entry_port                      = builder.get_object("entry_port")
    togglebutton_open_socket        = builder.get_object("togglebutton_open_socket")
    button_close_socket             = builder.get_object("button_close_socket")
    toolbutton_about                = builder.get_object("toolbutton_about")
    label_eps_mcu_date              = builder.get_object("label_eps_mcu_date")
    label_eps_mcu_time              = builder.get_object("label_eps_mcu_time")
    label_eps_mcu_temp              = builder.get_object("label_eps_mcu_temp")
    label_eps_mcu_curr              = builder.get_object("label_eps_mcu_curr")
    label_eps_mcu_last_reset_cause  = builder.get_object("label_eps_mcu_last_reset_cause")
    label_eps_mcu_reset_count       = builder.get_object("label_eps_mcu_reset_count")
    label_eps_sp_volt_mypx          = builder.get_object("label_eps_sp_volt_mypx")
    label_eps_sp_volt_mxpz          = builder.get_object("label_eps_sp_volt_mxpz")
    label_eps_sp_volt_mzpy          = builder.get_object("label_eps_sp_volt_mzpy")
    label_eps_sp_curr_mx            = builder.get_object("label_eps_sp_curr_mx")
    label_eps_sp_curr_px            = builder.get_object("label_eps_sp_curr_px")
    label_eps_sp_curr_my            = builder.get_object("label_eps_sp_curr_my")
    label_eps_sp_curr_py            = builder.get_object("label_eps_sp_curr_py")
    label_eps_sp_curr_mz            = builder.get_object("label_eps_sp_curr_mz")
    label_eps_sp_curr_pz            = builder.get_object("label_eps_sp_curr_pz")
    label_eps_mppt_dc_ch_1          = builder.get_object("label_eps_mppt_dc_ch_1")
    label_eps_mppt_dc_ch_2          = builder.get_object("label_eps_mppt_dc_ch_2")
    label_eps_mppt_dc_ch_3          = builder.get_object("label_eps_mppt_dc_ch_3")
    label_eps_mppt_mode_ch_1        = builder.get_object("label_eps_mppt_mode_ch_1")
    label_eps_mppt_mode_ch_2        = builder.get_object("label_eps_mppt_mode_ch_2")
    label_eps_mppt_mode_ch_3        = builder.get_object("label_eps_mppt_mode_ch_3")
    label_eps_mppt_output_volt      = builder.get_object("label_eps_mppt_output_volt")
    label_eps_rtd_ch_0              = builder.get_object("label_eps_rtd_ch_0")
    label_eps_rtd_ch_1              = builder.get_object("label_eps_rtd_ch_1")
    label_eps_rtd_ch_2              = builder.get_object("label_eps_rtd_ch_2")
    label_eps_rtd_ch_3              = builder.get_object("label_eps_rtd_ch_3")
    label_eps_rtd_ch_4              = builder.get_object("label_eps_rtd_ch_4")
    label_eps_rtd_ch_5              = builder.get_object("label_eps_rtd_ch_5")
    label_eps_rtd_ch_6              = builder.get_object("label_eps_rtd_ch_6")
    label_eps_bat_volt              = builder.get_object("label_eps_bat_volt")
    label_eps_bat_curr              = builder.get_object("label_eps_bat_curr")
    label_eps_bat_average_curr      = builder.get_object("label_eps_bat_average_curr")
    label_eps_bat_acc_curr          = builder.get_object("label_eps_bat_acc_curr")
    label_eps_bat_charge            = builder.get_object("label_eps_bat_charge")
    label_eps_bat_heater_1_dc       = builder.get_object("label_eps_bat_heater_1_dc")
    label_eps_bat_heater_2_dc       = builder.get_object("label_eps_bat_heater_2_dc")
    label_eps_bat_heater_1_mode     = builder.get_object("label_eps_bat_heater_1_mode")
    label_eps_bat_heater_2_mode     = builder.get_object("label_eps_bat_heater_2_mode")
    label_eps_bat_temp_monitor      = builder.get_object("label_eps_bat_temp_monitor")
    label_eps_bat_status            = builder.get_object("label_eps_bat_status")
    label_eps_bat_protection        = builder.get_object("label_eps_bat_protection")
    label_eps_bat_cycle_counter     = builder.get_object("label_eps_bat_cycle_counter")
    label_eps_bat_raac              = builder.get_object("label_eps_bat_raac")
    label_eps_bat_rsac              = builder.get_object("label_eps_bat_rsac")
    label_eps_bat_rarc              = builder.get_object("label_eps_bat_rarc")
    label_eps_bat_rsrc              = builder.get_object("label_eps_bat_rsrc")

    assert window                           != None
    assert button_preferences               != None
    assert entry_address                    != None
    assert entry_port                       != None
    assert togglebutton_open_socket         != None
    assert button_close_socket              != None
    assert toolbutton_about                 != None
    assert label_eps_mcu_date               != None
    assert label_eps_mcu_time               != None
    assert label_eps_mcu_temp               != None
    assert label_eps_mcu_curr               != None
    assert label_eps_mcu_last_reset_cause   != None
    assert label_eps_mcu_reset_count        != None
    assert label_eps_sp_volt_mypx           != None
    assert label_eps_sp_volt_mxpz           != None
    assert label_eps_sp_volt_mzpy           != None
    assert label_eps_sp_curr_mx             != None
    assert label_eps_sp_curr_px             != None
    assert label_eps_sp_curr_my             != None
    assert label_eps_sp_curr_py             != None
    assert label_eps_sp_curr_mz             != None
    assert label_eps_sp_curr_pz             != None
    assert label_eps_mppt_dc_ch_1           != None
    assert label_eps_mppt_dc_ch_2           != None
    assert label_eps_mppt_dc_ch_3           != None
    assert label_eps_mppt_mode_ch_1         != None
    assert label_eps_mppt_mode_ch_2         != None
    assert label_eps_mppt_mode_ch_3         != None
    assert label_eps_mppt_output_volt       != None
    assert label_eps_rtd_ch_0               != None
    assert label_eps_rtd_ch_1               != None
    assert label_eps_rtd_ch_2               != None
    assert label_eps_rtd_ch_3               != None
    assert label_eps_rtd_ch_4               != None
    assert label_eps_rtd_ch_5               != None
    assert label_eps_rtd_ch_6               != None
    assert label_eps_bat_volt               != None
    assert label_eps_bat_curr               != None
    assert label_eps_bat_average_curr       != None
    assert label_eps_bat_acc_curr           != None
    assert label_eps_bat_charge             != None
    assert label_eps_bat_heater_1_dc        != None
    assert label_eps_bat_heater_2_dc        != None
    assert label_eps_bat_heater_1_mode      != None
    assert label_eps_bat_heater_2_mode      != None
    assert label_eps_bat_temp_monitor       != None
    assert label_eps_bat_status             != None
    assert label_eps_bat_protection         != None
    assert label_eps_bat_cycle_counter      != None
    assert label_eps_bat_raac               != None
    assert label_eps_bat_rsac               != None
    assert label_eps_bat_rarc               != None
    assert label_eps_bat_rsrc               != None
