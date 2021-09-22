#!/usr/bin/python
import sys

from tdconnections import config_helper
from tdconnections import halo_api_caller
from tdconnections import json_to_csv
from tdconnections import utility


def main():
    utility.Utility.log_stdout("********************** TD Connections Script Started **********************")

    utility.Utility.log_stdout("================================================================")
    utility.Utility.log_stdout("********************** Operation **********************")
    operation_choice = input(
        "Enter 1 for Listing Listening Ports.\nEnter 2 for Listing Inbound Connections.\nEnter 3 for Listing Outbound "
        "Connections.\nEnter 0 to EXIT.:\n")
    target_operation = int(operation_choice)
    if target_operation == 1:
        utility.Utility.log_stdout("================================================================")
        utility.Utility.log_stdout("********************** Listening Ports **********************")
        port_number_choice = input(
            "Enter 1 for Filtering Listening Ports with Specific Port Number.\nEnter 2 to retrieve all Listening "
            "Ports.\nEnter 0 to EXIT.:\n")
        target_port_number_choice = int(port_number_choice)
        if target_port_number_choice == 1:
            target_port_number = input("Please, Enter Specific Port Number to Filter Listening Ports with it:\n")
        elif target_port_number_choice == 2:
            target_port_number = ""
        elif target_port_number_choice == 0:
            utility.Utility.log_stdout("Terminating The Program.")
            sys.exit()
        else:
            utility.Utility.log_stdout("Wrong Choice, terminating the program.")
            sys.exit()
    elif target_operation == 2:
        utility.Utility.log_stdout("================================================================")
        utility.Utility.log_stdout("********************** Inbound Connections **********************")
        ip_choice = input(
            "Enter 1 for Filtering Inbound Connections with Specific list of IPs.\nEnter 2 to retrieve all Inbound "
            "Connections.\nEnter 0 to EXIT.:\n")
        target_IPs_choice = int(ip_choice)
        if target_IPs_choice == 1:
            target_ip_list = input(
                "Please, Enter comma separated list of IPs to Filter Inbound Connections with it/them:\n")
        elif target_IPs_choice == 2:
            target_ip_list = ""
        elif target_IPs_choice == 0:
            utility.Utility.log_stdout("Terminating The Program.")
            sys.exit()
        else:
            utility.Utility.log_stdout("Wrong Choice, terminating the program.")
            sys.exit()
    elif target_operation == 3:
        utility.Utility.log_stdout("================================================================")
        utility.Utility.log_stdout("********************** Outbound Connections **********************")
        ip_choice = input(
            "Enter 1 for Filtering Outbound Connections with Specific list of IPs.\nEnter 2 to retrieve all Outbound "
            "Connections.\nEnter 0 to EXIT.:\n")
        target_IPs_choice = int(ip_choice)
        if target_IPs_choice == 1:
            target_ip_list = input(
                "Please, Enter comma separated list of IPs to Filter Outbound Connections with it/them:\n")
        elif target_IPs_choice == 2:
            target_ip_list = ""
        elif target_IPs_choice == 0:
            utility.Utility.log_stdout("Terminating The Program.")
            sys.exit()
        else:
            utility.Utility.log_stdout("Wrong Choice, terminating the program.")
            sys.exit()
    elif target_operation == 0:
        utility.Utility.log_stdout("Terminating The Program.")
        sys.exit()
    else:
        utility.Utility.log_stdout("Wrong Choice, terminating the program.")
        sys.exit()
    utility.Utility.log_stdout("================================================================")
    utility.Utility.log_stdout("********************** Group ID **********************")
    target_group_id = input(
        "Please, Enter Target Group ID:")
    utility.Utility.log_stdout("================================================================")
    utility.Utility.log_stdout("********************** Output Directory **********************")
    output_directory_choice = input(
        "Enter 1 for Entering Output Directory for CSV file.\nEnter 2 to use the current directory.\nEnter 0 to "
        "EXIT.:\n")
    target_output_directory_choice = int(output_directory_choice)
    if target_output_directory_choice == 1:
        target_output_directory = input(
            "Please, Enter Output Directory for CSV file:\n")
    elif target_output_directory_choice == 2:
        target_output_directory = ""
    elif target_output_directory_choice == 0:
        utility.Utility.log_stdout("Terminating The Program.")
        sys.exit()
    else:
        utility.Utility.log_stdout("Wrong Choice, terminating the program.")
        sys.exit()
    utility.Utility.log_stdout("================================================================")

    config = config_helper.ConfigHelper()
    json_to_csv_obj = json_to_csv.JSONToCSV()

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
    if target_operation == 1:
        utility.Utility.log_stdout(
            "3- Retrieving list of group listening ports")
        td_connections_lst = halo_api_caller_obj.get_group_listening_ports(target_group_id,
                                                                           target_port_number)
    if target_operation == 2:
        utility.Utility.log_stdout(
            "3- Retrieving list of group inbound connections")
        td_connections_lst = halo_api_caller_obj.get_group_inbound_connections(target_group_id,
                                                                               target_ip_list)
    if target_operation == 3:
        utility.Utility.log_stdout(
            "3- Retrieving list of group outbound connections")
        td_connections_lst = halo_api_caller_obj.get_group_outbound_connections(target_group_id,
                                                                                target_ip_list)

    utility.Utility.log_stdout(
        "4- exporting retrieved td connections list into CSV format")
    json_to_csv_obj.convert_json_to_csv(target_output_directory, td_connections_lst)
    utility.Utility.log_stdout(
        "********************** TD Connections Script Finished **********************")


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
