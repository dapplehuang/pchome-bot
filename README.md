# PCHOME-BOT

## Installation

1. Find the brower's version.
   - setting -> about Chrome

<img src="https://i.imgur.com/O5YRSuc.png" style="zoom:25%;" />

2. Download the [Chrome Driver](https://chromedriver.chromium.org/downloads)

3. Unzip the file and put chromedriver under `/usr/local/bin ` (mac / linux)

   ```bash
   mv chromedriver /usr/local/bin
   ```

4. Install selenium

```bash
pip3 install selenium --no-cache --user
```



## Usage

1. Set the variables in `pchome.py`.

```python
PRODUT_WEBSITE = ''
PCHOME_ACCOUNT = '@gmail.com'
PCHOME_PASSWORD= ''
```

2. Run the script

```bash
python3 pchome.py
```

