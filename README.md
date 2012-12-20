This app runs a tiny web service on your mac on port 8181, which any mobile device can connect to using a web browser.

When connected, the browser is presented with a set of buttons. Clicking any of the buttons triggers a piece of
applescript on the server-side to perform the action.

### Setup

The simplest setup is as follows. Anywhere on your system where you feel comfortable (no root privs or anything), do
this:

```
mkdir ikeys
cd ikeys
virtualenv -p python2.7 .
source bin/activate
git clone https://github.com/redspider/ikeys.git .
```

Now it's all installed, all you have to do to run it up is (in the same dir):

```
python app.py
```

and it should fire up and show some log stuff and then wait. Then you can open your ipad and point it at your mac's IP
on port 8181, ie http://10.0.77.5:8181/

Once you've got the screen with the buttons, check the bell button says "Bing". if that works, put the app on your
homescreen and launch it from there for a variant without the url bar.
