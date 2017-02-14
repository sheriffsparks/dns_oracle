Port of the bigram model DNS filter created by CDR Bilzor. This project does not run inline. Instead it is meant for communication with powerdns.

### Dependicies
Your going to need zmq, python-systemd, and python-zmq i think.

The install script will install it as a systemd service. I recommend this because systemctl stop dnsoracle.service does a better job of killing the multithreaded handler.

To test run dnsoracle_client "query"  where query is the string you want to try. False means the script thinks the query should be dropped

to monitor the logs run: journalctl -u dnsoracle.service -f
