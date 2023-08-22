def can_segment(text, language, start=0):
    if start == len(text):
        return True

    for word in language:
        if text.startswith(word, start):
            if can_segment(text, language, start + len(word)):
                return True

    return False

# Example usage
text = "testcase3"
list_lang = ['test', 'case', 'se3', 'ca']

result = can_segment(text, list_lang)
print("Segmentation possible:", result)
