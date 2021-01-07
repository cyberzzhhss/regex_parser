This is the program file. It should be possible to call the program on the command line with a text file as a parameter and output regexp matches in the format indicated below. For example,

  dollar_program.py target_text.txt
  telephone_regex.py target_text.txt

  dollar_output.txt -- this should contain the dollar amounts recognized by your program, one per line. The parts of the 
lines that are not part of the dollar amount should not be printed at all. 3 lines of example output might be something 
like this:

  $5 million
  $5.00
  five hundred dollars
  
  telephone_output.txt – the output file for telephone numbers, e.g.,
  212-345-1234
  777-1000