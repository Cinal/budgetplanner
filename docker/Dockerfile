FROM python:3.12.2
ARG USER_NAME


ENV home_dir /home/app
ENV app_name budgetplanner
ENV code_dir $home_dir/$app_name/


ARG GROUP_ID
ARG USER_ID
ARG USER_NAME

ENV POETRY_VERSION=1.2.0 \
    POETRY_HOME="/opt/poetry" \
    GUNICORN_VERSION=21.1.0

ENV PIP_VERSION=23.1.2
ENV POETRY_VERSION=1.5.1
ENV PYTHON_VERSION=3.12

ENV POETRY_RUN_PATH ${home_dir}/

RUN apt-get update -qq && apt-get install --no-install-recommends -y \
  sudo build-essential python3-dev python3-venv \
  postgresql-client libpq-dev libgdal-dev vim \
  libcurl4-openssl-dev libssl-dev python3-psycopg2 \
  wait-for-it wget vim-tiny git jq \
  && apt-get clean


RUN apt-get update && \
    apt-get install -y curl libpq-dev libcurl4-openssl-dev libssl-dev git && \
    curl -sSL https://install.python-poetry.org | python - && \
    pip install gunicorn==${GUNICORN_VERSION}

ENV VENV_PATH /home/$USER_NAME/venv

RUN addgroup --gid ${GROUP_ID} ${USER_NAME} || true
RUN adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} ${USER_NAME} || true

RUN mkdir ${home_dir} && chown -R ${USER_NAME} ${home_dir}
RUN mkdir ${VENV_PATH} && chown -R ${USER_NAME} ${VENV_PATH}
RUN chown -R $USER_NAME /usr/local/include/python3.12

USER $USER_NAME

RUN python3 -m venv $VENV_PATH
RUN $VENV_PATH/bin/python3 -m pip install -U pip==$PIP_VERSION
RUN $VENV_PATH/bin/pip3 --retries 10 install poetry==$POETRY_VERSION

ENV POETRY_PATH $VENV_PATH/bin/poetry
RUN $POETRY_PATH config virtualenvs.create false
RUN $POETRY_PATH config installer.max-workers 2


ENV PATH="${POETRY_HOME}/bin:${PATH}"
USER $USER_NAME

COPY cinal-budgetplanner/poetry.lock cinal-budgetplanner/pyproject.toml ${POETRY_RUN_PATH}
RUN (cd $POETRY_RUN_PATH && $POETRY_PATH install --no-interaction --no-ansi --only main)

ARG DEVELOP
RUN if [ "$DEVELOP" = "true" ]; then \
      cd $POETRY_RUN_PATH && \
      $POETRY_PATH install --no-interaction --no-ansi --only --dev; \
  fi

RUN $VENV_PATH/bin/pip3 install --retries 10 pygments ipython

ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONPATH=$home_dir/budgetplanner/

COPY cinal-budgetplanner/docker/start-app.sh /opt/
COPY cinal-budgetplanner/${app_name}/ ${code_dir}

RUN python -m pip install gunicorn

EXPOSE 8080

WORKDIR $code_dir

ENTRYPOINT [ "/opt/start-app.sh" ]
