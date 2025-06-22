# Use a small Python image
FROM python:3.11-slim

# Install Robot Framework and RequestsLibrary
RUN pip install --no-cache-dir \
      robotframework==7.3 \
      robotframework-requests

# Make /robot our working directory
WORKDIR /robot

COPY . /robot

RUN mkdir -p /robot/output

CMD ["robot", "--pythonpath", ".", "--outputdir", "output", "tests"]
