# DjanKo

Django endpoint for your Ko-Fi webhooks.
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P8H27N3)

## Running the repl
0. Create a new repl using this template: [https://replit.com/github/septn/djanko](https://replit.com/github/septn/djanko) or if you wish to deploy on Railway, make sure you put this on your start command
   ```
   python manage.py migrate && python manage.py runserver 0.0.0.0:8000
   ```
1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Set up another secret environment variable where the key is `KOFI_VERIFICATION_TOKEN` and the value is your Ko-Fi
   verification token. You can get this value [here](https://ko-fi.com/manage/webhooks?src=sidemenu).
3. Change `Webhook URL` on that same page into the URL where you host this django instance. ie: `https://djanko.MyREPL.repl.co/kofi/webhook/`
4. Migrate your database using `python manage.py migrate` command.
5. Start by sending some hooks, and check it on admin page.
## Sample Usage

Once you get some hooks logged from Ko-Fi, you can then grab by sending a GET request to this url:

```
https://djanko.MyREPL.repl.co/kofi/supporters/ 
```
```
https://djanko.MyREPL.repl.co/kofi/supporter/10/ 
```
