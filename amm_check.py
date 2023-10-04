import os
import time

def is_app_running(app_name):
    """Check if app is running."""
    try:
        # The pgrep command searches for processes by name.
        # If the app is running, the command will return a process ID.
        # Otherwise, it will not return anything.
        output = os.popen(f'pgrep {app_name}').read().strip()
        return bool(output)
    except Exception as e:
        print(f"Error checking if {app_name} is running: {e}")
        return False

def launch_app(app_name):
    """Launch the app."""
    try:
        os.system(f'open -a {app_name}')
    except Exception as e:
        print(f"Error launching {app_name}: {e}")

def main():
    app_name = "amm"
    log_filename = "amm_check_log.txt"
    
    while True:
        if is_app_running(app_name):
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {app_name} is running. Will check again in 30 seconds.")
            with open(log_filename, "a") as log_file:
                log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Checked: {app_name} is running.\n")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {app_name} is not running. Launching it now.")
            with open(log_filename, "a") as log_file:
                log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Checked: {app_name} is not running. Launched it.\n")
            launch_app(app_name)
        time.sleep(30)

if __name__ == "__main__":
    main()
