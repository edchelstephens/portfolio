# Deploy on Ubuntu 22.04 Server
- Follow tutorial on [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)
- Also check helpful post [Django deployment with Nginx and Gunicorn](https://pylessons.com/django-deployment) with [Youtube Video](https://www.youtube.com/watch?v=1fjpNXK7yqc)
- **Gotchas:**
    - ensure wsgi.py has correct DJANGO_SETTINGS_MODULE dotted path
    - ensure that www-data can cd to user home directories:
        - check if www-data has access
            `sudo -u www-data stat /home/username/location_to_static_files`
        - ensure www-data has access
            `sudo gpasswd -a www-data username`
