# Getting Started with Jupyter Notebook

The OpenDS4All curricular modules are targeted at Jupyter Notebook (or JupyterLab).  We include both sample code and lecture notebooks to illustrate basic concepts.

This guide, which can be used either by the instructional staff or students, focuses on how to set up a Jupyter Notebook environment for the class, and it has two main parts:

1. Instructions for setting up Jupyter Notebook on a commercial cloud-hosted environment (Section 1).
   
2. Instructions for setup on your local machine (Section 2).

## 1. Cloud Setup

Our suggestion is to use cloud-based infrastructure for doing the homework assignments in the OpenDS4All course.  This has several advantages:

* It supports any type of student machine, even including Chromebooks and iPads.
* It does not require any installation of software on local machines.

We provide several options.

### 1.1 Google Colab

Google Colab is perhaps the simplest setup.  To get set up, go to **colab.research.google.com** and sign in using a Google (GMail, Google Drive) account. (If you don't have one, you'll need to create one.)

Colab has several major positives:
1. Notebooks can be stored and shared on Google Drive.
2. Colab supports execution on relatively powerful machines and Google's TPUs.

However, it does require a Google account, and performance depends somewhat on availability of Google cloud resources.

### 1.2 Microsoft Azure Notebooks

Sign up by clicking on "Try It Now" at: [https://notebooks.azure.com/](https://notebooks.azure.com/).  You can Sign in using a Microsoft account, and from the "My Projects" page you will be able to launch new environments and notebooks.

### 1.3 Amazon SageMaker

For Amazon, we recommend you sign up for an Amazon account using [AWS Educate](awseducate.com).  

* From the `Services` menu you can select `SageMaker`.  
* You may need to change your region (via the drop-down menu) to US-East-2 (Ohio).  
 
There is an option in the left pane for `Notebook instances`. 
* Select `Create Notebook Instance`.
* Enter a name (with no spaces) for the notebook instance.
* Under `IAM Role`, choose `Create a New IAM Role` and accept the defaults, and click on `Create role`.
* Click `Create notebook instance` once more!
* This will take some time, but eventually you can click on `Open Jupyter` to get a Jupyter Notebook.

### 1.4 IBM Watson Studio

Sign up at: [https://dataplatform.cloud.ibm.com/](https://dataplatform.cloud.ibm.com/)

## 2. Setup on a Local Machine

Alternatively, you can do assignments on your local machine.  Specifics will depend somewhat on your hardware and operating system.

Our preferred option -- which will allow you to do all assignments -- is to use Docker Desktop.  This installs Jupyter and Python (and Apache Spark) within a container.  As a fallback, you may also consider installing Python 3.6 and Jupyter Notebook 6.0.1 on your local machine; you may not be able to do the Apache Spark assignments.

###  Installing Docker

Your first task will be to install Docker itself. Please see the setup instructions below, which depend on your operating system. If, during download of the installer from Docker, you have an option to choose between the “Stable” and “Beta” versions, please stick with Stable!

-   [Mac](https://docs.docker.com/docker-for-mac/).  
    
-   [Windows 10 Pro/Education or better](https://store.docker.com/editions/community/docker-ce-desktop-windows).        
    Once Docker is installed, you should see the little whale icon for Docker on your Task Bar. Right-click, then choose Settings, then “Shared Drives.” Add a check for the C Drive.        
    
-   [Windows 8/Windows 10 Home](https://www.docker.com/products/docker-toolbox). We recommend that you upgrade to Windows 10 Education or Pro if possible, as the Docker integration is much better. However, if you have Windows 8 or Windows 10 Home, you can install the “legacy” product called [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/). Before installing Docker Toolbox, check if you have [Oracle VirtualBox](https://www.virtualbox.org/) installed. If so, please update to the latest build else check the option to install virtualbox.  
      
    Once Docker is installed, run Docker Quickstart Terminal. Approve the various requests. Ultimately you should get a bash terminal.
    
-   [Linux (Ubuntu)](https://docs.docker.com/engine/installation/linux/ubuntulinux/). Install [Docker CE](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-docker-ce) according to the basic instructions.

### 1.2 Installing Jupyter on Docker

#### Initially Launching Jupyter and Sharing a Directory

Make sure that your docker program is running in system (an icon will appear in menu bar/notification area of Mac/Windows). You can start the program by clicking it in LaunchPad or Start Menu. After that, launch your operating system command-line: in Mac OS and Linux, this is “Terminal” and on Windows it’s “Command Prompt” or "PowerShell". Then type in the following two lines. In this document, we’ll use userid to refer to your user login ID on your local machine.  

For Windows 10 Pro/Education (where the environment variable `%USERPROFILE%` is by default set to `\Users\{userid}`), you can open Command Prompt or PowerShell and run:
```
mkdir %USERPROFILE%\Jupyter
echo "Test" > %USERPROFILE%\Jupyter\test.txt
docker run -v %USERPROFILE%\Jupyter:/home/jovyan/work -it -p 8888:8888 jupyter/all-spark-notebook
```
For Windows 10 Home you’ll need to first open the Command Prompt and run:
```
mkdir %USERPROFILE%\Jupyter
vboxmanage sharedfolder add default --name "%USERPROFILE%\Jupyter" --hostpath "%USERPROFILE%\Jupyter" --automount` 
echo "Test" > %USERPROFILE%\Jupyter\test.txt
docker run -v %USERPROFILE%\Jupyter:/home/jovyan/work -it -p 8888:8888 jupyter/all-spark-notebook
```

For Mac/Linux, or Windows 10 Home under **Docker Quickstart Terminal** (where the environment variable `$HOME` is by default set to `/Users/{userid}`):
```
mkdir ~/Jupyter
echo "Test" > $HOME/Jupyter/test.txt
docker run -v $HOME/Jupyter:/home/jovyan/work -it -p 8888:8888 jupyter/all-spark-notebook
```

These commands will (1) create a directory for your Jupyter environment and files in `/Users/{userid}`, (2) download and install a Docker image containing Python and Jupyter Notebook as well as a local version of Spark. (If you want to dive deeply into the Docker-Jupyter environment, you can get details [here](https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook).) For Linux, you may need to add the parameter `--net=host` to the command line.

Once Docker says it is ready, it should give a message like:

 ```
To access the notebook, open this file in a browser:
file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html

Or copy and paste one of these URLs:  
http://c87c45da4bfe:8888/?token=eb1cc446...  
or http://127.0.0.1:8888/?token=eb1cc446...
```
  
Select the URL (starting with `http://`) and copy it. Open up your Web browser and paste it into the URL bar. You should see a screen like the one below. Click on the “work” directory.  

![](https://lh3.googleusercontent.com/XD2TRvpLM4I5kDzBYn_4QMbunfkw6_QpFDFzzBqgek81LcOtLOQt6oodpXq0yQSNbSf6sQAudAOQwR8G1Z4nwi2KyLcGb6CXciqdk3_qYq_ECBN6RTNdJd7M4SNDgW-3EgnqS0xR)


Verify that `test.txt` exists. This file was created in your $HOME/Jupyter directory on your host machine, and it needs to be there to confirm that your Jupyter instance can share files with the host.  Otherwise, everything will still work -- but all of your files will only be accessible from within your Docker container, not from your computer.
  

![](https://lh4.googleusercontent.com/U9coRJNuhCHroeFB_PY0TqXSIKFNQq2BDhygvnY9uQCt2LoXOenBZ3otc0FUIQRY9OrKMWekkRdq_mpGSvQobxqFZ7xcn4ZiR2MYC7tbtRt6cXrHqmessDgOJ7_SNNsJyJikzy8o)

#### If You Need a Password or Token

Follow the instructions as above.

#### If It Didn’t Work

Check the URL you were given. If it says something like `http://(eabacdef or 127.0.0.1):8888/…` replace the item in the parentheses with `127.0.0.1` or `localhost`.

If you are on Windows 10 Home or otherwise using Docker Toolbox, you may need to replace `127.0.0.1:8888` with `192.168.99.100:8888`. If that still doesn’t work, `docker machine ip` default might tell you a different address to use.

#### Installing Kitematic (only do this once)
The first time, go to the Docker “whale” icon in your menu bar (Mac) or toolbar (Windows) and choose “Kitematic”:  ![](https://lh4.googleusercontent.com/3n6rFewuVNznqSnM5nZMA8HsbAHvYVSxK6o78_VlcT4JN1TA5DkZa5quOKzXlJKGfUipE_Zp8yYkWiVb8W8gOnpb3tcMJQAbPsqL4ZX0)

When the dialog box pops up, click on the link that says “You can download it here.”

-   Mac: Extract Kitematic to "Applications"
-   Windows 10 Home: You need to do this from the start menu. If Kitematic complains about an ENOENT error, click on “Use Virtualbox.”
-   Windows 10 Pro or Education: Extract the folder to  `C:\\Program Files\Docker\Kitematic`

**You can skip the registration with Docker Hub, since you won’t be publishing any containers.**

### 1.3 Connecting to Jupyter after a Reboot

At times you’ll need to stop your Docker instance, e.g., after rebooting. If you reboot and repeat the steps in Section 1.2, you’ll end up creating another container with Jupyter, which can be very wasteful. Instead you can relaunch and reconnect to your existing container via Kitematic. Before using Kitematic, you should check that your docker program is running. Then: 

Mac OS X: Run Kitematic. (click the whale icon and select Kitematic in the options, or start Kitematic in launchpad) You can skip the registration with Docker Hub. 

Windows 10: Run Kitematic.

-   On Windows 10 Home you will need to do this via the Start Menu.
    
-   On Windows 10 Pro or Education, there is a “whale” icon in the Task Bar that will let you access Kitematic.  
      
    

If Kitematic complains about an ENOENT error, click on “Use Virtualbox.” You can skip the registration with Docker Hub, since you won’t be publishing any containers.

  

1.  Once you are at the main page, look on the left side, where you’ll see a list of containers on your machine, e.g.,: ![](https://lh4.googleusercontent.com/VfTFrF_jCVA5KH42E0Kzrnz3qu_OHlXlJ7ODcGH89g6UcN_tY16otg9bEq3H5zVoZAN6TxXNqlWpfpKU7KFDa50q1jB9txRMdmGjKc4tqcVNb__nJOlZnQ9_uDG10PqPvnMXoGRj)
    

  

2. Click on the container and click on the Start button. This will start your Jupyter Notebook.

![](https://lh3.googleusercontent.com/OCrERPuaGEujoRholZ2rOb4_tGYB2Z48qLw3XXF5FDxjjFKrELusRsleEH5ZycnI7Kx_wW4L2dxvTa8ZcLyBZAEXkXYG7m8c9DfPwcY41Vfcus8jdbJ482oureg0zhlnhS-LWJbY)

  

Inside the log window you will eventually see something like:

  
```
Copy/paste this URL into your browser when you connect for the first time,

to login with a token:

[http://localhost:8888/?token=9ed4c2dad760cbde0215a0ee7784adf1d416c1ff4d9068eb](http://localhost:8888/?token=9ed4c2dad760cbde0215a0ee7784adf1d416c1ff4d9068eb)
```
  

Click on the Web Preview icon on the right to launch it on a browser. If you don't see the Web Preview, you may also try to visit the IP address directly in your browser, as mentioned in the previous section. If you see a screen like the one below, then you are ready to go, and you can skip to the “Your Data” section below! If not, you should follow the instructions below.

  

![](https://lh6.googleusercontent.com/xL7-s9By6PNu1Go7ypFWnAWR1M_La98nlt1_p_uX8D4MAHRq3Xe6ryNDOl_a0EpGvSdLOlwnvC9rTyGdL8G8XxTkJl_BvzJMoYIaow74uNXflfeQxaS4B9_O1cCd526id7EVDJeN)

#### If You Need a Password or Token

If, instead, you see something like:

![](https://lh5.googleusercontent.com/pt6i4scEuGtu0UjWI24EEskzcby_eamMrz1opTpUlFTnwxKoqyNtBpTaHS7_Sj9wiTokTxrQ4K7KjGW_mjmufb57IYoFdteCqnJ4SmB5jEh5OmdNV5g5rRzu5QE9THmWeEGu1DMC)

  

Use the token value generated in the Kitematic container terminal.

eg: [http://localhost:8888/?token=9ed4c2dad760cbde0215a0ee7784adf1d416c1ff4d9068eb](http://localhost:8888/?token=9ed4c2dad760cbde0215a0ee7784adf1d416c1ff4d9068eb)

#### Your Notebooks and Data

Please consistently work in the “work” directory in Jupyter -- this corresponds to the Jupyter directory on your host machine. Your files should be saved there, and you’ll be able to back up and retrieve them even if Docker crashes.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgwMzgwMDM1Myw1NTM3MDkwMTksMTIxND
A1MjQ2NV19
-->