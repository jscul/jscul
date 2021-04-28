# common.sh
Common Linux modules and APIs.

```shell
pip install awsebcli --upgrade --user
```
~/.aws/config
```shell
[profile eb-cli]
aws_access_key_id = XXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXX

[profile eb-cli2]
aws_access_key_id = XXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXX
```
```bash
eb init --profile eb-cli2
```
Set environment variables for the environment (deletes PARAM4, PARAM5).
```bash
eb setenv foo=bar JDBC_CONNECTION_STRING=hello PARAM4= PARAM5=
```

### Development setup

1) VSCode: https://code.visualstudio.com/download
2) Fira code: `sudo apt install fonts-firacode`
3) Docker install: `sudo snap install docker`

### Tutorials

### ffmpeg

1) Create video from set of images: https://stackoverflow.com/a/37478183

### Blender
