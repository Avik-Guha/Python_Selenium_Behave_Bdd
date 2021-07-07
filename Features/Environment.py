import os
from Base import Base
import hashlib
from behave.model_core import Status


def before_all(context):
    # By default all driver binaries are saved to user.home/.wdm folder.
    # You can override this setting and save binaries to project.root/.wdm.
    os.environ['WDM_LOCAL'] = '1'

    # Clear log file
    file = open("Logs/info_log.txt", "w")
    file.close()

    environment = context.config.userdata.get("environment")
    # environment = "QA"
    Base.set_environment(environment)
    Base.set_logger()


# This method will remove duplicate lines from log file and create final_log.txt file
def after_all(context):
    output_file_path = "Logs/final_log.txt"
    input_file_path = "Logs/info_log.txt"

    completed_lines_hash = set()

    output_file = open(output_file_path, "w")

    for line in open(input_file_path, "r"):
        hash_value = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hash_value not in completed_lines_hash:
            output_file.write(line)
            completed_lines_hash.add(hash_value)
    output_file.close()


def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser")
    # browser = "Chrome"
    Base.set_driver(browser)
    context.driver = Base.get_driver()
    return context.driver


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == Status.failed:
        context.driver.get_screenshot_as_file("Screenshots/screenshot.png")

# before_all(context)
# after_all(context)
# before_feature(context, Features)
# after_feature(context, Features)
# before_scenario(context, scenario)
# after_scenario(context, scenario)
# before_tag(context, tag)
# after_tag(context, tag)
# before_step(context, Steps)
# after_step(context, Steps)

# This file name must always be Environment.py
