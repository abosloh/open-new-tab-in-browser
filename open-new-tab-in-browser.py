
list = ['http:www.google.com','http:www.google.com','http:www.google.com','http:www.google.com']

# example 1
import webbrowser

for url in list:
  webbrowser.get('firefox').open_new_tab(url)


# example 2
import os 

for url in list:
  os.system("firefox -new-tab %s" % url)


