A script to back up the github.com/BlockChainCommons organisation, repositories, and metadata.
This script will also install a [systemd-timer](https://www.freedesktop.org/software/systemd/man/systemd.timer.html) to run this backup weekly if one does not exist.

# Prerequisites
- systemd
- python3.11

# Installation and Use
- This script assumes that it will be run as `root` on a dedicated lightweight VPS like a Linode Nanode or DigitalOcean Droplet.
- Create a [Github personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for the BlockchainCommons organisation.
- *NOTE: This token should be renewed annually.*
- Create a file named `bc-monitor-github-backup.classic-token` in `/root` which you will copy to the `blockchaincommons-github-backup` directory created in the steps below.

```console
cd /root
git clone git@github.com:BlockchainCommons/deployment-scripts.git
ln -sv deployment-scripts/github-backup blockchaincommons-github-backup
cd blockchaincommons-github-backup
cp -v /root/bc-monitor-github-backup.classic-token .
python3 -m venv env
source env/bin/activate
pip install -r ./requirements.txt
python3 ./backup.py
journalctl -xe --follow github-backup.timer
```
