# Trabajo Practico

### Technologies:
    - SQLite ( sqlite tools for windows )
    - Python ( Anaconda for windows systems)

### Libraries:
    - Bottle
    - Pony.ORM

# How to use:
Ensure you have " python3 " installed on your system and execute the following commands to deploy database with relathionships and populate data on Vouchers table.

anaconda for windows systems:
https://www.anaconda.com/distribution/

and sqltools for windows:
https://www.sqlitetutorial.net/download-install-sqlite/


# For linux:

# Clone Repository

```sh
$ git clone URL
```

# Project Directory
```sh 
cd <path>
``` 

# Install Deps
```sh
$ make deps
```

# Start the App
```sh
$ make start
```

# Populate Databse
```sh
$ make populate
```

# Cleanup 
```sh
$ make clean
```

# For windows:

# Clone Repository

```sh
$ git clone URL
```

# Project Directory
```sh 
cd <path>
``` 

# Install Deps ( anaconda console )
```sh
$ conda install -c conda-forge bottle
$ conda install -c conda-forge pony
```

# Start the App ( powershell console or cmd )
```sh
$ python start
```

# Populate Databse ( powershell console or cmd )
```sh
$ python populate
```

# Cleanup ( powershell console or cmd )
``` delete sqlite.db file
```

### Author: Javier E. Pereyra
