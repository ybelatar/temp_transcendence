FROM acorp/django-base:latest

ADD backend /app/backend

WORKDIR /app/backend

RUN apt-get install -y \
	curl

COPY tools/entrypoint.sh /app/backend/entrypoint.sh
RUN chmod +x /app/backend/entrypoint.sh

EXPOSE 8000

CMD ["/app/backend/entrypoint.sh"]
