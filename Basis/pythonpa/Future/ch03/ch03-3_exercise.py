#coding=utf-8
words=['Aurora','Melody','Skye','Daisy','Soleil']
print(words)

print(sorted(words))#对列表进行临时排列

print(words)

print(sorted(words,reverse=True))#对列表进行临时反转排列

print(words)

words.reverse()#对列表进行永久性反转排列
print(words)

words.reverse()#对列表进行反转使其回到原来的状态
print(words)

words.sort()#对列表进行排列
            #一般都是主语words在前面，后面使用修饰词（sort）来进行修改
print(words)

words.sort(reverse=True)

print(words)
