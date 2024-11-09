words = ["abc","car","ada","racecar","cool"]

pndrome = ''
for word in words:
    if word==word[::-1]:
        return word

