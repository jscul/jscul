<!--
test.js
test2.js
-->

# [Python 3.6](https://github.com/jscul/common.py/edit/master/README.md)

[Test File](#example-file)

### Common and useful Python modules.

The following project was set up as a directory for common code modules that I use regularly. It is not meant as an import but rather as a source code from which you can copy/paste different **functions**/**classes**/**etc**. The code is based on *Python3.6*.

## Environment

### Virtual Environment Setup [🐍](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- You need to install *virutalenv*:

```shell
python3 -m pip install --user virtualenv && \
        sudo apt-get install python3-venv && \
        python3 -m venv _env && \
        . _env/bin/activate
```

- **Then** set your [VSCode Python environment](https://code.visualstudio.com/docs/python/environments) to your virtual environment.
    
### Development Setup
- Run `pip install pytest==5.0.1 black` to install the VSCode test environment and Python formatter.
- VSCode has some issues with the latest version of `pytest`, instead use version 5.0.1: `pip install --force-reinstall pytest==5.0.1`.

### Install Dependencies 📚
- All dependencies for all files can be found in *./requirements.txt*.
- To install dependencies run `pip install -r requirements.txt`.

### Uninstall Dependencies 🗑️
- To remove dependencies you can delete the environment: `rm -r _env`.
- If in global scope you may have to run: `pip freeze | xargs pip uninstall -y`.

### Example File

```python
import random

num = random.randomint(0, 1000000)
print(f"Hello alternate reality {num}!")
```

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

[Back to top](#Python-3-6)
