# python-yt-mp3

## For your info
This tool downloads only the audio from Youtube videos. If you would like support for videos as well, feel free to open a GitHub Issue :) 

## Setup Instructions

### 1. Clone the Repository
```sh
git clone git@github.com:vromanyu/python-yt-mp3.git
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to keep dependencies isolated:
```sh
python -m venv .venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
Use `requirements.txt` to install the necessary packages:
```sh
pip install -r requirements.txt
```

### 5. Build the Project
If you're on Linux, you should make the `build.sh` executable.
```sh
chmod +x build.sh
```
Run `build.sh` if you're on Linux, or `build.ps1` if you're on Windows.

### 6. Run the Tool
The tool runs in the command line. As parameters we pass the desired URLs:
```sh
./converter "url1" "url2" "urlX"
```
There's also Docker support. To run the tool and dispose the container aftewards we can execute:
```bash
docker run --rm -v ./output:/app/output vromanyu/python-yt-mp3:latest "url1" "url2" "urlN"
```

