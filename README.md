Technologies:
    * SQLite
    * Python

Python Libs:
    * bottle
    * pony.orm


How to use:
Ensure you have " python3 " installed on your system and execute the following commands to deploy database with relathionships and populate data on Vouchers table.

- $git clone {project.git}
- $cd project
- $Make deps # Install dependencies
- $Make populate # Populate Vouchers
- $Make start # Start application

* Disruptive database release: Only for Linux
- Make releasedb