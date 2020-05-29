print('进入了test__name__模块')
# __name__指的是当前模块的名字
# 如果是直接运行的当前.py文件,那么__name__就等于__main__
# 否则__name__等于test__name__
print(__name__)

if __name__ == '__main__':
    print('进入了test__name__中的main')
