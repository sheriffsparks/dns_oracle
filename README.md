Port of the bigram model DNS filter created by CDR Bilzor. This project does not run inline. Instead it is meant for communication with powerdns.

### Dependicies
Your going to need zmq, python-systemd, and python-zmq and mysql the mysqldb stuff for python. If I missed something please update this list.

### Installation
The install script will install it as a systemd service. I recommend this because systemctl stop dnsoracle.service does a better job of killing the multithreaded handler.

The mysql database parameters are configurable in the source but right now the database name is dns and the table is dns. The user is dnspy and the password is dnstester. When installing on a new system you will need to manually build out this database. The table was created with the following:

```
CREATE TABLE dns(
query VARCHAR(50) PRIMARY KEY
);
```


### Running
To start the program run

```
sudo systemctl start dnsoracle.service
```

To test run dnsoracle_client "query"  where query is the string you want to try. False means the script thinks the query should be dropped

The program logs are handled by systemd. Run the following command to get a tailed viewing of the logs:

```
journalctl -u dnsoracle.service -f
```

### TODO
We will probably want to maintain our own list of blacklisted domains that we have gathered from other sources. I think the best way to implement this will be another table that just contains blacklisted domains. Then the list can be added to with a SQL command. This has the benifit of automatic blacklisting from other sources if we see fit.

