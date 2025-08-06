# start from the uv image that includes python + uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Copy project files
WORKDIR /cli-roman

COPY . .

RUN uv sync

RUN uv pip install .

#entrypoint to use the CLI command
# ENTRYPOINT [".venv/bin/roman"]

CMD [".venv/bin/uvicorn", "roman_api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
