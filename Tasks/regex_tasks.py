import re

text_1 = "the man's number is 123-456-7890"
output_1 = re.findall(r'\d{3}-\d{3}-\d{4}', text_1)
print(output_1)
# print(re.findall(r'[0-9-]+', text_1))

text_2 = 'tolu@yahoomail.com'
output_2 = re.findall('[A-Za-z]+[0-9]*@[a-z]+mail.com', text_2)
print(output_2)

text_3 = 'Alice and Bob are Good Friends'
output_3 = re.findall(r'\b[A-Z][a-z]+\b', text_3)
# output_3 = re.findall(r'\b[A-Z][a-z]+\b', text_3)
print(output_3)

text_4 = "Hello! How are you doing?"
output_4 = re.findall(r'[A-Za-z]+', text_4)
print(output_4)