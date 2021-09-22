import csv
from datetime import datetime
from . import utility


class JSONToCSV(object):

    def convert_json_to_csv(self, output_directory, json_object):
        json_data = json_object[0]
        connections_data = json_data['connections']

        # now we will open a file for writing
        current_time = utility.Utility.date_to_iso8601(datetime.now())
        file_name = 'connections_data_file_'+current_time+'.csv'
        file_name = file_name.replace(':', '-')
        if output_directory == "" :
            absolute_path = file_name
        else:
            absolute_path = output_directory+"/"+file_name

        data_file = open(absolute_path, 'w')

        # create the csv writer object
        csv_writer = csv.writer(data_file)

        # Counter variable used for writing
        # headers to the CSV file
        count = 0

        for connection in connections_data:
            if count == 0:
                # Writing headers of CSV file
                header = connection.keys()
                csv_writer.writerow(header)
                count += 1

            # Writing data of CSV file
            csv_writer.writerow(connection.values())

        data_file.close()
