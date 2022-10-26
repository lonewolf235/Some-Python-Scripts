#pip install -U gpx-converter    dependancy
from gpx_converter import Converter
import os
import codecs
import subprocess
import pandas as pd

root_vid_directory = r"P:/coding/Machine Learning/Datasets/pothole/gopro videos/"    #gopro videos location
ddpai_directory = r"P:/coding/Machine Learning/Datasets/pothole/ddpai pro videos/"     #ddpai videos location
def goprogenerate():
    for path, directories, files in os.walk(root_vid_directory):
        for video_file in files:
            if video_file.endswith("mp4") or video_file.endswith("MP4"):
                full_mp4_path = os.path.join(path, video_file)
                full_gpx_output_path = full_mp4_path.replace(".MP4", ".GPX")
                print(f"Processing: {full_mp4_path}")
                with open(full_gpx_output_path, "w") as gpx_file:
                    exiftool_command = ["P:\coding\Machine Learning\Datasets\pothole\exif files\exiftool.exe", "-ee", "-p", "P:\coding\Machine Learning\Datasets\pothole\exif files\gpx.fmt.txt", full_mp4_path]
                                        ## Exiftool.exe full location                                                         ## Gpx.fmt.txt full location          
                    subprocess.run(exiftool_command, stdout=gpx_file)
                print(f"Succesfully created: {full_gpx_output_path}\n")
goprogenerate()

def csvconvert():
    for path, directories, files in os.walk(root_vid_directory):
        for video_file in files:
            if video_file.endswith("GPX"):
                full_gpx_path = os.path.join(path, video_file)
                # full_json_output_path = full_gpx_path.replace(".GPX", ".json")
                full_csv_output_path = full_gpx_path.replace(".GPX", ".csv")
                # Converter(input_file=full_gpx_path).gpx_to_json(output_file=full_json_output_path)
                Converter(input_file=full_gpx_path).gpx_to_csv(output_file=full_csv_output_path)

csvconvert()


def goproinfo():
    for path, directories, files in os.walk(root_vid_directory):
        for csv_file in files:
            if csv_file.endswith("csv") or csv_file.endswith("CSV"):
                full_csv_path = os.path.join(path, csv_file)
                dataset=pd.read_csv(full_csv_path)
                time=dataset.time
                date=time.str.split(expand=True)[0]
                timestamp=time.str.split(expand=True)[1].str.split("+",expand=True)[0]
                latitude= dataset.latitude
                altitude= dataset.altitude
                longitude= dataset.longitude
                for i in range(len(dataset)):
                    print("date: ",date[i])
                    print("timestamp: ",timestamp[i])
                    print("latitude: ",latitude[i])
                    print("longitude: ",longitude[i])
                    print("altitude: ",altitude[i])
                    print(i)
goproinfo()

def ddpaiinfo():
    for path, directories, files in os.walk(ddpai_directory):
        for ddpai_file in files:
            if ddpai_file.endswith("gpx") or ddpai_file.endswith("GPX"):
                ddpai_path = os.path.join(path, ddpai_file)
                with codecs.open(ddpai_path, 'r', encoding='utf-8',errors='ignore') as file1:
                    for line in file1.readlines():
                        if (line.startswith('$GPRMC')):
                            #print(line)
                            #file2.write(line[len("$GPRMC,"):])
                            timeStamp = line[len("$GPRMC,"):].split(',')[0]
                            print('timeStamp:', timeStamp)
                            latiTude = line[len("$GPRMC,"):].split(',')[2]
                            print('latiTude:', latiTude)
                            longiTude = line[len("$GPRMC,"):].split(',')[4]
                            print('longiTude:', longiTude)
                            dateStamp = line[len("$GPRMC,"):].split(',')[8]
                            print('dateStamp:', dateStamp)      
                # close and save the files
                file1.close()

ddpaiinfo()