This is a Python Script that intakes a wikiepdia url and for each page, finds the first link in the text and goes to that page. The script ends when it finds the Philosophy wikipedia page with the url of 'https://en.wikipedia.org/wiki/Philosophy'

The script will print in the terminal the url of each new link it finds, along with the number of steps it takes to get to it's destination. 

If the number of hops reaches above 100, the script will end and will print that it has ended due to the hops reaching the maximum steps.

In order to run the command, first to install all requirements run: 

pip install -r requirements.txt

Finally, run the python script using python getting_to_philosophy.py "WIKIPEDIA URL"

For instance, run: 

python getting_to_philosophy.py https://en.wikipedia.org/wiki/Chicago