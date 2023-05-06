ARG os_name="slim-bullseye"
ARG os_version="3.9.16"
ARG repo="python"

FROM ${repo}:${os_version}-${os_name}

ADD . /tmp/dependencies

WORKDIR /tmp/dependencies

RUN pip3 install --upgrade --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /tmp

CMD python3 dependencies/dependencies.py -s -f requirements.txt



