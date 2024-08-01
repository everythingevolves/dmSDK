import subprocess
import time
import webbrowser

def main() -> None:
    # Launch Jupyter Lab
    proc = subprocess.Popen(["jupyter", "lab", "--notebook-dir=notebooks", "--no-browser", "--port=8888"])
    
    # Give JupyterLab some time to start up
    time.sleep(5)

    # Open the browser to the Jupyter Lab URL
    webbrowser.open("http://localhost:8888")

    # Wait for the Jupyter Lab process to complete
    proc.wait()

if __name__ == "__main__":
    main()