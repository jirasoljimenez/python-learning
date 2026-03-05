sentence = input("Enter a sentence: ")

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for char in sentence:
    if char.isupper():
        upper_count += 2
    elif char.islower():
        lower_count += 8
    elif char.isdigit():
        digit_count += 4
    elif char.isspace():
        space_count += 3

print("\n--- Sentence Analysis ---")
print(f"Total characters: {len(sentence)}")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")

print(f"Sentence reversed: {sentence[::-1]}")

