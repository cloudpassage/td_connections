# TD_Connections
Traffic Discovery Retrieval Tool

## Goal:
The main purpose of this tool is to retrieve the traffic discovery connections 
(Listening Ports, Inbound Connections, Outbound Connections) for a specific group based on pre-defined filters (i.e. specific port number,
List of IPs) and export these results into CSV file.

## Requirements:
- CloudPassage Halo API key (with auditor privileges).
- Python 3.6 or later including packages specified in "requirements.txt".

## Installation:
`git clone https://github.com/cloudpassage/td_connections.git`

`cd td_connections/app`

`pip install -r requirements.txt`

## Configuration:
| Variable | Description | Default Value |
| -------- | ----- | ----- |
| HALO_API_KEY_ID | ID of HALO API Key | <HALO_API_KEY_ID> |
| HALO_API_KEY_SECRET | Secret of HALO API Key | <HALO_API_KEY_SECRET> |
| HALO_API_HOSTNAME | Halo API Host Name | https://api.cloudpassage.com |
| HALO_API_PORT | Halo API Port Number | 443 |
| HALO_API_VERSION | HALO EndPoint Version | v1 |

## How to run the tool (stand-alone):
To run the script follow the below steps.

1.  Navigate to the app folder that contains module "runner_with_inputs.py", and run it


    `cd td_connections/app`

    `python runner_with_inputs.py`



2. Script will ask user to enter required operation number, there are three choices:
   1. Listening Ports
   2. Inbound Connections
   3. Outbound Connections
   4. Exit



3. If the user chooses listening ports operation, then script will give the user three options:
   1. Use specific port number to filter retrieved listening ports (i.e. 22)
   2. Retrieve all available listening ports
   3. Exit



4. If the user chooses inbound connections operation, then script will give the user three options:
   1. Use list of IPs to filter retrieved inbound connections (i.e. 172.31.30.108, 172.31.15.11)
   2. Retrieve all available inbound connections
   3. Exit



5. If the user chooses outbound connections operation, then script will give the user three options:
   1. Use list of IPs to filter retrieved outbound connections (i.e. 172.31.30.108, 172.31.15.11)
   2. Retrieve all available outbound connections
   3. Exit



6. Then the script will ask the user enter the target group id



7. After that, the script will ask the user to choose where to save the output CSV file, the script will give the user three options:
   1. Set specific output directory for the generated CSV file (i.e. C:/Users/td_connections/app)
   2. Save the CSV file in the current directory
   3. Exit



8. After setting the required input parameters above, The script will start connecting to HALO API and retrieving required TD connections.