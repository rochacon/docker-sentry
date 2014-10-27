FROM python:2.7
RUN pip install sentry dj-database-url && pip install sentry[postgres]
ADD sentry.conf.py /etc/sentry.conf.py
ENTRYPOINT ["/usr/local/bin/sentry", "--config=/etc/sentry.conf.py"]
CMD []
EXPOSE 9000
