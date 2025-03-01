import numpy

demo_list = list(map(int, input().split()))

array = numpy.array(demo_list, int)

print(numpy.reshape(array, (3,3)))
