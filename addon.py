import subprocess

steamLink = "steamlink"

process = subprocess.Popen(steamLink, stdout=subprocess.PIPE)
output, error = process = process.communicate()