def count_substring_occurrences(text, substring):
    text = text.lower()  # Convert the entire text to lowercase
    substring = substring.lower()  # Convert the letter/word will be searching to lowercase
    count = text.count(substring)  # use Count method to count the occurrences of the lowercase substring
    return count

# Test cases
text = "Python is a powerful and versatile programming language. Python is widely used for web development."
substring = "python"
result = count_substring_occurrences(text, substring)
print(f"The substring '{substring}' appears {result} times in the text.")
