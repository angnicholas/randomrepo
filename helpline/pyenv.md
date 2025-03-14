# pyenv Installation steps
[Back](README.md)

1. ```https://github.com/pyenv/pyenv#how-it-works```
2. ```https://github.com/pyenv/pyenv-virtualenv```
3. Open a terminal and run ```pyenv install [version_number]```
4. Might need to run ```pyenv global [version_number]```

## Pyenv simply doesn't work lol

Continuously check
- if activating and deactivating gives you correct behaviour

```
pyenv virtualenv 3.11.0 hodge
pyenv activate hodge

pip3 install python-dotenv
pip3 freeze # should have
pyenv deactivate
pip3 freeze # should not have
```

If fail, then
``` pip3 freeze | xargs pip uninstall -y ```

Repeatedly check
- if the path is correct ```echo $PATH```




Now do the following


```
rm -rf ~/.pyenv

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile



git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

pyenv install 3.11.0
pyenv global 3.11.0

pyenv virtualenv-init
pyenv virtualenv testenv

pyenv activate testenv

which pip3


pyenv

```

All along check path is correct 

Okay... so what we have found out is
1. it is indeed a PATH problem. everything else works fine. 

2. the problem is with VSCODE. When I open a terminal window, the PATH gets mangled.

3. the problem is with some extension in VSCODE. because when i open vscode with no extensions it is fine.

GUYS I THINK I GOT IT
```"python.terminal.activateEnvironment": false,```
add this shit to the ```settings.json``` in the stupid vscode