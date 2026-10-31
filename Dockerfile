FROM ctfd/ctfd:3.8.9

# First boot: run CTFd's own setup form in-process with the admin from CTFD_ADMIN_*, after
# migrations and before the server listens, so /setup is never open to whoever finds the URL
# first. Later boots find setup done and skip it.
COPY railway-setup.py /opt/CTFd/railway-setup.py
ENTRYPOINT ["sh", "-c", "python ping.py && flask db upgrade && python railway-setup.py && SKIP_DB_PING=true exec /opt/CTFd/docker-entrypoint.sh"]
