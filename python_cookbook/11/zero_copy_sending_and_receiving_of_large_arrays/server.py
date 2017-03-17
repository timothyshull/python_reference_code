from socket import *

from zerocopy import send_from

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c, a = s.accept()

import numpy

a = numpy.arange(0.0, 50000000.0)
send_from(a, c)
c.close()
