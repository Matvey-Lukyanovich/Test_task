import pyshorteners

link = input("URL")
s = pyshorteners.Shortener().tinyurl.short(link)
print(s)