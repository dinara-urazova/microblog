# Install project

To install project on a local machine run these commands:
```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ flask run --debug (same result below)
(venv) $ flask --debug --app microblog run
...работает сервер, ctrl + c для выхода
(venv) $ deactivate
```

or simply run this script:
```
$ ./install.sh
```

# Run project
```
$ ./run.sh
```

and then  open your browser.