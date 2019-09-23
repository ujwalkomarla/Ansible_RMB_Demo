#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for exos_auto_save_cfg
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: auto_save_Cfg
version_added: 2.10
short_description: Manage automatic configuration save feature.
description:
  - This module manages the automatic configuration save feature on Extreme Networks EXOS based switches.
author: 
  - Ujwal Komarla (@ujwalkomarla)
options:
  config:
    description: The list of automatic configuration save options
    type: dict
    suboptions:
      name:
        description:
          - File name to which the configuration needs to be saved.
        type: str
        default: "primary"
      enable:
        description:
          - This is a boolean value to control the configuration auto save feature.
        type: bool
        required: True
      interval:
        description:
          - Interval at which the configuration needs to be auto saved.
        type: int
        default: 5
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - replaced
    - deleted
    default: replaced
"""
EXAMPLES = """
# Using replaced
# Before state:
# -------------
# x460g2#show configuration | include "save configuration"
#  save configuration automatic every 10 primary

- name: "Configure auto-save feature"
  exos_auto_save_cfg:
    config:
      name: secondary
      interval: 30
      enable: true
    state: replaced

# After state:
# -------------
# x460g2#show configuration | include "save configuration"
# save configuration automatic every 30 secondary


# Using Deleted without any config passed
# Before state:
# -------------
# x460g2#show configuration | include "save configuration"
#  save configuration automatic every 10 primary

- name: "Disable auto-save feature"
  exos_auto_save_cfg:
    state: deleted
# After state:
# -------------
# x460g2#show configuration | include "save configuration"
# x460g2#


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.exos.argspec.auto_save_cfg.auto_save_cfg import Auto_save_cfgArgs
from ansible.module_utils.network.exos.config.auto_save_cfg.auto_save_cfg import Auto_save_cfg


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Auto_save_cfgArgs.argument_spec,
                           supports_check_mode=True)

    result = Auto_save_cfg(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()