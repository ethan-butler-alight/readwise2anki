# readwise2anki

## Development Prerequisites

1. Python 3.12 w/ pip
2. Pipenv

## Getting Started with Development

1. `git clone https://github.com/ethan-butler-alight/readwise2anki.git`
2. `pipenv install`
3. `pipenv shell`
4. Create a `src\readwise2anki\config.json` file with the contents

```
{
  "API_KEY": "<YOUR READWISE API KEY HERE>"
}
```

5. Create a symlink pointing `src\readwise2anki` to your Anki addons folder

6. `python runanki.py`
