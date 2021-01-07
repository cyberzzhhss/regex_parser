import sys,re 
regex = r"(\$?(?:(\d+|a|half|quarter|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\w+teen|\w+ty|hundred|thousand|\w+illion).)*((\d+|and|((and|a)?.)?half( a)?|quarter|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\w+teen|\w+ty|hundred|thousand|\w+illion))(\s)?(dollar|cent)(s)?)|((\$(?:\d+.)*\d+)(.(\w+illion|thousand))?)"
with open(sys.argv[1], 'r') as f:
    test_str = f.read()
matches = re.finditer(regex, test_str, re.MULTILINE)
outFile=open("dollar_output.txt","w")
for matchNum, match in enumerate(matches, start=1):
    outFile.write(match.group()+"\n")
outFile.close()


