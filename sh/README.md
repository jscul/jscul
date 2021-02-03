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
4) https://averagelinuxuser.com/ubuntu_custom_launcher_dock/

### Tutorials

1) Docker: https://www.youtube.com/watch?v=fqMOX6JJhGo
2) Vim: https://www.youtube.com/watch?v=wlR5gYd6um0

### ffmpeg

1) Create video from set of images: https://stackoverflow.com/a/37478183

### Blender

- https://docs.blender.org/manual/en/latest/compositing/types/output/file.html

### Aseprite

### Unity

- https://docs.microsoft.com/en-us/dotnet/core/install/linux
- https://www.mono-project.com/download/stable/

- https://www.youtube.com/watch?v=tW744Zgc1YY&ab_channel=Sykoo
- https://answers.unity.com/questions/691438/how-do-i-create-a-sprite-sheet-for-a-2d-character.html#:~:text=Select%20the%20image%20in%20the,options%20lower%20in%20the%20Inspector

- https://breadcrumbsinteractive.com/two-unity-tricks-isometric-games/
- https://www.youtube.com/watch?v=CTf0WjhfBx8&frags=wn&ab_channel=CodeMonkey
- https://www.youtube.com/watch?v=kJ4Ovd5HaMc&ab_channel=DevDuck
- https://docs.unity3d.com/2017.4/Documentation/Manual/SpritePhysicsShapeEditor.html
