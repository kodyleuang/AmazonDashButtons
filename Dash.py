#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo communicate with other Cozmo robots
'''

import cozmo
import socket
import errno
from socket import error as socket_error

# need to get movement info
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket_error as msg:
        robot.say_text("socket failed" + msg).wait_for_completed()
    ip = "10.0.1.10"
    port = 5000

    try:
        s.connect((ip, port))
    except socket_error as msg:
        robot.say_text("socket failed to bind").wait_for_completed()
    cont = True

    robot.say_text("ready").wait_for_completed()

    # SET COZMO's NAME
    myName = {'maxwell', 'mac_cheese', 'elements', 'emergency',
              'gatorade', 'cottonelle', 'quest', 'kitty', 'sky',
              'mashup', 'poof', 'temptation', 'human'}

    while cont:
        bytedata = s.recv(4048)
        #data = str(bytedata)
        data = bytedata.decode('utf-8')
        print('this is the data recv ' + data)
        if not data:
            cont = False
            s.close()
            quit()
        else:
            instructions = data.split(";")
            print(instructions)
            if instructions[0] in myName:
                robot.say_text(instructions[0])
                print("item found " + data)

cozmo.run_program(cozmo_program)
