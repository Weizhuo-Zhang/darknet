import cv2
datasetType = "test"

homePath = "/home/weizhuozhang"
dataPrefix = "{0}/workspace/darknet/build/darknet/x64/data".format(homePath)
outputPath = "{0}/car_data/{1}".format(dataPrefix, datasetType)

annoPath = "{0}/dataset/stanford_cars_dataset/anno_{0}.csv".format(homePath, datasetType)
nameFilePath = "{0}/stanford_car.names".format(dataPrefix)

nameMap = {}

with open(nameFilePath) as file:
    count = 1
    for line in file.readlines():
        line = line.strip()
        nameMap[count] = line
        count += 1

with open(annoPath) as file:


