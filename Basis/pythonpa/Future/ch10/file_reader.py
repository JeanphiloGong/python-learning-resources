# coding=gbk
file_path = r"C:\Users\34282\Desktop\������\�ļ�����\ch10\pi_digits.txt"
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents)
	for line in file_object:
		print(line)


file_path = r"C:\Users\34282\Desktop\������\�ļ�����\ch10\pi_digits.txt"
with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())


with open(file_path) as file_object:
	lines = file_object.readlines()
	print(lines)
	
for line in lines:
	print(line.rstrip())
