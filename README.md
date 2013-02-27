BoilerFlask + ffmpeg
============

A simple boilerplate Flask application with support for ffmpeg and numpy.
This example uses the (somewhat old) python-ffmpeg-buildpack. Future support should use .vendor_urls and multibuildpack to reference the most up to date heroku-python-buildpack.

Instructions
------------
To deploy this application after cloned, simply:

	$ heroku create --buildpack git://github.com/integricho/heroku-buildpack-python-ffmpeg.git
	$ heroku config:add BUILDPACK_URL=git://github.com/integricho/heroku-buildpack-python-ffmpeg.git

You may also want to use `gunicorn` with `gevent`, in which case simply edit the `Procfile` and `requirements.txt` to add the dependencies and declare the web process.

To use it locally, you must download `pip` and `virtualenv`

    $ sudo easy_install pip
    $ sudo pip install virtualenv

Optionally, install `foreman` and `heroku` Ruby Gems

    $ sudo gem install foreman heroku



Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

On ubuntu, install the necessary packages:
	$sudo apt-get install python-dev 

Next, install the requirements in your isolated python environment.

    $ pip install -r requirements.txt



Now, you can run the application locally.

    $ python run.py

You can also run it using the production server if you install `libevent-dev` and `foreman`, but I am leaving that for another day, it also is difficult in Windows

    $ foreman start