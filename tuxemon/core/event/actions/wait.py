# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time

from tuxemon.core.event.eventaction import EventAction
from tuxemon.core.tools import number_or_variable


class WaitAction(EventAction):
    """ Blocks event chain for some time
    The duration can be either a number or the name of a numeric variable

    Valid Parameters: duration

    * duration (string): time in seconds to wait for
    """
    name = "wait"
    valid_parameters = [
        (str, 'seconds')
    ]

    # TODO: use event loop time, not wall clock
    def start(self):
        secs = number_or_variable(self.session, self.parameters.seconds)
        self.finish_time = time.time() + secs

    def update(self):
        if time.time() >= self.finish_time:
            self.stop()
