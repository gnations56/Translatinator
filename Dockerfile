FROM ubuntu
RUN apt-get update
RUN apt-get install -y software-properties-common apt-transport-https
RUN yes | apt-add-repository ppa:mozillateam/firefox-next
RUN apt-get update
RUN apt-get install -y firefox xvfb python3-pip wget
RUN pip3 install selenium discord.py
RUN cd /root && wget  https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN cd /root && tar -xzvf geckodriver-v0.26.0-linux64.tar.gz && cp /root/geckodriver /usr/bin/geckodriver
CMD (xvfb-run python3 /root/bot.py)