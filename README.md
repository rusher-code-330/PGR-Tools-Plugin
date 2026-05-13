<p align="center">
  <img src="https://api.websim.com/blobs/019e188f-2e56-75ee-ae6d-286fa8372ba0.png" width="800">
</p>

![Version](https://img.shields.io/badge/PGR-Plugin-yellow?style=for-the-badge&logo=tag)
[![Python](https://img.shields.io/badge/python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Repo](https://img.shields.io/badge/repo-PGRTOOLS-181717?style=for-the-badge&logo=github)](https://github.com/rusher-code-330/pgr-tools)
[![Developer](https://img.shields.io/badge/developer-Rusher-ff4d4d?style=for-the-badge&logo=github)](https://github.com/rusher-code-330)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-8.1.1-007808?style=for-the-badge&logo=ffmpeg)](https://ffmpeg.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-ff0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)

---


# PGR Tools Plugin

### add?

Please submit a pull request to ask for your plugin to be added to PGR Tools
I’ll take a look to check that everything is in order

---

This is where you can request to publish your plugin for PGR Tools

---

To help you build your plugin, take a look at the Timer plugin as an example

---

Each plugin must contain 

```python
REQUIRES = ["{python module}"]
```

It must also contain 

```python
def run():
```

Each PGR Tools plugin must contain `| ` for each print statement and `|{txt} > ` for input and output
```python
example = int(input("| time ?. . . > "))
```

```python
example = input("| exemple > ")
```

```python
print("|hello")
```
Further details will be available on the future documentation page
 
