# feed-lib

This library is responsible to hold all the feed related packages and modules that can be added to the folder to makes feed processig easier.

#### This repo contains different modules, each performing one category of tasks.

1. File downloader
2. Field level helper
3. Product level helper
4. Catalog level helper

#### Files that are present in this repo, and their usage

1. pypackage.py
    - Holds all the python packages under an unified file
	
2. requirements.txt
    - This file is responsible to install all the python dependent package
    ```python
	pip install -r requirements.txt --user
	```

3. config.py
	- Contains the configurations that will be used in the `feed.py`
	- These configurations contain transformers, that inturn hold key level information 

4. fieldhelpers.py
	- This file contains isolated functions that take in the raw value from the feed and return modified value to be added to the `unbxd_product = {}`
	
5. producthelpers.py
	- Holds isolated functions that can be added based on the customer requirements and run mainly for debug purpose
	- Holds a class `productLevelHelpers` which holds both generic and customer related functions that run by triggering `__run__()` function having the list all the functions that have to be run

6. skeleton_feed.py
    - Holds the outer structure that on few modifications get customer specific.
    
#### Starting with a feed upload process

1. 