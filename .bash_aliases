# Bash aliases for Ubuntu Server
alias eb="vim ~/.bash_aliases"
alias rb="cd ~/ && . .bashrc"
alias sb="cat ~/.bash_aliases"

# Project
alias cded="cd ~/ed && source edenv/bin/activate"
alias cdp="cd ~/project && source projectenv/bin/activate && export DJANGO_SETTINGS_MODULE=portfolio.settings.production"


# Git
alias gs="git status"
alias gl="git log"

# Django
alias pym="python manage.py"
alias mkg="pym makemigrations"
alias mg="pym migrate"
alias cst="pym collectstatic"
alias psy="pym shell"

# System
alias sudosystemctl="sudo systemctl"
alias systemctlstatus="sudosystemctl status"
alias sudojournalctl="sudo journalctl"

# Postgres
alias psg="sudo -u postgres psql"


# Change directory
alias cdsysd="cd /etc/systemd/"
alias cdsys="cdsysd && cd system/"
alias cdh="cd ~/.ssh"
alias esh='eval "$(ssh-agent -s)" && ssh-add ~/.ssh/ed_github'

# Gunicorn
alias startapp="sudosystemctl start gunicorn.socket && sudosystemctl enable gunicorn.socket"
alias restartapp="sudosystemctl restart gunicorn && sudosystemctl daemon-reload && sudo systemctl restart gunicorn.socket gunicorn.service"
alias gunicornstatus="systemctlstatus gunicorn"
alias gunicornfile="file /run/gunicorn.sock"
alias gunicornsocket="systemctlstatus gunicorn.socket"
alias gunicornjournalsocket="sudojournalctl -u gunicorn.socket"
alias gunicornjournal="sudojournalctl -u gunicorn"
alias editgunicornservice="sudo vim /etc/systemd/system/gunicorn.service"
alias editgunicornsocket="sudo vim /etc/systemd/system/gunicorn.socket"


# Nginx
alias editnginx="sudo vim /etc/nginx/sites-available/project"
alias restartnginx="sudo nginx -t && sudo systemctl restart nginx"
alias reloadnginx="sudo nginx -s reload"
alias nginxstatus="systemctlstatus nginx"

# Logs
alias nginxlog="sudo tail -F /var/log/nginx/error.log"
alias nginxjournal="sudojournalctl -u nginx"
alias nginxaccess="sudo less /var/log/nginx/access.log"
alias nginxerror="sudo less /var/log/nginx/error.log"


# Python
alias pyclean="pyclean --verbose ."
