from math import *
net_struct = {
    
    'network': {'net': [[3, 1, 0,0], [3, 1, 0,0], [3, 1, 0,5]],
             'name': ['conv1', 'conv2', 'dilate_convolution']}
}

imsize = 224
def outFromIn(isz, net, layernum):
    totstride = 1
    insize = isz
    for layer in range(layernum):
        fsize, stride, pad,dilation = net[layer]
        if dilation>=1:
            fsize=(fsize-1)*dilation+1
        outsize = floor((insize - fsize + 2 * pad) / stride)+1
        insize = outsize
        totstride = totstride * stride
    return outsize, totstride

def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad,dilation = net[layer]
        if dilation>=1:
            fsize=(fsize-1)*dilation+1
        RF = ((RF - 1) * stride) + fsize
    return RF

if __name__ == '__main__':
    print "layer output sizes given image = %dx%d" % (imsize, imsize)

    for net in net_struct.keys():
        print '************net structrue name is %s**************' % net

        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize, net_struct[net]['net'], i + 1)
            rf = inFromOut(net_struct[net]['net'], i + 1)
            print "Layer Name = %s, Output size = %3d, Stride = % 3d, RF size = %3d" % (
            net_struct[net]['name'][i], p[0], p[1], rf)
