names = ['John','Paul','George','Ringo']
a = list(filter((lambda x:(x == 'John') or (x == 'Paul')),names))
print(a)
