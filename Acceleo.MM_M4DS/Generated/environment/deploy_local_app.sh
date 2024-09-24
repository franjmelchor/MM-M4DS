#!/bin/bash
set -e

sudo apt update --yes
sudo apt install python3-pip git --yes

REPO_URL="https://github.com/franjmelchor/MD4DSP-m2python.git"
PROJECT_DIR="./wf_model_dataset_python"

PYTHON_INTERPRETER="/usr/bin/python3.11"
DATA_LOCAL_DIR="/home/carlos/Escritorio/datasets"

CONTRACTS_SCRIPT="contracts_Job_Model_data_set_with_metanode_PYTHON_"
TRANSFORMATIONS_SCRIPT="transformations_Job_Model_data_set_with_metanode_PYTHON_"
WORKFLOW_SCRIPT="dataProcessing_Job_Model_data_set_with_metanode_PYTHON_"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Cloning the project repository..."
    git clone --depth 1 --branch develop $REPO_URL $PROJECT_DIR
else
    echo "Project directory already exists. Skipping clone."
fi

cp $CONTRACTS_SCRIPT.py ./wf_model_dataset_python/generated_code
cp $TRANSFORMATIONS_SCRIPT.py ./wf_model_dataset_python/generated_code
cp $WORKFLOW_SCRIPT.py ./wf_model_dataset_python/generated_code

cd "$PROJECT_DIR"


if [ -f "requirements.txt" ]; then
    echo "Installing project requirements..."
    $PYTHON_INTERPRETER -m pip install --no-cache-dir -r requirements.txt
else
    echo "requirements.txt not found. Skipping installation of requirements."
fi

clear

while true; do
    echo -e "\nWhat would you like to do?"
    echo "    1. Execute the Workflow validation contracts"
    echo "    2. Execute the Workflow data transformations"
    echo "    3. Execute the complete Pipeline (transformations and contracts)"
    echo -e "    4. Exit\n"

    read -r -p "Select an option: " option
    clear

    if [ "$option" -eq 1 ]; then
        echo -e "Executing the Workflow validation contracts...\n"
        if ! $PYTHON_INTERPRETER -m generated_code.$CONTRACTS_SCRIPT; then
            echo "An error occurred while executing the Workflow validation contracts."
        fi
    elif [ "$option" -eq 2 ]; then
        echo -e "Executing the Workflow data transformations...\n"
        if ! $PYTHON_INTERPRETER -m generated_code.$TRANSFORMATIONS_SCRIPT; then
            echo "An error occurred while executing the Workflow data transformations."
        fi
    elif [ "$option" -eq 3 ]; then
        echo -e "Executing the complete Pipeline...\n"
        if ! $PYTHON_INTERPRETER -m generated_code.$WORKFLOW_SCRIPT; then
            echo "An error occurred while executing the complete Pipeline."
        fi
    elif [ "$option" -eq 4 ]; then
        echo -e "Exiting the application...\n"
        break
    else
        echo -e "Invalid option. Please select a valid option.\n"
    fi
done
