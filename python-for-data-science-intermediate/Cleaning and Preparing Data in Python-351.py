## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`
num_rows = len(moma)

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace('one', 'two')
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

from csv import reader
open_file = open('artworks.csv')
read_file = reader(open_file)
moma = list(read_file)
moma = moma[1:]

var = 0

for row in moma:
    for n in row:
        x1 = row[2].replace('(','')
        x2 = x1.replace(')','')
        moma[var][2] = x2
        x1 = row[5].replace('(','')
        x2 = x1.replace(')','')
        moma[var][5] = x2
    var += 1

print(moma[:5])

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    if gender == '':
        gender = 'Gender Unknown/Other'
    else:
        gender = gender.title()
    row[5] = gender
    nationality = row[2]
    if nationality == '':
        nationality = 'Nationality Unknown'
    else:
        nationality = nationality.title()
    row[2] = nationality
print(moma[:5])

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
        return date
    elif date == "":
        return date

for row in moma:
    birthdate = row[3]
    deathdate = row[4]
    birthdate = clean_and_convert(birthdate)
    deathdate = clean_and_convert(deathdate)
    row[3] = birthdate
    row[4] = deathdate
    
print(moma[:3])

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for i in bad_chars:
        if i in string:
            string = string.replace(i, '')
    return string

stripped_test_data = []
for n in test_data:
    word = strip_characters(n)
    stripped_test_data.append(word)

print(stripped_test_data)


## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if '-' in string:
        split = string.split('-')
        date1 = int(split[0])
        date2 = int(split[1])
        date = round((date1 + date2) / 2)
        return date
    else:
        return int(string)

processed_test_data = []    

for date in stripped_test_data:
    data = process_date(date)
    processed_test_data.append(data)
    

print(processed_test_data)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date
print(moma[:5])