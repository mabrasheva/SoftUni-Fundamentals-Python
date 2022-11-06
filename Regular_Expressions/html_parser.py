# Write a program that extracts a title and all the content of a HTML file:
# •	The title should be between the HTML tags <title> and <\title>.
# •	The content should be between the HTML tags <body> and <\body>.
# There might be different HTML tags, which you should ignore:
# •	Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, <\html>
# •	You also should ignore the HTML tag "\n"
# Example:
# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide free
# real-world practical\n training for young people who want to turn into\n skillful Python software engineers.
# </p></body>\n</html>"
# In this example the title is "News" and the content is "SoftUni aims to provide free real-world practical training for
# young people who want to turn into skillful Python software engineers."
# Input
# •	The input will be read from the console.
# •	The input consists of a single line.
# Output
# •	The content should be a single string.
# •	You should extract only the text without the tags.
# •	When you extract the title and the content, you should print the result in the following format:
# o	"Title: {extracted title}"
# o	"Content: {extracted content}"

import re

text = input()

pattern_title = r"<title>(.*)<\/title>"
pattern_content = r"<body>.*<\/body>"
pattern_tags_to_remove = r"<[^>]*>|\\n"

title = re.search(pattern_title, text)
content = re.search(pattern_content, text)
title = title[0]
content = content[0]
tags_title = re.findall(pattern_tags_to_remove, title)
tags_content = re.findall(pattern_tags_to_remove, content)
if tags_title:
    for tag in tags_title:
        title = title.replace(tag, "")

if tags_content:
    for tag in tags_content:
        content = content.replace(tag, "")

print(f"Title: {title}")
print(f"Content: {content}")
