# -*- coding: UTF-8 -*-
#
#    =======================================================================
#    Copyright (C), 2018, Huawei Tech. Co., Ltd.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#    =======================================================================
#
import os
import sys

from static_check_commands import StaticCheckCommands

THIS_FILE_NAME = __file__

sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(THIS_FILE_NAME)), ".."))

import comm.util as util


def main():
    check_type = os.sys.argv[1]

    static_check_commands = StaticCheckCommands()
    ret, commands = static_check_commands.get_commands(check_type)
    if not ret:
        exit(-1)

    for command in commands:
        ret = util.execute(command, print_output_flag=True)
        if not ret[0]:
            exit(-1)
    exit(0)


if __name__ == '__main__':
    main()