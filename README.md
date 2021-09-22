# TD_Connections
Traffic Discovery Retrieval Tool

## Goal:
The main purpose of this tool is to retrieve the traffic discovery connections 
(Listening Ports, Inbound Connections, Outbound Connections) for a specific group based on pre-defined filters (i.e. specific port number,
List of IPs) and export these results into CSV file.

## Requirements:
- CloudPassage Halo API key (with admin privileges).
- Python 3.6 or later including packages specified in "requirements.txt".

## Installation:
`git clone https://github.com/cloudpassage/td_connections.git`

`pip install -r requirements.txt`

## Configuration:
| Variable | Description | Default Value |
| -------- | ----- | ----- |
| HALO_API_KEY_ID | ID of HALO API Key | <HALO_API_KEY_ID> |
| HALO_API_KEY_SECRET | Secret of HALO API Key | <HALO_API_KEY_SECRET> |
| HALO_API_HOSTNAME | Halo API Host Name | https://api.cloudpassage.com |
| HALO_API_PORT | Halo API Port Number | 443 |
| HALO_API_VERSION | HALO EndPoint Version | v1 |
| TARGET_GROUP_ID | Target Group ID to retrieve TD connections for| <TARGET_GROUP_ID> |
| TARGET_PORT_NUMBER | Specific Port Number to filter Listening ports with | <TARGET_PORT_NUMBERS> i.e. 22 |
| TARGET_IP_ADDRESSES | Specific IPs to filter Inbound/Outbound connections with | TARGET_IP_ADDRESSES i.e. 172.31.30.108, 172.31.15.11 |
| TARGET_OPERATION | Target Operation (LISTEN, IN, OUT) for (Listening Ports, Inbound Connections, Outbound Connections) | LISTEN |
| OUTPUT_DIRECTORY | Output directory for the generated CSV file | Same directory of the script |

## How to run the tool (stand-alone):
The following commands are for running the mapping script.

`cd td_connections/app`

`python runner.py`
