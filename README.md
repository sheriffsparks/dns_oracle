Port of the bigram model DNS filter. This project does not run inline. Instead it is meant for communication with powerdns.

At a high level this program uses multiple tests to decide if a query is good or not. It listens internally on port 5555. A pdns lua script communicates with the service by sending it a query. The service returns "true" if the query is good and "false" if the query is bad. 

The methods in goodness determination include bigram probability, entropy, and analysis of what characters are used. As a final check stop, if the query is deemed valid, it is stored in a database. Every $UPDATE\_SECONDS (default=300) a thread queries the database and checks if a any second level domain has a high number of subdomains. If it does then the second level domain is added to a drop list and future queries for this domain. 

This program was used in a defensive cyber competition. The red team primarly used Cobalt Strike. We found that it broke DNS C2 for them with minimal impact to good DNS traffic. It has not been used in a network with a high number of users. I imagine it would not be efficient enough but maybe the techniques used can help you develop a more robust solution. 

### Dependicies
Your going to need zmq, python-systemd, and python-zmq and mysql the mysqldb stuff for python. If I missed something please let me know.

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

move config vars to a config file

make a better installer

make whitelisting easier
