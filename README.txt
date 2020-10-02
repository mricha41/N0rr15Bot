Restarting the CherryPy server:

kill $(cat $HOME/webapps/norrisbot/pid)
~/webapps/norrisbot/autostart.cgi

Installing Python packages example:

PYTHONPATH=$HOME/webapps/norrisbot/lib/python3.7 easy_install-3.7 --install-dir=$HOME/webapps/norrisbot/lib/python3.7 --script-dir=$HOME/webapps/norrisbot/bin timezonefinder
