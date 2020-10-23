FROM python:3.7-slim

# select the directory to run the app
WORKDIR /app

# set environment variables
ENV STRINGS=['ab','abc','abc','abc','bc','bc']

#copy all files needed in the directory app
COPY . /app 

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Run function
ENTRYPOINT [ "python3", "main.py" ]

#default string array
CMD ["ab_ac_abc"]