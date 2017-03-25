# ![alt text](http://i.imgur.com/pgoj0JF.gif "Tweet@Trump")

Let's be honest here. President Trump's tweeting habits aren't the best. It seems like he says lots of crazy things on impetus. Well what if I want to tweet right back at him? That's where Tweet@Trump comes in.

This application, simply put, allows you to respond to President Trump's tweets (or anybody's tweets for that matter) with a generic message mere milliseconds after he sends one out. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need the [Git CLI](https://git-scm.com/downloads) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed on your machine. 

This project is written in [Python 3.6.0](https://www.python.org/downloads/)

### Installation

A step by step series of what to do to get Tweet@Trump running.

Clone the repository

``` Shell
git clone https://github.com/SishaarRao/Tweet-at-Trump.git
```

Go in and edit *secret.py* with your Consumer & Access keys

``` Python
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
CONSUMER_KEY = 'INSERT YOUR CONSUMER KEY HERE'
CONSUMER_SECRET = 'INSERT YOUR SECRET CONSUMER KEY HERE'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
ACCESS_KEY = 'INSERT YOUR ACCESS KEY HERE'
ACCESS_SECRET = 'INSERT YOUR SECRET ACCESS KEY HERE'

```

Go in and edit *message.txt* with the message you'd like to tweet

```
This is my message that I want to reply with. Don't include the @ in the beginning. Make sure it's less than 150 characters!

```

Go in and edit *main.py* with the USERNAME you'd like to tweet @.

``` Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# User that you want to immediately respond to
USERNAME = "realDonaldTrump"
...
```

## Running a Test

You can run *main.py* on your local machine.

``` Shell 
python3 main.py
```
Note: Your account will only automatically tweet while the program is running, so set the @ account to your friend's, tell him to tweet while it's running, and see if the program tweets in response.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

