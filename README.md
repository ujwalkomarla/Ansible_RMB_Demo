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
