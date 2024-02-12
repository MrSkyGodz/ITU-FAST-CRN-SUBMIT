# crn_submit
Just add it to Chrome as a bookmark.

# fast_submit_api
python3 post requests
## run
`python3 fast_submit_api.py`
## requirements
`pip3 install -r requirements.txt`

## preparation
- Sign in `https://kepler-beta.itu.edu.tr/`.
- Press Fn + F12 and press Network.
- Refresh the page.
- Find `KisiselBilgiler` or etc. and click on it.
- In the `Header` section inside the `Request Header` find `Authorization:`.
- Copy all Authorization it is like `Bearer xxxx`.
- Paste into Python code variable named `auth_key`.
- Fill your crn's and run the code.
