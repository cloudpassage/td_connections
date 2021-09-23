import imp
import os
import sys

module_name = 'tdconnections'
current_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(current_dir, '../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
td_connections = imp.load_module(module_name, fp, pathname, description)


class TestHALOAPICalls:

    def test_get_group_listening_ports(self):
        config = td_connections.ConfigHelper()
        halo_api_caller_obj = td_connections.HaloAPICaller(config)
        halo_api_caller_obj.authenticate_client()
        group_id = config.target_group_id
        port_number = config.target_port_number
        td_connections_lst = halo_api_caller_obj.get_group_listening_ports(group_id, port_number)
        listening_ports_list = td_connections_lst[0]
        assert listening_ports_list['count'] == 4

    def test_get_group_inbound_connections(self):
        config = td_connections.ConfigHelper()
        halo_api_caller_obj = td_connections.HaloAPICaller(config)
        halo_api_caller_obj.authenticate_client()
        group_id = config.target_group_id
        ip_list = config.target_ip_addresses
        td_connections_lst = halo_api_caller_obj.get_group_inbound_connections(group_id, ip_list)
        inbound_connections_list = td_connections_lst[0]
        assert inbound_connections_list['count'] == 1261

    def test_get_group_outbound_connections(self):
        config = td_connections.ConfigHelper()
        halo_api_caller_obj = td_connections.HaloAPICaller(config)
        halo_api_caller_obj.authenticate_client()
        group_id = config.target_group_id
        ip_list = config.target_ip_addresses
        td_connections_lst = halo_api_caller_obj.get_group_outbound_connections(group_id, ip_list)
        outbound_connections_list = td_connections_lst[0]
        assert outbound_connections_list['count'] == 47
