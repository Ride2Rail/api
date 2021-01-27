# Ride2Rail Categorizer

## Building

From the repository base directory:

```bash
docker build -t r2r/api:latest .
```

## Running

This will run the API and auto-reload it if the python files get modified:

```bash
docker run -d --name r2r-app -p 5000:80 -v $(pwd):/app r2r/api:latest /start-reload.sh
```
