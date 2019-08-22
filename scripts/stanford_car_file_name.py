from pathlib import Path

datasetType = "test"

outputPath = "/home/weizhuozhang/workspace/darknet/build/darknet/x64/data/stanford_car_{0}.txt".format(datasetType)

datasetPrefix = "data/car_data/{0}".format(datasetType)
absPathPrefix = "/home/weizhuozhang/workspace/darknet/build/darknet/x64"

annoPath = "/home/weizhuozhang/dataset/stanford_cars_dataset/anno_{0}.csv".format(datasetType)
nameFilePath = "/home/weizhuozhang/workspace/darknet/build/darknet/x64/data/stanford_car.names"

nameMap = {}

with open(nameFilePath) as file:
    count = 1
    for line in file.readlines():
        line = line.strip()
        nameMap[count] = line
        count += 1

with open(annoPath) as file:
    with open(outputPath, 'w') as outputFile:
        count = 0
        for line in file.readlines():
            line = line.strip().split(',')
            fileName = line[0]
            classNum = nameMap[int(line[-1])]
            outputStr = "{0}/{1}/{2}".format(datasetPrefix, classNum, fileName)
            absPath = "{0}/{1}".format(absPathPrefix, outputStr)
            absPathLib = Path(absPath)
            if not absPathLib.exists():
                print(absPath)
                count += 1
            outputFile.write("{0}\n".format(outputStr))
        if 0 != count:
            print("There are {0} imgs not found".format(count))
