#!/bin/sh

alembic init alembic
# alembic revision --autogenerate -m "Create messages table"
alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000
