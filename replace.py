# create a string
a_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# using the 'replace()' function to exchange the '!' characters for spaces within the string, 'a_sentence'
print(a_sentence.replace("!" , " "))

# use of the 'upper()' function to change a string that is written with lower case lettering.
print(a_sentence.upper() .replace("!" , " "))

# reprint in reverse
print(a_sentence[::-1] .upper() .replace("!" , " "))