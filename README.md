# RoverUI ✨

[![Python 3.10 - 3.11](https://img.shields.io/badge/python-3.10--3.11-blue.svg)](https://www.python.org/downloads/)

**RoverUI** is a web-based interface for leveraging the powerful WebRover library to generate high-quality datasets from structured topic files. Designed with simplicity and flexibility, RoverUI allows users to upload topic files in JSON, YAML, or Markdown formats and generate AI-ready datasets in JSONL format.

---

## 🚀 Features

- **WebRover Integration**: Seamlessly powered by the WebRover library for advanced dataset generation.
- **Multi-Format Input Support**: Accepts JSON, YAML, and Markdown files as input.
- **LLM-Ready Outputs**: Outputs datasets in JSONL format, suitable for training large language models.
- **User-Friendly Web Interface**: Upload files and download datasets with ease.
- **Dataset Management**: Organize and manage generated datasets efficiently.

---

## 🔄 Workflow

1. **Upload**: Provide a topic file in JSON, YAML, or Markdown format.
2. **Generate**: Let RoverUI use WebRover to scrape content and generate datasets.
3. **Download**: Retrieve your dataset in JSONL format.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or 3.11
- PostgreSQL (or any other supported database)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Area-25/roverui.git
cd roverui
```

2. **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up the database:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server:**
```bash
python manage.py runserver
```

Access RoverUI at `http://127.0.0.1:8000`.

---

## 🎨 Using RoverUI

### Uploading Topic Files
- Navigate to the "Upload File" page.
- Choose a topic file in JSON, YAML, or Markdown format.
- Click "Upload" to process the file.

### Generating Datasets
- Once the topic file is uploaded, RoverUI uses WebRover to generate a dataset.
- 

### Downloading Datasets
- After generation, download it in JSONL format.

---

## 🔧 Development

### Setting Up for Development

1. **Install WebRover library:**
```bash
pip install webrover
```

2. **Run tests:**
```bash
python manage.py test
```

3. **Lint code:**
```bash
flake8
```



---

## 🚨 Troubleshooting

1. **Database Issues:** Ensure PostgreSQL is running and the database credentials are correct in `settings.py`.
2. **File Upload Errors:** Check file format and ensure it conforms to supported JSON, YAML, or Markdown syntax.
3. **WebRover Errors:** Validate the installation and functionality of the WebRover library.

---

## 🌐 Roadmap

- Add support for additional output formats.
- Enhance UI/UX for better user experience.
- Integrate authentication for multi-user access.
- Introduce advanced dataset filtering and preprocessing options.

---

## 📚 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

RoverUI is powered by WebRover. Special thanks to all contributors and the open-source community.

