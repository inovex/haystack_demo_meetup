# Haystack Meetup Demo

Haystack demonstration used for discussions during a DataScience Meetup:
Meetup: Building LLM applications - inovex GmbH.

It showcases:

- Index & Query Pipelines
- Crawling website content
- LLM integration & multi-turn conversations

Additionaly it contains a `CustomPreprocessor` which handles crawled websites.

## Setup

### Virtual Env & Dependencies

Install the dependencies inside `requirements.txt`.
Execute the first cell in `main.py` to automatically install jupyter-notebook into the same environment.

### Elasticsearch Documentstore

An Elasticsearch Documentstore is required to run the haystack demo.
Deployment via docker is the easiest way.

```sh
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.11.2
```

### LLM API

LLM API credentials are required, to run later stages of the notebook.
An `.env` file provides a credentials template. 
(We used gpt3.5 from azure. If you plan to use another model read the [haystack-docs](https://docs.haystack.deepset.ai/docs/prompt_node), since the initialization format changes.)



