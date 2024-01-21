FROM python:3.12
# RUN apt update
# RUN apt upgrade -y
# RUN apt install python3 -y
# RUN apt install python3-pip -y
WORKDIR /VoloAssignment
ADD . /VoloAssignment
COPY ./requirements.txt /VoloAssignment/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /VoloAssignment
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]