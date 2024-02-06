# Surchin
Surchin is a simple script which works to redirect sites found with duckduckgo for lynx.

## Table of Contents
- [Description](https://github.com/ks-nunes/surchin#Description)
- [Requirements](https://github.com/ks-nunes/surchin#Requirements)
- [Installation](https://github.com/ks-nunes/surchin#Installation)
	- [Script](https://github.com/ks-nunes/surchin#Script)
	- [Manual Install](https://github.com/ks-nunes/surchin#Manual)
- [Redirector](https://github.com/ks-nunes/surchin#Redirector)
- [Usage](https://github.com/ks-nunes/surchin#Usage)
## Description
To my knowledge lynx doesn't have extensions and I wanted to use privacy respecting frontends. So this was born, it functions as an intermediary between my chosen search engine(duckduckgo) and lynx, being a sort of pseudo browser extension. The name is a play on searching and sea urchins. 
## Requirements 
- Python (3.11)
- Redirector.json file in ~/surchin
## Install
### Script
```
pip install duckduckgo_search
git clone https://github.com/ks-nunes/surchin ~/surchin
chmod +x ~/surchin/setup.sh
sudo ./setup.sh
```
### Manual
```
pip install duckduckgo_search
git clone https://github.com/ks-nunes/surchin ~/surchin
```
Create a file in a $PATH of your choosing.
```
sudo nvim /path/to/your/chosen/path/surchin
```
Populate it with the following.
```
#!/bin/bash
cd ~/surchin/
search_query="$@"
ddgs text -k "$search_query" -o json
python ~/surchin/redirect.py
lynx ~/surchin/output.html 
find ~/surchin/ -type f -regex '.*text_[^.]*\.json' -exec rm {} \;
```
Give it executable permissions.
```
chmod +x /path/to/your/chosen/path/surchin
```
## Redirector
The Redirector.json file is the one where you define what sites you want to redirect and where to. it is empty by default.The script was made to be compatible with Redirector extension by [einaregilsson](https://github.com/einaregilsson/Redirector,). This means if you're already using it, then you can just export your settings and save the file to the ~/surchin directory.  If not you can make your own File and add arguments to it manually. 

The only arguments the script looks at are these three, the rest is ignored. 
```
[
	{
		"includePattern": "https://www.youtube.com/*",
		"redirectUrl": "https://farside.link/invidious/$1",
		"disabled": false,
    }
]
```
This is an example of what a single entry export from Redirector looks like, you don't need to change anything, but the script only needs the above parameters to work
```
[
        {
            "description": "Youtube/Invidious",
            "exampleUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "exampleResult": "https://yewtu.be/watch?v=dQw4w9WgXcQ",
            "error": null,
            "includePattern": "https://www.youtube.com/*",
            "excludePattern": "",
            "patternDesc": "",
            "redirectUrl": "https://yewtu.be/$1",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": false,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        }
]
```

## Usage
```
surchin [SEARCH QUERY]
```

