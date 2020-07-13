# Ovirt Console
Ovirt Console parses a console.vv file and partially automates connecting to Ovirt virtual machines with VNC enabled.

Ovirt Console was developed because of the inability for popular VNC viewer applications to read the *console.vv* file associated with remotely accessible virtual machines running in Ovirt. The program automates running the installed VNC viewer and displaying the associated password.

## Prerequisites for Ovirt Console
Ovirt Console requires:
- Python 3
- A VNC viewer such as [RealVNC](https://www.realvnc.com/en/) or [TigerVNC](https://tigervnc.org/)

## How to Setup Ovirt Console
- Clone this repository as `git clone https://github.com/jasonmpittman/ovirt-console`

## How to Use Ovirt Console
1. Click on the *console* option your Ovirt instance.
2. Download and save the console.vv file.
  - **Important**: save the file in the ovirt-console repo directory
3. From a shell / terminal, execute Ovirt Console as `python3 ovirt-console`
  - Two things will happen. First, the VNC viewer will be executed. Second, the Ovirt set password will be displayed in the shell / terminal.
4. Copy the password from the shell and paste into the VNC viewer application. 
5. Click *connect* or press Enter.

## Testing
Ovirt Console has been tested using Python 3.6.9 on Ubuntu 18.04.4 LTS and the same running as Windows Subsystem for Linux.