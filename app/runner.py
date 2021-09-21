#!/usr/bin/python
import sys

from tdconnections import config_helper
from tdconnections import halo_api_caller
from tdconnections import utility
from tdconnections import json_to_csv


def main():
    utility.Utility.log_stdout("TD Connections Script Started ...")
    config = config_helper.ConfigHelper()
    utility.Utility.log_stdout("1- Creating HALO API CALLER Object.")
    halo_api_caller_obj = halo_api_caller.HaloAPICaller(config)

    """
    First we make sure that all configs are sound...
    """
    utility.Utility.log_stdout("2- Checking the provided configuration parameters")
    check_configs(config, halo_api_caller_obj)

    """
    Retrieving list of group listening ports / inbound connections / outbound connections
    """
    utility.Utility.log_stdout(
        "3- Retrieving list of group listening ports / inbound connections / outbound connections")
    td_connections_lst = halo_api_caller_obj.get_group_listening_ports(config.target_group_id)
    #td_connections_lst = halo_api_caller_obj.get_group_inbound_connections(config.target_group_id)
    #td_connections_lst = halo_api_caller_obj.get_group_outbound_connections(config.target_group_id)
    json_to_csv_obj = json_to_csv.JSONToCSV()
    json_to_csv_obj.convert_json_to_csv(td_connections_lst)
    #print(td_connections_lst)


def check_configs(config, halo_api_caller):
    halo_api_caller_obj = halo_api_caller
    if halo_api_caller_obj.credentials_work() is False:
        utility.Utility.log_stdout("Halo credentials are bad!  Exiting!")
        sys.exit(1)

    if config.sane() is False:
        utility.Utility.log_stdout("Configuration is bad!  Exiting!")
        sys.exit(1)


if __name__ == "__main__":
    main()
