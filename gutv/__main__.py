#!/usr/bin/env python

#
#  __main__.py
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
import sys
import pathlib

sys.path.append(str(pathlib.Path(os.path.realpath(__file__)).parents[1]))

from gutv.gu_tv import GUTV

def main(args):
    """
    Main function.

    :param args: Command line arguments.
    :type: Any

    :return: The code uppon termination.
    :rtype: int
    """
    app = GUTV()

    return app.run()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
