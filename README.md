# Virtual Yoga Instructor

* [Description](#description)
* [Features](#features)
* [Setup](#setup)

## Description:
The application helps in finding the correctness of a yoga posture by comparing it with an expert's yoga pose. 

## Features:
* **When the desired pose is achieved by the yoga practitioner it beeps and shows next pose.**
* **Used affine Transformation to match two skeletons.**
* **MediaPipe was used to get stream of images of practitioner and return the response live.**

## Setup:

- # Only for Windows:
  - # in powershell(run as #Administrator)
    - Install chocolatey from [here](https://chocolatey.org/install)
                   or run
      ```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

    - Then, ```choco install make```.
- clone the repository:
  - ```git clone https://github.com/Praveendwivedi/HackFit.git``` 
- in terminal run following commands:
  - ```cd HackFit```
  - ```make```
  - for Windows:
    - ```Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser``` 
    - ```. HFenv\Scripts\activate```
  - for linux:
    - ```. ./HFenv/bin/activate```
  - finally:
    - ```make run```  

