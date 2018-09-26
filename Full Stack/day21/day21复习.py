# 序列化模块
#     数据类型转化成字符串的过程就是序列化
#     方便存储和网络传输
#     json
#          dumps:从数据类型转向字符串
#          loads：与上相反
#          dump：和文件有关
#          load：泵loads多次
#     pickle
#          方法和json一样
#          dumps和load的时候，文件时rb或wb打开的
#          支持python所有的数据类型
#          序列化和反序列化需要相同的环境
#     shelve
#         只提供open方法
#         open方法获取了一个文件句柄
#         操作和字典类似

# 模块的导入
#     import
#     from import
#     as重命名
#     都支持多名字导入
#     sys.moudles记录了所有被导入的模块
#     sys.path 记录了导入包的时候寻找的所有路径