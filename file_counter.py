import os
import time


def num_files(directory):
    i = 0
    for f in directory:
        i += 1

    return i


input_directory = raw_input("Enter the input directory: ")
data_directory = raw_input("Enter the data directory: ")


target_num = num_files(os.listdir(input_directory))

print "Number of files in " + input_directory + " is: " + str(target_num)

while True:
    data_num = num_files(os.listdir(data_directory))
    print "Number of files in " + data_directory + " is: " + str(data_num)
    
    time.sleep(60)


