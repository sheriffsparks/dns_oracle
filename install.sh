#/bin/bash
if [ "${EUID}" -ne 0 ]
then
    printf "ERROR: please run with sudo\n"
    exit
fi


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"



printf "\n[*] Installing dnsoracle to /usr/local/bin/\n"
ln -sf ${DIR}/src/dnsoracle /usr/local/bin/

printf "\n[*] Installing dnsoracle_client to /usr/local/bin/\n"
ln -sf ${DIR}/src/dnsoracle_client /usr/local/bin/

printf "\n[*] Installling dnsoracle data files to /usr/local/etc/dnsoracle/\n"
mkdir /usr/local/etc/dnsoracle
cp ${DIR}/src/data/*.txt /usr/local/etc/dnsoracle/

printf "\n[*] Installing dnsoracle as a systemd service\n"
cp ${DIR}/dnsoracle.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable dnsoracle.service


