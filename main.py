from subprocess import Popen


Popen(f"gunicorn server:app --bind 0.0.0.0:8080", shell=True)
Popen("python3 -m bot", shell=True)
