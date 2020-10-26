import re
import sys
import glob

# Get and check user inputs
if len(sys.argv) < 2:
    raise ValueError('Please provide paths to files or folder.')

if sys.argv[1].endswith('.tex'):
    # Case latex paths (filter .tex files)
    latex_paths = list(filter(lambda a: a.endswith('.tex') ,sys.argv[1:]))
else:
    # Case latex folder
    latex_folder = sys.argv[1]
    latex_paths = glob.glob(latex_folder + '/*.tex')

# latex_paths = ['introduction.tex', 'preliminaries.tex'] # Manually provided latex paths

matches = []

for latex_path in latex_paths:
    latex_file = open(latex_path, "r")
    latex_content = latex_file.read()

    # https://stackoverflow.com/questions/29403784/python-extract-pattern-from-string-using-regex
    # https://stackoverflow.com/questions/12091065/negative-pattern-matching-in-python

    pattern = re.compile(r'\$.*?(?!\\).\$')
    matches += [match for match in re.findall(pattern, latex_content)]

# Compute stats
stats = [
[
m1,
matches.count(m1),
sum([m2.count(m1[1:len(m1)-1]) for m2 in matches if len(m2) > len(m1)])
]
for m1 in set(matches)
]

# Put stats into a pandas DataFrame and visualize
import pandas as pd
pd.set_option('display.max_rows', None)

def pretty_print(df):
    print(df.to_markdown())

stats_table = pd.DataFrame(stats, columns = ['math_expression', 'isolated_occurences', 'occurences_as_substring'])

# Query DataFrame
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

r1 = pysqldf("SELECT * FROM stats_table ORDER BY isolated_occurences, occurences_as_substring, -length(math_expression);")
print(r1)

r2 = pysqldf("SELECT * FROM stats_table WHERE length(math_expression) < 20 AND (isolated_occurences > 1 OR occurences_as_substring > 1) ORDER BY isolated_occurences, occurences_as_substring, -length(math_expression);")
pretty_print(r2)

# Remind considered files
print('\nConsidered files: ' + str(latex_paths))
