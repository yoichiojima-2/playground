# I will try to create a word frequency counter using the given script as inspiration

text = "Hello, how are you? I am just testing this script to see how it works. Let's have fun with it!"

# Removing punctuation and converting text to lowercase
cleaned_text = "".join(char.lower() if char.isalpha() else " " for char in text)

# Splitting the text into words
words = cleaned_text.split()

# Counting the frequency of each word
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sorting the words by frequency in descending order
sorted_word_freq = {
    k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
}

print(sorted_word_freq)
