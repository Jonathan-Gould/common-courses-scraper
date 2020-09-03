# An NYU Classes Web Scraper
This is a simple project I made to figure out who I have taken the most classes with. I figure someone else might think it's useful, so I'm sharing it here.
## Dependencies
This project uses Python 3 and the Selenium library. Selenium can be installed with pip, but be aware that you might also need a web driver. I used the `gecko` Firefox driver, which can be installed with `brew`.
## Usage
First, run `python scraper.py` to get the database.
Then I recommend copy-pasting the contents of `analysis.py` into a python REPL like iPython (`%cpaste` helps if you're using iPython). That way you can make queries faster.
## Maintenance
I've gotten what I wanted out of this script, so I'm not looking to maintain it.
However, if you think it's neat and want to improve it, I'd be happy to help you out.
## Disclaimer
I initially created this project for personal use, so it doesn't follow best coding practices.
Also, it might break if the NYU Classes website UI changes at all.
