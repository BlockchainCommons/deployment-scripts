import subprocess

ACCESS_TOKEN_FILE = 'bc-monitor-github-backup.classic-token'
ORGANIZATION      = 'BlockchainCommons'
BACKUP_DIRECTORY  = 'github.com-blockchaincommons-backup'

# https://wiki.archlinux.org/title/systemd/Timers
SYSTEMD_SERVICE_NAME = 'Github Backup'
SYSTEMD_TIMER_FILE_NAME = 'github-backup.timer'
SYSTEMD_SERVICE_FILE_NAME = 'github-backup.service'
SYSTEMD_TIMER_CONTENTS = f'''
[Unit]
Description={SYSTEMD_SERVICE_NAME}

[Timer]
OnCalendar=weekly
Persistent=true

[Install]
WantedBy=timers.target
'''

SYSTEMD_SERVICE_CONTENTS  = '''
[Service]
WorkingDirectory=/root/blockchaincommons-github-backup
ExecStart=/root/blockchaincommons-github-backup/env/bin/python3 /root/blockchaincommons-github-backup/backup.py

[Install]
WantedBy=multi-user.target
'''

try:
    result = subprocess.run(['systemctl', 'is-enabled', SYSTEMD_TIMER_FILE_NAME], 
            check = True)
except subprocess.CalledProcessError as e:
    with open(f'/etc/systemd/system/{SYSTEMD_TIMER_FILE_NAME}', 'w') as f:
        f.write(SYSTEMD_TIMER_CONTENTS)
    with open(f'/etc/systemd/system/{SYSTEMD_SERVICE_FILE_NAME}', 'w') as f:
        f.write(SYSTEMD_SERVICE_CONTENTS)
    subprocess.run(['systemctl', 'daemon-reload'], check = True)
    subprocess.run(['systemctl', 'enable', SYSTEMD_TIMER_FILE_NAME], check = True)
    subprocess.run(['systemctl', 'enable', SYSTEMD_SERVICE_FILE_NAME], check = True)
    subprocess.run(['systemctl', 'start', SYSTEMD_TIMER_FILE_NAME], check = True)

# TODO(nochiel) Print out active options before running the script.

from datetime import datetime
subprocess.run(['github-backup', ORGANIZATION, 
    '--token', f'file://{ACCESS_TOKEN_FILE}', 
    '--output-directory', f'{BACKUP_DIRECTORY}-{datetime.now()}', 
    '--all', 
    '--private', 
    '--organization'])

