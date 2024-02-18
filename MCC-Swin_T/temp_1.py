# import numpy as np
#
# for i in  range(20):
#     print(np.random.beta(0.8, 0.8))
#
# import  torch
# torch.set_printoptions(precision=4, sci_mode=False)
#
# def one_hot(x, num_classes, on_value=1., off_value=0.):
#     x = x.long().view(-1, 1) # torch.Size([2, 1])
#
#     on_value=0.5001
#     subCenter_value=0.2
#
#     label_1=torch.full((x.size()[0], num_classes), off_value).scatter_(1, x, on_value)
#     label_2 = label_1.scatter_(1, x + 1, subCenter_value)
#     label_3 = label_2.scatter_(1, x + 2, subCenter_value)
#
#     return label_3
#
# a=torch.tensor([0,2]) #torch.Size([2])
#
# # y1 = one_hot(a, 3, on_value=0.9001, off_value=0.0001)
# # y2 = one_hot(a.flip(0), 3, on_value=0.9001, off_value=0.0001)
# # print(y1)
#
#
# y1_ = one_hot(a*3, 3*3, on_value=0.9001, off_value=0.0001)
# y2_ = one_hot(a.flip(0)*3, 3*3, on_value=0.9001, off_value=0.0001)
#
# print(y1_)
# print(y2_)
#
# y_mer=y1_ * 0.1 + y2_ * (1. - 0.1)
# print(y_mer)
# print(y_mer.shape)
#
# a=torch.tensor([1,2,3,4,5,6],dtype=torch.float32)
# a=a.view(3,2)
# print(a)
#
# b = a.flip(0).mul_(0.8)
# print(b)
#
# def one_hot(x, num_classes, on_value=1., off_value=0.):
#     x = x.long().view(-1, 1) # torch.Size([2, 1])
#     return torch.full((x.size()[0], num_classes), off_value).scatter_(1, x, on_value)
#
# a=torch.tensor([1,3]) #torch.Size([2])
#
# y1 = one_hot(a, 5, on_value=0.9001, off_value=0.0001)
# y2 = one_hot(a.flip(0), 5, on_value=0.9001, off_value=0.0001)
# print(y1)
# print(y2)
#
# y_mer=y1 * 0.5 + y2 * (1. - 0.5)
# print(y_mer)
# print(y_mer.shape)
#
# b=torch.full((a.size()[0], 5), 0.0001) # torch.Size([2, 5])
# print(b)
#
# c=b.scatter_(1, a, 0.9001) #torch.Size([2, 5])
# print(c)
