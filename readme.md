# image-renamer
## Use case
This script can help you rename multiple images to their resolution with the ability to add a prefix.
A possible scenario to the above is when you are exporting multiple assets from a program like Adobe Photoshop or
Illustrator at multiple resolutions. 

## Requirements
Script has been tested and is working on both **Windows 11** and **Ubuntu 22.04.2 LTS**  with **Python 3.10** installed.
Script's python code is based on very simple python concepts and any >=Python 3.7 should be able to handle it.

## How to install
1. Clone the repository to your local computer
2. Change your current directory to repository directory
3. Install the dependencies found on requirements.txt using pip either globally or in a virtual environment

## How to run
Navigate to script's main directory and run in terminal
```shell
python main.py
```
After executing the above a prompt to specify the path will be shown
```text
Enter path to rename images (if none, the local dir will be used): 
```
You don't have to use quotes if your path contains spaces around directory names. The script **does not search for images
recursively** (in each folder presented on path). If you wish to rename images contained in multiple folders you need to
run the script separately for each folder. The script searches the directory only for images having the suffix **.jpg**,
**.jpeg** and **.png**

After specifying the path a prompt to enter a prefix will be shown
```text
Enter prefix to rename images (if none, images will only contain their resolution in their name):
```
When specifying a prefix, please avoid using special or reserved words/characters like "COM1" or "CON" on Windows. If
a prefix is specified images gathered from the entered path will be renamed as follows:
```text
{PREFIX} - {RESOLUTION}.{ORIGINAL IMAGE SUFFIX}
```
If no prefix is specified at all images gathered from the entered path will be renamed as follows:
```text
{RESOLUTION}.{ORIGINAL IMAGE SUFFIX}
```
