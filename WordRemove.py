def remove_word(str,word):
    str1=str.replace(word," ")
    return str1
str2="Hello  good mrng hi hello good"
print(str2)
str3=remove_word(str2,"Hello")
print(str3)

