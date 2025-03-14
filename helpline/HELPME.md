# Troubleshooting Guide of the Machines

### A history.
In the beginning, there was nothing. Humans walked around in desolate plains in a thick summer fog. Then out of the darkness, a beacon of truth and light appeared. StackOverflow and Google. But that wasn't good enough so a saviour was sent. That saviour was called ChatGPT. But it turns out that the saviour sometimes spouts bullshit that seems to make sense, so the CATALOGUE had to be made to record what made sense and what did not.

This is that catalogue,

specifically for the purpose of fixing machines

which is really all a programmer does.

Fixing machines. "please fix my toaster, you have a degree in CS." ISN'T as far-fetched as you would think.

# 1. Bluetooth pairing.
ref. https://chat.openai.com/c/7a192499-72cf-466c-a9cf-dc31c554cfb0

```
#!/bin/bash

sudo systemctl restart bluetooth
bluetoothctl

And THEN In the bluetoothctl context:
power on
agent on
defalt-agent
scan on
pair <MAC_ADDRESS>
remove <MAC_ADDRESS>

```

2. NPM Problems
https://askubuntu.com/questions/1152570/npm-cant-find-module-semver-error-in-ubuntu-19-04 



# 2. The Grand Python Problem

``` pip3 freeze | xargs pip3 uninstall -y ```

