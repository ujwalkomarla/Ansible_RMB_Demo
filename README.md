# Ansible_RMB_Demo
Demo for writing Ansible Network Modules with Resource Module Builder for EXOS


* Start by cloning the [Ansible Resource Module Builder](https://github.com/ansible-network/resource_module_builder).
* Write your Network module's model with [`myos_interfaces`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/tree/master/resource_module_builder/models/myos/interfaces)
as an example - [`exos_auto_save_cfg`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/tree/master/resource_module_builder/models/exos/auto_save_cfg).
* Follow the [Usage Instructions](https://github.com/ujwalkomarla/Ansible_RMB_Demo/tree/master/resource_module_builder#usage) to scaffold your model, to get output as seen here - [`exos_auto_save_cfg_generated`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/tree/master/exos_auto_save_cfg_generated).
* Write the "facts" gathering logic in the generated [`/module_utils/network/exos/facts/auto_save_cfg/auto_save_cfg.py`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/blob/master/exos_auto_save_cfg_generated/module_utils/network/exos/facts/auto_save_cfg/auto_save_cfg.py) file.
* Write the "config" logic in the generated [`/module_utils/network/exos/config/auto_save_cfg/auto_save_cfg.py`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/blob/master/exos_auto_save_cfg_generated/module_utils/network/exos/config/auto_save_cfg/auto_save_cfg.py) file.
* Completed module is located at [`exos_auto_save_cfg`](https://github.com/ujwalkomarla/Ansible_RMB_Demo/tree/master/exos_auto_save_cfg)
* Run `diff -r -y --suppress-common-lines exos_auto_save_cfg_generated exos_auto_save_cfg` to see the code changes required from generated files to actual module code.
```diff
diff -r -y --suppress-common-lines exos_auto_save_cfg_generated/library/exos_auto_save_cfg.py exos_auto_save_cfg/library/exos_auto_save_cfg.py
module: exos_auto_save_Cfg				      |	module: auto_save_Cfg
							      >	        required: True
diff -r -y --suppress-common-lines exos_auto_save_cfg_generated/module_utils/network/exos/argspec/auto_save_cfg/auto_save_cfg.py exos_auto_save_cfg/module_utils/network/exos/argspec/auto_save_cfg/auto_save_cfg.py
    argument_spec = {'config': {'options': {'enable': {'type' |	    argument_spec = {'config': {'options': {'enable': {'requi
diff -r -y --suppress-common-lines exos_auto_save_cfg_generated/module_utils/network/exos/config/auto_save_cfg/auto_save_cfg.py exos_auto_save_cfg/module_utils/network/exos/config/auto_save_cfg/auto_save_cfg.py
							      >	from ansible.module_utils.network.exos.exos import run_comman
                self._connection.edit_config(commands)	      |	               run_commands(self._module, commands)
            kwargs = {}					      |	            commands = self._state_overridden(want, have)
            commands = self._state_overridden(**kwargs)	      <
            kwargs = {}					      |	            commands = self._state_deleted(want, have)
            commands = self._state_deleted(**kwargs)	      <
            kwargs = {}					      |	            commands = self._state_merged(want, have)
            commands = self._state_merged(**kwargs)	      <
            kwargs = {}					      |	            commands = self._state_replaced(want, have)
            commands = self._state_replaced(**kwargs)	      <
							      >
    def _state_replaced(**kwargs):			      |	    def _state_replaced(want, have):
							      >	        if want != have:
							      >	            if want['enable']:
							      >	                commands.extend(["save configuration automati
							      >	            else:
							      >	                commands.extend(["save configuration automati
    def _state_overridden(**kwargs):			      |	    def _state_overridden(want, have):
    def _state_merged(**kwargs):			      |	    def _state_merged(want, have):
    def _state_deleted(**kwargs):			      |	    def _state_deleted(want, have):
							      >	        if have['enable']:
							      >	            commands.extend(["save configuration automatic ne
diff -r -y --suppress-common-lines exos_auto_save_cfg_generated/module_utils/network/exos/facts/auto_save_cfg/auto_save_cfg.py exos_auto_save_cfg/module_utils/network/exos/facts/auto_save_cfg/auto_save_cfg.py
							      |	from ansible.module_utils.network.exos.exos import run_comman
        if connection:  # just for linting purposes, remove   <
            pass					      <
							      <
            data = ("resource rsrc_a\n"			      |	            data = run_commands(self._module, commands={"comm
                    "  a_bool true\n"			      |
                    "  a_string choice_a\n"		      |	        obj = {}
                    "  resource here\n"			      |	        if data:
                    "resource rscrc_b\n"		      |	            cfg_obj = self.render_config(self.generated_spec,
                    "  key is property01 value is value end\n |	            if cfg_obj:
                    "  an_int 10\n")			      |	                obj = cfg_obj
							      <
        # split the config into instances of the resource     <
        resource_delim = 'resource'			      <
        find_pattern = r'(?:^|\n)%s.*?(?=(?:^|\n)%s|$)' % (re <
                                                           re <
        resources = [p.strip() for p in re.findall(find_patte <
                                                   data,      <
                                                   re.DOTALL) <
							      <
        objs = []					      <
        for resource in resources:			      <
            if resource:				      <
                obj = self.render_config(self.generated_spec, <
                if obj:					      <
                    objs.append(obj)			      <
        if objs:					      |
            params = utils.validate_config(self.argument_spec |	        params = utils.validate_config(self.argument_spec, {'
            facts['auto_save_cfg'] = params['config']	      |	        facts['auto_save_cfg'] = params['config']
        config['name'] = utils.parse_conf_arg(conf, 'resource |	        config['name'] = conf['autoSaveCfgFName']
        config['some_string'] = utils.parse_conf_arg(conf, 'a |	        config['enable'] = True if conf['autoSaveEnabled'] ==
							      |	        config['interval'] = int(conf['autoSaveTimeInt'])
        match = re.match(r'.*key is property01 (\S+)',	      /	        return utils.remove_empties(config)
                         conf, re.MULTILINE | re.DOTALL)      <
        if match:					      <
            config['some_dict']['property_01'] = match.groups <
							      <
        a_bool = utils.parse_conf_arg(conf, 'a_bool')	      <
        if a_bool == 'true':				      <
            config['some_bool'] = True			      <
        elif a_bool == 'false':				      <
            config['some_bool'] = False			      <
        else:						      <
            config['some_bool'] = None			      <
							      <
        try:						      <
            config['some_int'] = int(utils.parse_conf_arg(con <
        except TypeError:				      <
            config['some_int'] = None			      <
        return utils.remove_empties(config)		      <
```
