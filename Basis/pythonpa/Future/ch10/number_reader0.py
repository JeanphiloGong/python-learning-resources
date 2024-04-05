coding = UTF-8
import json
filename = '"C:\Users\34282\Desktop\±‡≥Ãœ‡πÿ\pythonpa\Future\ch10\number.json"'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
