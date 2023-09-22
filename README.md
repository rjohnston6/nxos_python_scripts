# NXOS Python Scripts

*A collection of Python Scripts and Modules to work with NX-OS systems.*

---

## Motivation

To assist in quering and reporting on various elements of Nexus configurations and deployments, this repo is a collection of scripts and modules that can help simplify the collection of data across a number of devices. The initial purpose is to connect to devices and identify orphan ports across a deployment.

## Features

Inital features include options to display data in 2 methods.
- Output to a formatted table on the terminal for quick point in time analysis
- Optionally, export to a csv file the returned results.

## Requirements
The scripts created are tested using python version 3.11.4 and are not validated against previous versions. To avoid issues ensure python version meets the minumum version of 3.11.4 and python libraries/modules match the versions listed in the ```requirments.txt``` file. 

Please adhere to the practice of using Python virtual environments to avoid inadvertently upgrading versions of python and associated libraries used by your systems operating system.
## Usage

To use the included scripts start by cloning the repo to your local development machine. 

```git clone https://github.com/rjohnston6/nxos_python_scripts.git```

**Note**: It is recommended to create or use an existing python Virtual Environment, the remainder of the instructions assumes an activated virtual environment before proceeding.

Next install the required Python Libraries needed to run the script. From a command line use pip and reference the ```requirements.txt``` file to install the required libraries.

```pip install -r requirements.txt```

Once cloned to report on the "orphan ports"  in the environment start by creating or editing the included ```devices.txt```  file with a list of management IP address for your devices one IP per line. 

Finally, to query the devices run the following:

```python orphan_ports.py -t```

This will execute the script asking for a global username and password to be able to connect to the devices and then return a formated table to the terminal. Optional flags are available that can be used when executing the script.

| Flag | Usage |
| ---- | ----- |
| -t | Display terminal formated table |
| -r | Output to a CSV report named "orphan_ports.csv" |
| -d STRING | To define an alternate .txt file of management addresses |


## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Russell Johnston <rujohns2@cisco.com>

## Credits

This project was an adaptation of a very smart engineer Juan Andres Rocha Bravo, that created a similar script to query devices and output results to multiple files based on the device and a provided list of commands. Without his previous work this would have taken much longer to prepare.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
