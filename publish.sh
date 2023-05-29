#!/usr/bin/env bash

rm -rf dist && poetry version patch && poetry build && twine upload dist/*.whl
