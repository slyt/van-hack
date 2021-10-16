import subprocess

subprocess.check_output(['pyuic5', 'test.ui', '-o', 'test_ui.py'])