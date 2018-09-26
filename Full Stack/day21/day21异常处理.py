# 程序一旦发生错误，就从错误的位置停下来不再继续执行后面的内容
# 使用try和exept就能处理异常
#     try时我们需要处理的代码
#     except：后面跟一个错误类型，当代码发生错误且错误类型符合的时候，就会执行except中的代码
#     except支持多分支
# 有没有一个能处理所有错误的类型：Exception
#     有了万能的处理机制仍然需要把能预测到的问题单独处理
#     单独处理的所有内容都应该写在万能异常之前
#     else：没有异常的时候执行else中的代码
#     finally:不管有没有异常都会执行
#         finally和return相遇时，依然会执行
#         函数里做异常处理用，不管是否异常去做一些收尾工作


try:
	ret = int(input('number >>>'))
	print(ret* '*')
except ValueErrpr:
	print('The value is wrong')
except Exception as e:
	print('Please input a number', e)
else:
	print('没有异常的时候执行else中的代码')
finally:
	print('(______')



def func():
	try:
		f = open('ifle', 'w')
		f.close()
		return True
	except:
		f.close()
		return False
	finally:
		f.close()

print(func())




