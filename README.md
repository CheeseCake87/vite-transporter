# 🚚 vite-transporter

**_Transport Vite apps._**

```bash
pip install vite-transporter
```

**Currently compatible with:**

- Flask
- Quart

**Note (Flask/Quart):** When including credentials in fetch requests in the vite app.
You must visit the serve app first to set the credentials.

For example, if the serve app is running on `http://127.0.0.1:5001`, you must visit this address first.

This won't be needed in production, as it's expected that the Vite app will be served from the same domain.

## How it works

### The pyproject.toml file

The pyproject.toml file is used to store what Vite apps are available.

Adding the following to the pyproject.toml file will transfer all the Vite
apps listed in the `vite_app_dirs` list to the serving app listed in the `serve_app` key.

`pyproject.toml`:

```toml
[tool.vite_transporter]
npm_exec = "npm"
npx_exec = "npx"
serve_app = "app_flask_demo"
vite_apps = ["app_vite_demo"]
```

The compiling of the Vite apps requires the `npx` and `npm` to be
available. You can use absolute paths here.

`npm_exec` is used to run `npm install` if your Vite app does not
have the `node_modules` folder.

`npx` is used to run the Vite app build command.

`serve_app` is the app that will serve the Vite compiled files.

`vite_app_dirs` is a list of directories that contain Vite apps.

You can send over many Vite apps to the serving app, they will be
accessible within template files.

### List the Vite apps

You can see what apps can be compiled by running:

```bash
vt list
```

### Compiling the Vite apps

```bash
vt compile
```

The Vite apps are compiled into a `dist` folder, the files contained
in this folder are then moved to a folder called `vite` in the serving app.

Any js file that is compiled that contains an asset reference will
replace `assets/` with `/--vite--/{app_name}`.

This requires that all assets in the Vite app stay in the `assets` folder.

## Working with vite-transporter using Flask / Quart

vite-transporter creates a couple of Flask / Quart context processors that match the Vite apps
to a Flask / Quart template.

### The context processors

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {{ vt_head('app_vite_demo') }}
    <title>Test</title>
</head>
<body>
{{ vt_body() }}
</body>
</html>
```

```
vt_head(
    vite_app_name: str  # The name of the Vite app to load
)
```

```
vt_body(
    root_id: str = "root",  # The id of the root element
    noscript_message: str = "You need to enable JavaScript to run this app.",
)
```

### Flask Example

```python
from flask import Flask, render_template

from vite_transporter.flask import ViteTransporter


def create_app():
    app = Flask(__name__)
    ViteTransporter(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
```

### Quart Example

```python
from quart import Quart, render_template

from vite_transporter.quart import ViteTransporter


def create_app():
    app = Quart(__name__)
    ViteTransporter(app)

    @app.route("/")
    async def index():
        return await render_template("index.html")

    return app
```

### CORS

Setting:

```python
ViteTransporter(app, cors_allowed_hosts=["http://127.0.0.1:5003"])
```

This is to allow the Vite app to communicate with the app.

**Note:** It's recommended to remove this in production.

## Running the demos

We will be using a package call `pyqwe` to run commands from the pyproject file.
Installing the development requirements will install `pyqwe`:

```bash
pip install -r requirements/tests.txt
```

Use `pyqwe` to install the local version of vite-transporter:

```bash
pyqwe install
```

The `serve_app` under `tool.vite_transporter` is currently set to use the Flask demo app.

We will run this in terminal 1:

```bash
pyqwe flask
```

You should be able to visit the Flask app from the link in the terminal, and see the current Vite app.

Next, we will run the Vite app in terminal 2:

```bash
pyqwe vite
```

Visit the vite app from the link in the terminal. Change something, save, then in terminal 3 run:

```bash
vt compile
```

The Vite app will be compiled, and the files will be moved to the Flask app.
Visiting the Flask app from the link in terminal 1 should show the changes.