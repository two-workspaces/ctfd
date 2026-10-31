# Deploy and Host CTFd on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template/ctfd-platform?referralCode=sLjDXb&utm_medium=integration&utm_source=button&utm_campaign=ctfd-platform)

[CTFd](https://github.com/CTFd/CTFd) is the open-source (Apache-2.0) platform behind thousands of Capture The Flag competitions and security training courses: challenges with flags and hints, a live scoreboard, users or teams, and plugins. This template runs a pinned CTFd release on MariaDB and Redis, keeps uploaded challenge files on a volume, and creates your admin on first boot, so the setup page is never open to whoever finds the URL first.

## About Hosting CTFd

Three services on Railway's private network:

- **CTFd**: the web app (gunicorn with gevent). Each start applies database migrations first. Challenge files are stored on a volume at `/var/uploads`.
- **MariaDB** with a volume: users, challenges, solves and settings.
- **Redis**: CTFd's cache and session store.

Everything survives redeploys. A bare CTFd container with its default SQLite database and no volume loses the whole event on the next redeploy; this one does not.

## Common Use Cases

- Run a CTF for a club, meetup, school, conference or company security week
- Host internal security training with a private scoreboard
- Keep a year-round practice CTF for students or a team
- Test challenges before moving them to a large event

## Dependencies for CTFd Hosting

- None to start. SMTP is optional, for email confirmation and password resets.

### Deployment Dependencies

- [CTFd on GitHub](https://github.com/CTFd/CTFd)
- [CTFd documentation](https://docs.ctfd.io/)
- [CTFd configuration reference](https://docs.ctfd.io/docs/deployment/configuration)

### Implementation Details

**First use:**

1. Enter your email as `CTFD_ADMIN_EMAIL` and, if you like, an event name as `CTFD_NAME` when you deploy.
2. Open the CTFd service's domain once all three services are green.
3. Log in with `CTFD_ADMIN_NAME` (default `admin`) and the generated `CTFD_ADMIN_PASSWORD` from the CTFd service's Variables tab. Change the password in your profile, then open **Admin Panel** to add challenges, set start and end times, choose users or teams mode and pick a theme.

**Email:** add `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_TLS` and `MAILFROM_ADDR` to the CTFd service, or set them in Admin > Config > Email.

**Bigger events:** CTFd uses gevent workers, so one worker serves many players. For hundreds of players, give the CTFd service 1 GB or more and raise `WORKERS` to 2 or 3.

Notes and limits:

- The `CTFD_ADMIN_*` and `CTFD_NAME` variables only matter on first boot. Change them later inside CTFd.
- Back up the MariaDB volume (Railway backups) or use Admin > Config > Backup to export the event before major changes.
- Players' challenge instances (containers per player) are not part of CTFd core and are not included.

## Why Deploy CTFd on Railway?

Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

By deploying CTFd on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.
