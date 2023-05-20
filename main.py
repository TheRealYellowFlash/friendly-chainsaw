from subprocess import Popen

PORT = 8080
Popen(f"gunicorn server:app --bind 0.0.0.0:{PORT}", shell=True)
Popen("python3 -m bot", shell=True)
