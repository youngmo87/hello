import struct

# labelFile = open("./data/t10k-labels-idx1-ubyte", "rb")
# 
def writeCsv(name):
    labelFile = open("./data/" + name + "-labels.idx1-ubyte", "rb")
    imageFile = open("./data/" + name + "-images.idx3-ubyte", "rb")
    csvFile = open("./data/" + name + ".csv", "w", encoding="utf-8")

    magicNo, labelCnt = struct.unpack(">II", labelFile.read(8))
    print(magicNo, labelCnt)
    magicNo, imageCnt = struct.unpack(">II", imageFile.read(8))
    print(magicNo, imageCnt)
    rows, cols = struct.unpack(">II", imageFile.read(8))
    pixels = rows * cols

    for i in range(labelCnt):
        label = struct.unpack("B", labelFile.read(1))[0]   # 답
        imgdata = list(map(lambda b: str(b), imageFile.read(pixels)))  # 28 * 28
        csvFile.write(str(label) + ",")
        csvFile.write(",".join(imgdata) + "\n") #\r\n에서 \r을 제거할 경우 실행됨

    # for j, x in enumerate(imgdata):
    #     if j % 28 == 0:
    #         print("\n")
    #     print('{:4s}'.format(str(x)), end='')

    # print("\n\n label=", label)

    labelFile.close()
    imageFile.close()
    csvFile.close()


writeCsv('train')
writeCsv("t10k")