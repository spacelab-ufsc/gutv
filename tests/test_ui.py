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
    window                              = builder.get_object("window_main")
    button_preferences                  = builder.get_object("button_preferences")
    entry_address                       = builder.get_object("entry_address")
    entry_port                          = builder.get_object("entry_port")
    button_open_socket                  = builder.get_object("button_open_socket")
    button_close_socket                 = builder.get_object("button_close_socket")
    toolbutton_about                    = builder.get_object("toolbutton_about")
    label_eps_mcu_date                  = builder.get_object("label_eps_mcu_date")
    label_eps_mcu_time                  = builder.get_object("label_eps_mcu_time")
    label_eps_mcu_temp                  = builder.get_object("label_eps_mcu_temp")
    label_eps_mcu_curr                  = builder.get_object("label_eps_mcu_curr")
    label_eps_mcu_last_reset_cause      = builder.get_object("label_eps_mcu_last_reset_cause")
    label_eps_mcu_reset_count           = builder.get_object("label_eps_mcu_reset_count")
    label_eps_sp_volt_mypx              = builder.get_object("label_eps_sp_volt_mypx")
    label_eps_sp_volt_mxpz              = builder.get_object("label_eps_sp_volt_mxpz")
    label_eps_sp_volt_mzpy              = builder.get_object("label_eps_sp_volt_mzpy")
    label_eps_sp_curr_mx                = builder.get_object("label_eps_sp_curr_mx")
    label_eps_sp_curr_px                = builder.get_object("label_eps_sp_curr_px")
    label_eps_sp_curr_my                = builder.get_object("label_eps_sp_curr_my")
    label_eps_sp_curr_py                = builder.get_object("label_eps_sp_curr_py")
    label_eps_sp_curr_mz                = builder.get_object("label_eps_sp_curr_mz")
    label_eps_sp_curr_pz                = builder.get_object("label_eps_sp_curr_pz")
    label_eps_mppt_dc_ch_1              = builder.get_object("label_eps_mppt_dc_ch_1")
    label_eps_mppt_dc_ch_2              = builder.get_object("label_eps_mppt_dc_ch_2")
    label_eps_mppt_dc_ch_3              = builder.get_object("label_eps_mppt_dc_ch_3")
    label_eps_mppt_mode_ch_1            = builder.get_object("label_eps_mppt_mode_ch_1")
    label_eps_mppt_mode_ch_2            = builder.get_object("label_eps_mppt_mode_ch_2")
    label_eps_mppt_mode_ch_3            = builder.get_object("label_eps_mppt_mode_ch_3")
    label_eps_mppt_output_volt          = builder.get_object("label_eps_mppt_output_volt")
    label_eps_rtd_ch_0                  = builder.get_object("label_eps_rtd_ch_0")
    label_eps_rtd_ch_1                  = builder.get_object("label_eps_rtd_ch_1")
    label_eps_rtd_ch_2                  = builder.get_object("label_eps_rtd_ch_2")
    label_eps_rtd_ch_3                  = builder.get_object("label_eps_rtd_ch_3")
    label_eps_rtd_ch_4                  = builder.get_object("label_eps_rtd_ch_4")
    label_eps_rtd_ch_5                  = builder.get_object("label_eps_rtd_ch_5")
    label_eps_rtd_ch_6                  = builder.get_object("label_eps_rtd_ch_6")
    label_eps_bat_volt                  = builder.get_object("label_eps_bat_volt")
    label_eps_bat_curr                  = builder.get_object("label_eps_bat_curr")
    label_eps_bat_average_curr          = builder.get_object("label_eps_bat_average_curr")
    label_eps_bat_acc_curr              = builder.get_object("label_eps_bat_acc_curr")
    label_eps_bat_charge                = builder.get_object("label_eps_bat_charge")
    label_eps_bat_heater_1_dc           = builder.get_object("label_eps_bat_heater_1_dc")
    label_eps_bat_heater_2_dc           = builder.get_object("label_eps_bat_heater_2_dc")
    label_eps_bat_heater_1_mode         = builder.get_object("label_eps_bat_heater_1_mode")
    label_eps_bat_heater_2_mode         = builder.get_object("label_eps_bat_heater_2_mode")
    label_eps_bat_temp_monitor          = builder.get_object("label_eps_bat_temp_monitor")
    label_eps_bat_status                = builder.get_object("label_eps_bat_status")
    label_eps_bat_protection            = builder.get_object("label_eps_bat_protection")
    label_eps_bat_cycle_counter         = builder.get_object("label_eps_bat_cycle_counter")
    label_eps_bat_raac                  = builder.get_object("label_eps_bat_raac")
    label_eps_bat_rsac                  = builder.get_object("label_eps_bat_rsac")
    label_eps_bat_rarc                  = builder.get_object("label_eps_bat_rarc")
    label_eps_bat_rsrc                  = builder.get_object("label_eps_bat_rsrc")
    label_obdh_mcu_date                 = builder.get_object("label_obdh_mcu_date")
    label_obdh_mcu_time                 = builder.get_object("label_obdh_mcu_time")
    label_obdh_mcu_temp                 = builder.get_object("label_obdh_mcu_temp")
    label_obdh_mcu_last_reset_cause     = builder.get_object("label_obdh_mcu_last_reset_cause")
    label_obdh_mcu_reset_count          = builder.get_object("label_obdh_mcu_reset_count")
    label_obdh_general_voltage          = builder.get_object("label_obdh_general_voltage")
    label_obdh_general_current          = builder.get_object("label_obdh_general_current")
    label_obdh_mem_sec_obdh             = builder.get_object("label_obdh_mem_sec_obdh")
    label_obdh_mem_sec_eps              = builder.get_object("label_obdh_mem_sec_eps")
    label_obdh_mem_sec_ttc_0            = builder.get_object("label_obdh_mem_sec_ttc_0")
    label_obdh_mem_sec_ttc_1            = builder.get_object("label_obdh_mem_sec_ttc_1")
    label_obdh_mem_sec_antenna          = builder.get_object("label_obdh_mem_sec_antenna")
    label_obdh_mem_sec_edc              = builder.get_object("label_obdh_mem_sec_edc")
    label_obdh_mem_sec_payloadx         = builder.get_object("label_obdh_mem_sec_payloadx")
    label_obdh_mem_sec_sbcd             = builder.get_object("label_obdh_mem_sec_sbcd")
    label_obdh_position_lattitude       = builder.get_object("label_obdh_position_lattitude")
    label_obdh_position_longitude       = builder.get_object("label_obdh_position_longitude")
    label_obdh_position_altitude        = builder.get_object("label_obdh_position_altitude")
    textview_obdh_position_tle          = builder.get_object("textview_obdh_position_tle")
    label_obdh_position_date            = builder.get_object("label_obdh_position_date")
    label_obdh_position_time            = builder.get_object("label_obdh_position_time")
    label_obdh_op_last_valid_tc         = builder.get_object("label_obdh_op_last_valid_tc")
    label_obdh_op_mode                  = builder.get_object("label_obdh_op_mode")
    label_obdh_op_date_last_mode_change = builder.get_object("label_obdh_op_date_last_mode_change")
    label_obdh_op_time_last_mode_change = builder.get_object("label_obdh_op_time_last_mode_change")
    label_obdh_op_mode_duration         = builder.get_object("label_obdh_op_mode_duration")

    assert window                               != None
    assert button_preferences                   != None
    assert entry_address                        != None
    assert entry_port                           != None
    assert button_open_socket                   != None
    assert button_close_socket                  != None
    assert toolbutton_about                     != None
    assert label_eps_mcu_date                   != None
    assert label_eps_mcu_time                   != None
    assert label_eps_mcu_temp                   != None
    assert label_eps_mcu_curr                   != None
    assert label_eps_mcu_last_reset_cause       != None
    assert label_eps_mcu_reset_count            != None
    assert label_eps_sp_volt_mypx               != None
    assert label_eps_sp_volt_mxpz               != None
    assert label_eps_sp_volt_mzpy               != None
    assert label_eps_sp_curr_mx                 != None
    assert label_eps_sp_curr_px                 != None
    assert label_eps_sp_curr_my                 != None
    assert label_eps_sp_curr_py                 != None
    assert label_eps_sp_curr_mz                 != None
    assert label_eps_sp_curr_pz                 != None
    assert label_eps_mppt_dc_ch_1               != None
    assert label_eps_mppt_dc_ch_2               != None
    assert label_eps_mppt_dc_ch_3               != None
    assert label_eps_mppt_mode_ch_1             != None
    assert label_eps_mppt_mode_ch_2             != None
    assert label_eps_mppt_mode_ch_3             != None
    assert label_eps_mppt_output_volt           != None
    assert label_eps_rtd_ch_0                   != None
    assert label_eps_rtd_ch_1                   != None
    assert label_eps_rtd_ch_2                   != None
    assert label_eps_rtd_ch_3                   != None
    assert label_eps_rtd_ch_4                   != None
    assert label_eps_rtd_ch_5                   != None
    assert label_eps_rtd_ch_6                   != None
    assert label_eps_bat_volt                   != None
    assert label_eps_bat_curr                   != None
    assert label_eps_bat_average_curr           != None
    assert label_eps_bat_acc_curr               != None
    assert label_eps_bat_charge                 != None
    assert label_eps_bat_heater_1_dc            != None
    assert label_eps_bat_heater_2_dc            != None
    assert label_eps_bat_heater_1_mode          != None
    assert label_eps_bat_heater_2_mode          != None
    assert label_eps_bat_temp_monitor           != None
    assert label_eps_bat_status                 != None
    assert label_eps_bat_protection             != None
    assert label_eps_bat_cycle_counter          != None
    assert label_eps_bat_raac                   != None
    assert label_eps_bat_rsac                   != None
    assert label_eps_bat_rarc                   != None
    assert label_eps_bat_rsrc                   != None
    assert label_obdh_mcu_date                  != None
    assert label_obdh_mcu_time                  != None
    assert label_obdh_mcu_temp                  != None
    assert label_obdh_mcu_last_reset_cause      != None
    assert label_obdh_mcu_reset_count           != None
    assert label_obdh_general_voltage           != None
    assert label_obdh_general_current           != None
    assert label_obdh_mem_sec_obdh              != None
    assert label_obdh_mem_sec_eps               != None
    assert label_obdh_mem_sec_ttc_0             != None
    assert label_obdh_mem_sec_ttc_1             != None
    assert label_obdh_mem_sec_antenna           != None
    assert label_obdh_mem_sec_edc               != None
    assert label_obdh_mem_sec_payloadx          != None
    assert label_obdh_mem_sec_sbcd              != None
    assert label_obdh_position_lattitude        != None
    assert label_obdh_position_longitude        != None
    assert label_obdh_position_altitude         != None
    assert textview_obdh_position_tle           != None
    assert label_obdh_position_date             != None
    assert label_obdh_position_time             != None
    assert label_obdh_op_last_valid_tc          != None
    assert label_obdh_op_mode                   != None
    assert label_obdh_op_date_last_mode_change  != None
    assert label_obdh_op_time_last_mode_change  != None
    assert label_obdh_op_mode_duration          != None
