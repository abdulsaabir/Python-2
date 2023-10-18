def count_vowels(string):
    vowels = 'aeiou'
    count = 0

    for char in string:
        if char.lower() in vowels:
            count += 1

    return count

# Example usage:
var1 = count_vowels("hello world")
print(var1)


var2 = count_vowels("GOOD  morning")
print(var2)

var3 = count_vowels("I will be There no Matte WHAT")
print(var3)