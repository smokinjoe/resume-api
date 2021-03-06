FROM python:3.6
ENV TZ UTC
ADD ./requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN mkdir -p /opt/logs && \
   mkdir -p /opt/media && \
  apt-get update && apt-get install --no-install-recommends -y \
  gcc \
  build-essential &&\
  pip install --no-cache-dir -r requirements.txt && \
  apt-get purge -y \
  gcc \
  build-essential && \
  apt-get clean autoclean && \
  apt-get autoremove -y && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/
EXPOSE 5000
ENV FLASK_APP resume_api/wsgi.py
ENV FLASK_CONFIG Dev
ENV FLASK_DEBUG 1
ADD . /opt/code/
RUN python /opt/code/setup.py develop
ARG REACT_APP_JOE_RESUME_API_SECRET
ENV REACT_APP_JOE_RESUME_API_SECRET "$REACT_APP_JOE_RESUME_API_SECRET"
CMD python resume_api/wsgi.py