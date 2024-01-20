FROM ubuntu
RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y
WORKDIR /VoloAssignment
COPY . /VoloAssignment
RUN pip3 install -r requirments.txt
EXPOSE 8000
CMD ["python3","manage.py", "runserver"]