# Webshell-Hunter

# Synopsis
This tool was create in order to help find both historical and ongoing webshells. Currently it will only look work with apache error logs
See https://github.com/NathanCoats/Webshell-Hunter/wiki for the roadmap.

# Requirements
- Python 3+
- Python Pip

# Installation
- ``` mkdir -p ~/sandbox/code ```
- ``` cd ~/sandbox/code ```
- ``` git clone https://github.com/NathanCoats/Webshell-Hunter.git ```
- ``` Webshell-Hunter ```
- ``` sudo apt install python3 ```
- ``` sudo apt install python3-pip ```
- ``` pip3 install -r requirements.txt ```

# Usage
- ``` zgrep {SEARCH_PHRASE} {Apache Log File(s)} | ~/sandbox/code/Webshell-Hunter/start-hunt.py ```


# References

