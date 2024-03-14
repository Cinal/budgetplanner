#!/bin/bash

set -e

[[ -n "$code_dir" ]]

export PYTHONPATH="$(pwd):$PYTHONPATH"


#!/bin/bash

function unittests() {
  TESTS_FAILED=0

  pytest -c /home/app/lib/pyproject.toml \
    -p no:cacheprovider \
    --no-migrations \
    --html=artifacts/pytest-html/index.html \
    --cov-config=/home/app/lib//pyproject.toml \
    --cov=budgetplanner \
    --cov-report=html \
    "${@:-tests}" || TESTS_FAILED=$?

  return $TESTS_FAILED
}

function linters() {
  FAILED_RUFF=0
  FAILED_BLACK=0


  echo "# ruff check"
  ruff check --config /home/app/lib/pyproject.toml --fix . || FAILED_RUFF=$?
  echo "# black check"
  black --config /home/app/lib/pyproject.toml . || FAILED_BLACK=$?

  for code in $FAILED_RUFF $FAILED_BLACK; do
    if [ "$code" != "0" ] ; then
      return 1
    fi
  done

  return 0
}


TESTS_FAILED_UNIT=0
TESTS_FAILED_LINT=0

unittests $@ || TESTS_FAILED_UNIT=$?
linters $@ || TESTS_FAILED_LINT=$?

if [ "$TESTS_FAILED_UNIT" != "0" ] ; then
  echo "----------------------- "
  echo "< Unit Testing Failed ! >"
  echo "----------------------- "
  exit 1
fi

if [ "$TESTS_FAILED_LINT" != "0" ] ; then
  echo "----------------------- "
  echo "< Linters Testing Failed ! >"
  echo "----------------------- "
  exit 1
fi
