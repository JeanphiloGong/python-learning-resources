#coding=UTF-8
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':#和message进行比较 ，如果不等于就会继续循环
	message = input(prompt)
	print(message)
