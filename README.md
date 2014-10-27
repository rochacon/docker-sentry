# Simple Sentry Docker image

## Setup and run

1. Modify `sentry.conf.py` as needed.
1. Start a Postgres instance and create the `sentry` database
1. Start a Redis instance
1. Build the Sentry container: `docker build -t sentry .`
1. Run Sentry web instance with `DATABASE_URL` and `REDIS_ENDPOINT` environment variables, like: `docker run -d -e DATABASE_URL=postgres://postgres:postgres@172.17.0.3:5432/sentry -e REDIS_ENDPOINT=172.17.0.4:6379 sentry start`
1. Run Sentry worker instance with `DATABASE_URL` and `REDIS_ENDPOINT` environment variables, like: `docker run -d -e DATABASE_URL=postgres://postgres:postgres@172.17.0.3:5432/sentry -e REDIS_ENDPOINT=172.17.0.4:6379 sentry worker -B`
