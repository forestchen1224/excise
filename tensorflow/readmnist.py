import numpy as np
import struct

def loadImageSet(which=0):
    print "load image set"
    binfile=None
    if which==0:
        binfile = open("train-images.idx3-ubyte", 'rb')
    else:
        binfile=  open("t10k-images.idx3-ubyte", 'rb')
    buffers = binfile.read()

    head = struct.unpack_from('>IIII' , buffers ,0)
    print "head,",head

    offset=struct.calcsize('>IIII')
    imgNum=head[1]
    width=head[2]
    height=head[3]
    #[60000]*28*28
    bits=imgNum*width*height
    bitsString='>'+str(bits)+'B' #like '>47040000B'

    imgs=struct.unpack_from(bitsString,buffers,offset)

    binfile.close()
    imgs=np.reshape(imgs,[imgNum,width,height])
    print "load imgs finished"
    return imgs

def loadLabelSet(which=0):
    print "load label set"
    binfile=None
    if which==0:
        binfile = open("train-labels.idx1-ubyte", 'rb')
    else:
        binfile=  open("t10k-labels.idx1-ubyte", 'rb')
    buffers = binfile.read()

    head = struct.unpack_from('>II' , buffers ,0)
    print "head,",head
    imgNum=head[1]

    offset = struct.calcsize('>II')
    numString='>'+str(imgNum)+"B"
    labels= struct.unpack_from(numString , buffers , offset)
    binfile.close()
    labels=np.reshape(labels,[imgNum,1])

    #print labels
    print 'load label finished'
    return labels

if __name__=="__main__":
    imgs=loadImageSet(0)
    imgs=loadImageSet(1)

    #import PlotUtil as pu
    #pu.showImgMatrix(imgs[0])
    loadLabelSet(1)
