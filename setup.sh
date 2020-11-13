#!/usr/bin/bash
printf "#!/bin/bash\n$PWD/bin/python $PWD/mkhost.py" > bin/mkhost
chmod +x bin/mkhost

ln -s "$PWD/bin/mkhost" /usr/local/bin/mkhost