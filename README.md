<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Advanced Call Forwarding with Python, Flask, and Twilio

[![Build status](https://api.travis-ci.org/TwilioDevEd/call-forwarding-flask.svg?branch=master)](https://ci.appveyor.com/project/TwilioDevEd/call-forwarding-flask)

Learn how to use [Twilio](https://www.twilio.com) to forward a series of phone calls to your state senators.

## Local Development

This project is built using the [Flask](http://flask.pocoo.org/) web framework, and runs on Python 2.7+ and Python 3.4+

To run the app locally, follow these steps:

1. Clone this repository and `cd` into it.

1. Create a new virtual environment with [virtualenv](https://virtualenv.pypa.io/en/latest/):

   ```bash
   virtualenv venv \
   source venv/bin/activate
   ```

   This application is compatible with Python versions 2.7 and 3.5, so feel free to use whichever installation you prefer in your environment.

1. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

1. Run the migrations:

   ```
   python manage.py db upgrade
   ```

1. Seed the database with data:

   ```
   python manage.py dbseed
   ```

   This will load `senators.json` and US zip codes into your SQLite database.
   **Please note:** our senators dataset is likely outdated, and we've mapped senators to placeholder phone numbers that are set up with Twilio to read a message and hang up.

1. Expose your application to the internet using
   [ngrok](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).
   In a separate terminal session, start ngrok with:

   ```
   ngrok http 5000
   ```

   Once you have started ngrok, update your TwiML application's voice URL setting to use your ngrok hostname. It will look something like this in your Twilio [console](https://www.twilio.com/console/phone-numbers/):

   `https://d06f533b.ngrok.io/callcongress/welcome`

1. Start your development server:

   ```
   $ python manage.py runserver
   ```

   Once ngrok is running, open up your browser and go to your ngrok URL.

## Run the Tests
Run the tests locally with [coverage](http://coverage.readthedocs.org/):

```
coverage run manage.py test
```

You can then view the coverage results with `coverage report` or build an HTML report with `coverage html`.

*Note: If coverage seems to run way too many files, you can omit directories by adjusting your coverage command to something like `coverage run --omit=venv/* manage.py test`. See the [coverage docs](http://coverage.readthedocs.org/) for more information.*

## Meta
* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](https://opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
