import sys,re 
regex = r"[(]?\d{3}[)]?[(\s)?.-]\d{3}[\s.-]\d{4}"
with open(sys.argv[1], 'r') as f:
    test_str = f.read()
matches = re.finditer(regex, test_str, re.MULTILINE)
outFile=open("telephone_output.txt","w")
for matchNum, match in enumerate(matches, start=1):
    outFile.write(match.group()+"\n")
outFile.close()
