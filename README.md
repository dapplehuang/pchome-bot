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
pip install selenium
```



## Usage

1. Set the variables in `pchome.py`.

```python
PRODUT_WEBSITE = ''
PCHOME_ACCOUNT = '@gmail.com'
PCHOME_PASSWORD= ''
```

2. un-comment line 74 in `pchome.py`.

```python
buy_btn.click()
```

3. Run the script

```bash
python pchome.py
```

