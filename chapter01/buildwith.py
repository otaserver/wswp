import builtwith
# 注意是安装python-whois而不是安装whois,2个包import的名称相同，但是调用的方法名不同。
import whois

# builtwith也不好使啊，没有显示使用什么构建的。
# print(builtwith.parse('https://am.zdmimg.com/202006/05/5eda0a9657e4f4910.jpg_e680.jpg'))

#无内容，报错。
# print(builtwith.parse('https://am.zdmimg.com/'))

# 勉强能显示出一些信息，应该是http的头信息中的内容。
# print(builtwith.parse('https://www.sina.com.cn'))
# print(builtwith.parse('https://www.lenovo.com'))

# domain = whois.whois('sina.com.cn')
# domain = whois.whois('am.zdmimg.com')
# domain = whois.whois('coqcod.com')
domain = whois.whois('arqhb.cn')
print(domain.__dict__)
print(domain.domain)
print(domain.expiration_date)
