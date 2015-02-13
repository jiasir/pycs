# pycs
SOHU CDN Utils

### Get started

* Define your environment with `CS_ACCESS_KEY` and `CS_SECURITY_KEY`
```
export CS_ACCESS_KEY='put your sohu cloud storage access key here'
export CS_SECURITY_KEY='put your sohu cloud storage security key here'
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