#!/bin/bash
touch ~/.local/bin/surchin 
echo '#!/bin/bash
search_query="$@"
cd ~/surchin/
ddgs text -k "$search_query" -o json
python ~/surchin/redirect.py
lynx ~/surchin/output.html
find ~/surchin/ -type f -regex '.*text_[^.]*\.json' -exec rm {} \;
' > ~/.local/bin/surchin
chmod +x ~/.local/bin/surchin
