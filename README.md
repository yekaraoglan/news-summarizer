# news-summarizer
Fine-tuning pretrained T5 on news dataset

## Dockerizing the project
1. Build the docker image
```
cd path/to/repository
docker build -t summarizer .
```

2. Run the docker image
```
docker run -p 5000:5000 -t summarizer
```

3. Test the API
```
curl -X POST -H "Content-Type: application/json" -d '{"text":(news article that you want to summarize)}' http://localhost:5000/predict
```