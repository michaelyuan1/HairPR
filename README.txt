
This is a splash page for an unlaunched B2B product,
which is very similar to AirPR but is actually called HairPR. It takes valid email addresses
and puts them in a database, and sends emails to those addresses thanking them for registering
with HairPR. 

I chose Django because I'd been interested in learning both Python and Django for some time
but hadn't had the motivation to. Django was interesting because it's somewhere of an intermediate
between Java's lack of meaningful abstraction and Rails' magic. Serving the static files was tricky,
but luckily I didn't have to write any CSS or jQuery because that had already been written by some
nice people. 


To deploy this as a local copy, you will need python virtualenv, and python v 2.7
Place your terminal in this root directory, where you found this file,
and use the following commands, which will start virtualenv:

virtualenv venv --distribute

source venv/bin/activate

pip install Django psycopg2

pip install -r requirements.txt

and finally the command:

python HairPR/manage.py runserver

which will run the server at localhost:8000

To see all the emails, got to localhost:8000/admin, using password admin and username admin, and clicking on the second users tab.



To deploy this on Heroku, first get a Heroku account, and configure your ssh keys, and get git. Initialize a git repository inside 
the HairPR root, add to it, and commit.
use the following command to create a Cedar app:

heroku create --stack cedar

then deploy using

git push heroku master

to check it, point your browser to wherever heroku made the app.

