# pycs
SOHU CDN Utils

### Get started

* Edit keys in `keys.py`
```
vi keys/keys.py
```
* Usage
```
python flushcdn.py [space_name] [uri]
```
* Example: Flush a image
```
python flushcdn.py shangpin /f/p/10/12/01/20101201180611437824-0-0.jpg
```
* Example: Flush multi uri
```
for i in $(cat uris.txt); do python flushcdn.py shangpin $i; done
```