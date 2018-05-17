# Easy AVR USB Keyboard Firmware Keymapper
# Copyright (C) 2013-2016 David Howland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Keyboard definition for a hand-wired keyboard"""

# The first decision you have to make is to choose a hardware
# layout.  Assuming you are using a Teensy2.0, ATmega32U4_16MHz_TKL
# is probably the best hardware layout for you.  ATmega32U4_16MHz_SIXTY
# might also work for you, though.  The sizes are defined in the
# templates/__init__.py file of the keymapper.
# Leave the rest of the imports like they are here.
import easykeymap.templates.ATmega32U4_16MHz_TKL as firmware
from easykeymap.ioports import *
from easykeymap.helper import make_matrix_config

# The name of the board in the "New" dialog
description = "Signum III"
# Unique string to identify THIS exact hardware layout
unique_id = "Signum_3_PCB_v0.5"
# The name of the .cfg file the system will try to find for altered
# layout options.  See the configs subdir of the keymapper.
cfg_name = "Signum III"

# Hand-wired boards usually use Teensy controllers.  Set this to
# True to make sure that the bootloader works.
teensy = True
# If your board has an exposed switch for going into the bootloader,
# you can set this to True and the system won't prompt you to add a
# BOOT key to your layout.
hw_boot_key = True

# These two parameters define the size of the keyboard in the display.
# Must be whole numbers in units of quarter key lengths.  A TKL
# usually is 6 rows high with a 1/2 key length gutter under the Fn row.
# Therefore int(6.5*4).  Apply the same logic the width.  Remember
# we are talking visual width, not number of columns.
display_height = int(6.5*4)
display_width = int(18.25*4)

# The number of rows and columns in the matrix.  In a hand-wired board
# each of these will correspond to a single pin.
num_rows = 4
num_cols = 12

# Keyboards work by scanning a matrix to check each key.  The scan
# works by setting an active row/column (strobing) and then reading
# the status of every switch that crosses it (sensing).
# strobe_cols tells the firmware which direction you have your diodes
# installed.  If diodes go from column to row, then strobe_cols must
# be False.  If diodes go from row to column, then strobe_cols must be
# True.
strobe_cols = False
# strobe_low tells the firmware if a row/column should be activated
# by pulling the pin high or low.  Hand-wired boards will almost always
# use strobe_low = True
strobe_low = True

# The matrix_hardware, matrix_strobe, matrix_sense parameters tell
# the firmware how to initialize the ports, what pins must be set
# for each row/column, and what order to strobe/sense.  These are
# complicated and are explained fully elsewhere.  It is easiest to
# configure the matrix by using the make_matrix_config function as
# shown below.  Just customize 'rows' and 'cols' for your project.
matrix_hardware, matrix_strobe, matrix_sense = make_matrix_config(
    strobe_cols=strobe_cols,
    strobe_low=strobe_low,
    rows=[B3, F5, D2, B5],
    #     R0  R1  R2  R3
    #cols=[F7, F5, F4, B5, B6, F6, D5, C7, C6, D3, B2, B7],
    cols=[B2, B7, B1, D0, B0, D1, B6, F0, F7, F1, F6, F4],
    #     C0  C1  C2  C3  C4  C5  C6  C7  C8  C9  C10 C11
    device=firmware.device
)

# The total number of LED outputs (indicators + backlights)
num_leds = 1
# The number of LED indicators (for example, caps lock)
num_ind = 1
# The number of backlight enable modes.  This counts the number of
# options available for the BL_ENABLE key.  Boards without backlights
# should use the minimum value of 2.
num_bl_enab = 2

# Define the default assignments of the indicator LEDs.  The length
# of this list must equal num_ind.  For each LED, the first string
# is the description of the key shown in the GUI.  The second string
# is the default function assigned to that LED.  LED functions must
# be strings as defined in led_assignments of gui.py.  Common choices
# are 'Num Lock', 'Caps Lock', 'Scroll Lock', 'Win Lock', 'Fn Active',
# 'Recording', 'Backlight', and 'Unassigned'.
led_definition = [
    ('Teensy', 'Recording'),
    #('red_bl_low', 'Recording'),
    #('green_bl_low', 'Recording'),
    #('blue_bl_low', 'Recording'),
]

# Definition of LED pins.  (indicators and backlights)  Indicators
# must come first and be in the same order as defined in led_definition.
# LED_DRIVER_PULLUP is used when the pin is connected to the anode of
# the LED and the cathode is connected to ground.
# LED_DRIVER_PULLDOWN is used when the pin is connected to the cathode
# of the LED and the anode is connected to the power supply.
led_hardware = [
#       Port    Pin    Direction
    ( REF_PORTD, 6, LED_DRIVER_PULLUP ),
]

# True if the board supports backlight, otherwise False
backlighting = True

