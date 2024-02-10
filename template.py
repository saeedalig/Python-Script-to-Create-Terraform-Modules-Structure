import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

# Define directory names
directories = [
    "environments",
    "modules"
]

# Create top-level directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    logging.info(f"Created directory: {directory}")

# Create environment directories and files
for env in ["dev", "stage", "prod"]:
    env_path = os.path.join("environments", env)
    os.makedirs(env_path, exist_ok=True)
    logging.info(f"Created directory: {env_path}")
    for file in ["main.tf", "variables.tf", "terraform.tfvars", "outputs.tf"]:
        filepath = os.path.join(env_path, file)
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Created file: {filepath}")

# Create module directories and files
for module in ["vpc", "ec2", "sg"]:
    module_path = os.path.join("modules", module)
    os.makedirs(module_path, exist_ok=True)
    logging.info(f"Created directory: {module_path}")
    for file in ["main.tf", "variables.tf", "outputs.tf"]:
        filepath = os.path.join(module_path, file)
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass  # Create an empty file
            logging.info(f"Created file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}. Skipping creation.")
