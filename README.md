# Cowin-Vaccination-Availablity-Notification-App(CVANA)
## _Available for Assam only for Now_

[![N|Solid](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJcAAABGCAMAAAD2I/bBAAAAdVBMVEX////yL0byJ0DyK0PyHzvyHDnyIj3xFzb+8/TxACv1bXr7ztH3kJj97/D4pKvxAC36vcLzPlL0VWTxACb1dYH3lZ3xDzL94eP2fon96er7yMz82dv5uL35sbf0ZHL++vrzSVr0W2r4nKT2iZL5q7HwABrwAAq4UwrBAAAD8UlEQVRoge2Ya7OqOgyGoQXKRe5argKi6/z/n3iStOpy7YW74xed2X1nHEuh8DRJk4LjWFlZWVlZWVlZWf1dXX/JsmMSvpvjQUnr19L3PF/W5aF7N81VxRIx9yru1XHzbiJUN+XcfRCTu3dDOU7PA4IJZBRFua8MJ6r03VgSjcUl2xVN1w3Hfe6Tyfh7F0BSk3mW/t6V+WhA7r4TLI0IK3vonGOBfj09dibrvH2f4bwDnYeE/nfzSn/nl7kqDCeZ/Ow+IJi804Z960blE64iCkD5mOX4L8PSw//6VaxR/orlODuy2DWRra4MOF+eceH1rl9cKDi9cKEVnr/KVcJweYFGciorCrF1KfcYWBMY0rv6oaWAe8qVM5Acr1xlgMev2qsHc7EKsXLGWV44Tiw59xgAdGhJoUlaRlxP7jS0pCHTXOc96UWumGkvktl5OQ85ueMAXWewkRzxqrTZE1c5FkojlgNqzBh6pATVO5orbeh4UI9J1nbfZuY1JAQ3khXmSCXTdKQwYRP0dZBAGE14/VKJlwshJPxEDuebL2jUR+D7kjf9l17tNUV4LHD46EYe+NSvT4MhVwPW8VZscQpTHqJjId5b7MPY87CReffaOQXKsM7q6QmgXd2ALOpGN65YlQ0Yvb8VORYdzbhwNQoV7eg/ATgc71fTxPCB9fzIFazkcb9RnscAVI2L9wsXB669+FZ3o9GIa4WbBMrt5zqv9wDRlHUkC+rCpRXhWfUskpeReWSRKlbRp3iSxSpP/MlFiehu7sCo6h7g5kxfmQ660Qx6EeKjcrRcJpQnOGfikuCDgnOvzAANWrfHfoOrpKGsdmtqeEYVwJBLxxCnupTSAycdP3yhFCK63+1VNrSgAgjD8LrkDbgM/XjNXxW1J2pft5Fcn9ngOtIhxykP5FFpshemuKci9DTuH7ku3wNZR91hi4uWjBoYqhVrksUM88QjV3NbnbetN8ztmb2U8zplLxMuw7z6ow4tOh8FZw2G6WCDS9cP3JioGlsaberM6pDmgvDN4lGtFqJvNCHSb+UJV6W5ODv5d0/8VaZ1+6wKEQsQdFABBm7V3aLY5spU/mKemoIwLJKG+5xbdhRoQOU+/+LoJCbnbS7ndC8WDzvN5zLcF4acf+NSXoWpz2q1YF7b5ApPt/XLo4MhlvE+OhE+x2SFGwjYA3JI/SUaFXaxnOxdgP85r9NM4n5QhJOAbbQX4NhVCgbXB1HZ/3zMtkzfO9JDBSjxEQNuLquqWohmgVaJWbPHVlWGxRSj5iO9d6xq7LE9VdPuF6880Ye+p33se+3Hfgf42O8mzqd+Z0J95nc50kd+x7SysrKysrKysvpn9D8wvko1x/JxZgAAAABJRU5ErkJggg==)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

CVANA is a quick, reliable intreagated solution for automatic notification of availablity of slots and other details like date, name of facility, pin number, address etc. for nearest covid 19 vaccination centre. Right Now CVANA notified user's phone by direct message and whatsapp message. 

## Features

- Automation can be acheived using linux crons job and can be run periodically according to user requirement
- Can easily be converted to API using Flask, Django for any UI intreagration.
- Can be used to send notification for other State in India.


## Pre-Requisite

Twilio’s Programmable SMS API helps  add robust messaging capabilities to CWANA applications..CWANA uses a Twilio’s Programmable SMS for securely deliver sms and whatsapp message to the user recipient phone munber.

So Please create an account on [twilio][dill] and generate all tokens and api-key and paste in the app.py .
.

## Installation

CWANA requires [python](https://www.python.org/) v3.7+ to run.

Clone the CWANA public Repository from Github

```sh
git clone https://github.com/jaikumardas577/Cowin-Vaccination-Availablity-Notification-App.git
cd Cowin-Vaccination-Availablity-Notification-App
```

Install the dependencies and devDependencies.

```sh
pip install -r requirements.txt
```

For Running Manually...

```sh
python app.py
```

## Development

Want to contribute? Great! Please add issues and clone the repository.


## License

MIT



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://www.twilio.com/try-twilio>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
