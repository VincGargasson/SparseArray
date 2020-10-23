FROM python:3.7-slim

# select the directory to run the app
WORKDIR /app

#copy all files needed in the directory app
COPY . /app

# set environment variables
ENV STRINGS ['ab','abc','abc','abc','bc','bc']

# Run function
ENTRYPOINT [ "python3", "main.py" ]

#default string array
CMD [ "ab,ac,abc"]