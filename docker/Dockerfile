FROM python:3.10-slim

ARG USER_ID
ARG USER_NAME
ENV HOME=/home/${USER_NAME} \
    VIRTUAL_ENV=/home/${USER_NAME}/venv
ENV \
  PYTHONUNBUFFERED=1 \
  DEBIAN_FRONTEND=noninteractive \
  TZ=Europe/Warsaw \
  PATH="${HOME}/.local/bin:${VIRTUAL_ENV}/bin:${PATH}" \
  PYTHONPATH="/app:${PYTHONPATH}" \
  BUILD_POETRY_LOCK="${HOME}/poetry.lock.build"

RUN apt-get -qq update \
    && apt-get -qq -y install --no-install-recommends vim gcc curl git build-essential libb64-dev unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip" \
    && unzip /tmp/awscliv2.zip -d /tmp \
    && /tmp/aws/install \
    && rm -rf /tmp/awscliv2.zip /tmp/aws

RUN addgroup --system --gid ${USER_ID} ${USER_NAME} \
    && useradd --system -m --no-log-init --home-dir ${HOME} --uid ${USER_ID} --gid ${USER_NAME} --groups ${USER_NAME} ${USER_NAME}

RUN chown -R ${USER_NAME}:${USER_NAME} ${HOME}
RUN mkdir -p /app && chown -R ${USER_NAME}:${USER_NAME} /app /tmp

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.7.1

USER ${USER_NAME}

COPY pyproject.toml *.lock /app/
WORKDIR /app

RUN poetry config virtualenvs.create false \
    && python -m venv ${VIRTUAL_ENV} \
    && pip install --upgrade pip setuptools \
    && poetry install && cp poetry.lock ${BUILD_POETRY_LOCK} \
    && rm -rf ${HOME}/.cache/*

USER root
COPY ./docker/scripts/* /
RUN chown -R ${USER_NAME} /*.sh && chmod +x /*.sh
RUN chown -R ${USER_NAME} ${HOME}/.local
USER ${USER_NAME}

RUN git config --global user.email "iletisimehmetalpay@gmail.com" \
    && git config --global user.name "Mehmet Alpay"

RUN python -m nltk.downloader stopwords && python -m nltk.downloader punkt

COPY . /app/
CMD ["/startup-script.sh"]
