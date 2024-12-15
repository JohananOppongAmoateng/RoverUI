
import os
from django.shortcuts import render
from django.conf import settings
from .forms import FileUploadForm
from .utils import parse_input_file, generate_dataset, save_dataset_as_file


# Create your views here.

def index(request):
    result = None
    error = None
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            input_file = request.FILES["input_file"]
            input_format = form.cleaned_data["input_format"]
            sites_per_topic = form.cleaned_data["sites_per_topic"]

            try:
                # Parse input file
                topics = parse_input_file(input_file, input_format)

                # Generate dataset
                dataset = generate_dataset(topics, sites_per_topic)

                # Save dataset to file
                file_path = save_dataset_as_file(dataset)

                file_name = os.path.basename(file_path)
                file_url = settings.MEDIA_URL + file_name
                result = {
                    "file_url": request.build_absolute_uri(file_url),
                    "topics": topics,
                    "total_sites": len(dataset),
                }

                return render(request, "home.html", {"form": form, "result": result})
            except Exception as e:
                error = str(e)
                return render(request, "home.html", {"form": form, "error": error})

    else:
        form = FileUploadForm()
        return render(request, "home.html", {"form": form})


