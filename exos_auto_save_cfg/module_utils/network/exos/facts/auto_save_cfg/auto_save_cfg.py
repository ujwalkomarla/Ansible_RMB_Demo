#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The exos auto_save_cfg fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
import re
from copy import deepcopy

from ansible.module_utils.network.common import utils
from ansible.module_utils.network.exos.argspec.auto_save_cfg.auto_save_cfg import Auto_save_cfgArgs
from ansible.module_utils.network.exos.exos import run_commands 

class Auto_save_cfgFacts(object):
    """ The exos auto_save_cfg fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Auto_save_cfgArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for auto_save_cfg
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            # typically data is populated from the current device configuration
            # data = connection.get('show running-config | section ^interface')
            # using mock data instead
            data = run_commands(self._module, commands={"command": "debug cfgmgr show one cfgmgr.autoSaveCfg", "output":"json"})    

        obj = {}
        if data:
            cfg_obj = self.render_config(self.generated_spec, data[0]['data'][0])
            if cfg_obj:
                obj = cfg_obj

        ansible_facts['ansible_network_resources'].pop('auto_save_cfg', None)
        facts = {}

        params = utils.validate_config(self.argument_spec, {'config': obj})
        facts['auto_save_cfg'] = params['config']

        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        config['name'] = conf['autoSaveCfgFName']
        config['enable'] = True if conf['autoSaveEnabled'] == '1' else False
        config['interval'] = int(conf['autoSaveTimeInt'])
        return utils.remove_empties(config)