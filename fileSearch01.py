# fileSearch.py
# dH 9/25/22
#
#  In this code challenge you will search an email file and list all the senders of all email messages. Email format
#  is prefix@domain. For example: firstlast99@gmail.com -- firstlast99 is the prefix and gmail.com is the domain. For
#  this program, you will call the prefix@domain the sender. Your Python program will use split() to parse the
#  prefix and domain and a Python dictionary to tabulate the number of email messages received from each prefix. For
#  this code challenge, consider prefix segments to uniquely identify each sender. Output your dictionary in many
#  ways: natural state (this could be any order and could be changed by your program (not by you)), values sorted
#  by value, keys sorted by keys, items sorted by vale and key, ascending and descending.
#  Advanced: Produce output that tabulates prefix@domain (does not parse into two parts) sends and use the
#  dictionary get() method to replace the if/else stmt. Explain how the get() method works and saves you from
#  writing code!
#

# References
#   https://www.w3schools.com/python/python_ref_file.asp
#   https://www.w3schools.com/python/python_ref_string.asp
#   https://www.w3schools.com/python/python_lists.asp
#   https://www.w3schools.com/python/python_lists_methods.asp
#   https://www.w3schools.com/python/python_dictionaries.asp
#   https://www.w3schools.com/python/ref_dictionary_get.asp
#   https://docs.python.org/3/tutorial/datastructures.html
#   https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp



# Open a file, read the file line by line and search for lines that begin with "From " (note the space after
# "From"). Lines that begin with "From:" (note the colon after "From" ) do not contain the sender.
#   1) Count the number of found lines and output the count.
#   2) Use split() to parse the line into separate words.
#   3) Use the second word as the email sender.
#   4) Output the email sender.
#   5) Use split('@') to parse the prefix and domain
#   6) Output the email sender's prefix and domain
#   7) Use a Python dictionary to count the number of messages from each sender
#   8) Demonstrate tuples in a dictionary

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# set accumulator to 0
# TODO: What is an accumulator and how are they used?
count = 0
# Read the file line by line.
# TODO: Where did my_file_handle come from? How was it created? What is it? What is my_line?
for my_line in my_file_handle:
    # TODO: What does [0:5] mean? What is this decision control structure checking?
    if (my_line[0:5] == "From "):
        # TODO: What are the elements of a list? What does split() do?
        my_list_of_words = my_line.split()
        print("dir(list):")
        # TODO: What is x[1] here?
        print(my_list_of_words[1])
        # TODO: What is happening here?
        two_parts = my_list_of_words[1].split('@')
        print(two_parts)
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)
        # TODO: Why don't we use count++?
        count = count + 1

print("\n\nThere were", count, "lines in the file with 'From ' as the first word!\n\n")

# Close the file so you can use it for your dictionary.
my_file_handle.close()

print("\n\n******** Python Dictionary Section ************\n\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

# TODO: Use a Python dictionary to tabulate the number of messages from each sender
num_of_msgs = dict()

# Use the loop you created for prefix/domain parsing.
for my_line in my_file_handle:
   if (my_line[0:5] == "From "):
        my_list_of_words = my_line.split()
        two_parts = my_list_of_words[1].split('@')
        prefix = two_parts[0]
        domain = two_parts[1]
        print(prefix)
        print(domain)
        # add item to dictionary
        # check to see if prefix exists in the dictionary
        # syntax is: key in dictionary
        if (prefix in num_of_msgs):
            print(num_of_msgs[prefix], " ", prefix,  " exists as a key in this dictionary")
            # add one to the value representing the number of messages
            num_of_msgs[prefix] = num_of_msgs[prefix] + 1
        else:
            # create a new key in the dictionary with one message
            num_of_msgs[prefix] = 1

# Loop through the dictionary to find the sender with the most messages
big_count = None
big_word = None
# TODO: What other programming language can use two variables as loop control variables?
for my_key,my_val in num_of_msgs.items():
    if big_count is None or my_val > big_count:
        big_word = my_key
        big_count = my_val

print("\n Most messages is by...")
print(big_word, big_count)

# Output the dictionary.
print("\n The num_of_msgs dictionary is: ")
print(num_of_msgs)
# Output the dictionary sorted by keys
print("\n The sorted-by-keys num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.keys()))
# Output the dictionary sorted by values
print("\n The sorted-by-values num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.values()))

# Demonstrate tuples and dictionaries
print("\nTuples in a dictionary:\n")
print("Key-Value Pairs are:")
for (myKey, myVal) in num_of_msgs.items():
    print(myKey, myVal)
print("\n...and printed as tuples...")
my_tuples = num_of_msgs.items()
print(my_tuples)

# Close the file
my_file_handle.close()

# Advanced: Use prefix@domain as the sender and the get() method in dictionary
print("\n*********** Advanced ************\n")

# Open the file.
file_name = "mbox-short.txt"
my_file_handle = open(file_name)

num_of_msgs = dict()

# Use the loop you created for prefix/domain parsing.
for my_line in my_file_handle:
   if (my_line[0:5] == "From "):
        my_list_of_words = my_line.split()
        sender = my_list_of_words[1]
        # print(sender)
        # add item to dictionary
        # TODO: Explain how  this line of code works and how it replaces the code on lines 88-95.
        num_of_msgs[sender] = num_of_msgs.get(sender, 0) + 1

# Loop through the dictionary to find the sender with the most messages
big_count = None
big_word = None
# TODO: What other programming language can use two variables as loop control variables?
for (my_key,my_val) in num_of_msgs.items():
    if big_count is None or my_val > big_count:
        big_word = my_key
        big_count = my_val

#print("\n Most messages is by...")
print(big_word, big_count)

# Output the dictionary.
print("\n The num_of_msgs dictionary is: ")
print(num_of_msgs)

# Output the dictionary keys sorted by keys
print("\n The sorted-by-keys num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.keys()))

# Output the dictionary values sorted by values
print("\n The sorted-by-values num_of_msgs dictionary is: ")
print(sorted(num_of_msgs.values()))

# Output the dictionary's key-value pairs sorted by key
# Loop through the dictionary in sorted key order
# () around k,v are added for programming clarity
print("\n Sorted by key...")
for (k,v) in sorted(num_of_msgs.items()):
    print(k,v)

# Output the dictionary's key-value pairs sorted by descending value
# create a temporary list of your dictionary items in value, key order
print("\n Sorted by value...")
tmp_list = list()
for (k,v) in num_of_msgs.items():
    # Note you have reversed the value/key order.
    tmp_list.append((v,k))
tmp_list = sorted(tmp_list, reverse=True)
print(tmp_list)
print("\n")
# Print a list of tuples
for my_tuple in tmp_list:
    print(my_tuple)

# Close the file
my_file_handle.close()




