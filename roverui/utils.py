import json
import os
import uuid
import yaml
from django.conf import settings
from webrover import WebRover


def parse_input_file(input_file, input_format):
    """Parse input file to extract topics."""
    if input_format == "json":
        data = json.load(input_file)
        topics = data.get("topics", [])
    elif input_format == "yaml":
        data = yaml.safe_load(input_file)
        topics = data.get("topics", [])
    elif input_format == "markdown":
        topics = [line.decode("utf-8").strip()[2:] for line in input_file if line.startswith(b"- ")]
    else:
        raise ValueError("Unsupported format")
    return topics


def generate_dataset(topics, sites_per_topic):
    """Generate a dataset using WebRover."""
    rover = WebRover()
    rover.scrape_topics(topics=topics, sites_per_topic=sites_per_topic)
    data = rover.get_dataset()
    print(data)
    return data


def save_dataset_as_file(dataset):
    """Save the dataset to a JSONL file and return the file path."""
    output_file_path = os.path.join(settings.MEDIA_ROOT, f"{uuid.uuid4()}.jsonl")
    with open(output_file_path, "w") as output_file:
        for entry in dataset:
            output_file.write(json.dumps(entry) + "\n")
    return output_file_path
