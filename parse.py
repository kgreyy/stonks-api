from tika import parser

parsed = parser.from_file('AP Public Ownership Report as of 09.30.20.pdf')
print(parsed["content"])
