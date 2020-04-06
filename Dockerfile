FROM python:3.7-slim-buster
ADD . .
WORKDIR .
RUN pip install flask gunicorn
EXPOSE 9000
CMD ["gunicorn", "-b", ":9000", "app:create_app()"]
