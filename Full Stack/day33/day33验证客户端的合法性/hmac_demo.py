# 访问谷歌
# http://www.google.com?username = 'bagaki', password = '079450'

# client --> server
# ip port
# server

# 检测一下客户端是否合法
# 不依靠登录认证

# import hmac    # hashlib
#
# h = hmac.new()  # secret_key 密钥，你想进行加密的bytes
# 密文 = h.digest()      # 拿到密文的内容
# hmac.compare_digest()  # 对比 密文和 另一个密文

import os
print(os.urandom(32))