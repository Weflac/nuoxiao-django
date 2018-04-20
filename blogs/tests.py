# -*- coding: utf-8 -*-

import functools


# 添加用户
def showary(*args, **kwargs):
    print(args)
    print(kwargs)


p1=functools.partial(showary,1,2,3)
p1()
p1(4,5,6)
p1(a='python', b='itcest')


p2=functools.partial(showary, a=3, b='liunx')
p2()
p2(1,2)
p2(a='python', b='itcest')



#
# class testAdd(unittest.TestCase):
#     def test_int(self):
#         self.assertGreater(showary())
#     def test_add(self):
#         self.assertFalse(showary())
#
# if __name__ == '__main__':
#     unittest.main()

