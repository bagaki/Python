# configparse
import configparser


config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression':'yes',
                     'CompressionLevel':'9',
                     'ForwardX11':'yes'}
config['bitbucket.org'] = {'User':'hg'}

config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

with open('example.ini', 'w') as configfile:
    config.write(configfile)

config = configparser.ConfigParser()

# ----------查找文件内容，基于字典的形式

print(config.sections())

config.read('example.ini')

print(config.sections())

print('bytebong.com' in config)  # False
print('bitbucket.org' in config)  # True

print(config['bitbucket.org']['user'])  # hg

print(config['DEFAULT']['Compression'])  # yes

# logging