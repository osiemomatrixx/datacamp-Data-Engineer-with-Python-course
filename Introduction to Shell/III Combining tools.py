"""
This chapter will show you how to use this power to select the data you want, and introduce commands for sorting values and removing duplicates.
"""

# How can I store a command's output in a file?
"""Combine tail with redirection to save the last 5 lines of seasonal/winter.csv in a file called last.csv."""
# $ tail -n 5 seasonal/winter.csv  > last.csv


## How can I use a command's output as an input?
"""Select the last two lines from seasonal/winter.csv and save them in a file called bottom.csv."""
# $ tail -n 2 seasonal/winter.csv > bottom.csv
"""Select the first line from bottom.csv in order to get the second-to-last line of the original file."""
# $ head -n 1 bottom.csv


## What's a better way to combine commands?
""" ** output | use the output -----> '|'== a pipe
"""
"""Use cut to select all of the tooth names from column 2 of the comma delimited file seasonal/summer.csv, then pipe the result to grep, 
with an inverted match, to exclude the header line containing the word "Tooth"""
# $ cut -d , -f 2 seasonal/summer.csv | grep -v Tooth


## How can I combine many commands?
"""Extend this pipeline with a head command to only select the very first tooth name."""
# $ cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 1


## How can I count the records in a file?
"""Count how many records in seasonal/spring.csv have dates in July 2017 (2017-07)."""
"""use grep with a partial date to select the lines and pipe this result into wc(short for "word count") with an appropriate flag to count the lines."""
# $ grep 2017-07 seasonal/spring.csv | wc -l
# out| 3


## How can I specify many files at once?
""" ** wildcards === to specify a list of files with a single expression ---- '*' 
    ** eg.---> cut -d , -f 1 seasonal/*
    ** eg---> cut -d , -f 1 seasonal/*.csv
"""
"""head to get the first three lines from both seasonal/spring.csv and seasonal/summer.csv"""
#  head -n 3 seasonal/spring.csv seasonal/summer.csv
""" out | ==> seasonal/spring.csv <==
Date,Tooth
2017-01-25,wisdom
2017-02-19,canine

==> seasonal/summer.csv <==
Date,Tooth
2017-01-11,canine
2017-01-18,wisdom""" 


## What other wildcards can I use?
""" ** wildcards less commonly used
      **   ? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
      **   [...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
      **   {...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.
      
--Which expression would match singh.pdf and johel.txt but not sandhu.pdf or sandhu.txt?"""
 # {singh.pdf, j*.txt}