# This can be used to configure different backlighting zones.  Explained
# in more detail elsewhere.  Length of list must equal num_bl_enab.
# Length of each tuple must equal num_leds.  Tuples use the same ordering
# as led_hardware.  Almost everyone should just use an all-on/all-off
# configuration.  That's a list of two tuples, one with all 1s for each
# LED, the other with all 0s for each LED.
bl_modes = [
    ( 1, ),
    ( 0, ),
]

# Just leave this here as-is.
KMAC_key = None

# Define your layout.  This is a list of rows.  Each row is a list
# of keys.  Each key is a tuple of three items.  First item is a tuple
# defining the width,height of the key.  If it is just a number, it
# will be a space instead of a key.  All units are in quarter key lengths,
# so a standard key would be (4,4).  Second item is a tuple defining the
# row,column in the matrix for that key.  Third item is the default scancode
# for that key, from scancodes.py.  If a row is a number instead of a list,
# it will just make a vertical spacer.

keyboard_definition = [
    [((4, 4), (0,  0),'HID_KEYBOARD_SC_ESCAPE'),
     ((4, 4), (0,  1),'HID_KEYBOARD_SC_Q'),
     ((4, 4), (0,  2), 'HID_KEYBOARD_SC_W'),
     ((4, 4), (0,  3), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (0,  4), 'HID_KEYBOARD_SC_R'),
     ((4, 4), (0,  5), 'HID_KEYBOARD_SC_T'),
     ((4, 4), (0,  6), 'HID_KEYBOARD_SC_Y'),
     ((4, 4), (0,  7), 'HID_KEYBOARD_SC_U'),
     ((4, 4), (0,  8), 'HID_KEYBOARD_SC_I'),
     ((4, 4), (0,  9), 'HID_KEYBOARD_SC_O'),
     ((4, 4), (0, 10),  'HID_KEYBOARD_SC_P'),
     ((4, 4), (0, 11),  'HID_KEYBOARD_SC_BACKSPACE')],

    [((4, 4), (1,  0),'HID_KEYBOARD_SC_TAB'),
     ((4, 4), (1,  1),'HID_KEYBOARD_SC_A'),
     ((4, 4), (1,  2), 'HID_KEYBOARD_SC_S'),
     ((4, 4), (1,  3), 'HID_KEYBOARD_SC_D'),
     ((4, 4), (1,  4), 'HID_KEYBOARD_SC_F'),
     ((4, 4), (1,  5), 'HID_KEYBOARD_SC_G'),
     ((4, 4), (1,  6), 'HID_KEYBOARD_SC_H'),
     ((4, 4), (1,  7), 'HID_KEYBOARD_SC_J'),
     ((4, 4), (1,  8), 'HID_KEYBOARD_SC_K'),
     ((4, 4), (1,  9), 'HID_KEYBOARD_SC_L'),
     ((4, 4), (1, 10),  'HID_KEYBOARD_SC_SEMICOLON_AND_COLON'),
     ((4, 4), (1, 11),  'HID_KEYBOARD_SC_APOSTROPHE_AND_QUOTE')],

    [((4, 4), (2,  0),'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), (2,  1),'HID_KEYBOARD_SC_Z'),
     ((4, 4), (2,  2), 'HID_KEYBOARD_SC_X'),
     ((4, 4), (2,  3), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (2,  4), 'HID_KEYBOARD_SC_V'),
     ((4, 4), (2,  5), 'HID_KEYBOARD_SC_B'),
     ((4, 4), (2,  6), 'HID_KEYBOARD_SC_N'),
     ((4, 4), (2,  7), 'HID_KEYBOARD_SC_M'),
     ((4, 4), (2,  8), 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((4, 4), (2,  9), 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((4, 4), (2, 10),  'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK'),
     ((4, 4), (2, 11),  'HID_KEYBOARD_SC_ENTER')],

    [((4, 4), (3,  0),'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((4, 4), (3,  1),'HID_KEYBOARD_SC_LEFT_GUI'),
     ((4, 4), (3,  2), 'HID_KEYBOARD_SC_LEFT_ALT'),
     ((4, 4), (3,  3), 'HID_KEYBOARD_SC_RIGHT_SHIFT'),
     ((4, 4), (3,  4), 'SCANCODE_FN'),
     ((4, 4), (3,  5), 'HID_KEYBOARD_SC_SPACE'),
     ((4, 4), (3,  6), 'HID_KEYBOARD_SC_SPACE'),
     ((4, 4), (3,  7), 'SCANCODE_FN2'),
     ((4, 4), (3,  8), 'HID_KEYBOARD_SC_LEFT_ARROW'),
     ((4, 4), (3,  9), 'HID_KEYBOARD_SC_DOWN_ARROW'),
     ((4, 4), (3, 10),  'HID_KEYBOARD_SC_UP_ARROW'),
     ((4, 4), (3, 11),  'HID_KEYBOARD_SC_RIGHT_ARROW')]
]

# Just leave this here as-is.
alt_layouts = {}
