FROM alpine:3.14

# install python3 and pip3
RUN apk add --no-cache python3 py3-pip

# install npm
RUN apk add --no-cache npm

 # copy all files from current dir to /app in container
COPY . /app

# set /app as working dir
WORKDIR /app

# install dependencies
RUN pip install -r requirements.txt

# install node dependencies in /app/frontend
RUN cd frontend/vue-project && npm install

# build frontend
RUN cd frontend/vue-project && npm run build

# expose port 80
EXPOSE 80

# run app.py at container launch
CMD ["python3", "backend/app.py"]