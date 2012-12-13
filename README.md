interview_tools
===============

The goal for this repo is to have a ton of tools and algorithms ready to make online interviews a breeze.

If you are an engineer and are about to interview me, good luck!

# Tools

## Copier

The first and most important step is to find a way to copy text from a local file to a code-sharing website. This allows me to edit quickly and in my native environment, lets me do such things as write and run tests and import libraries.

Copier opens a browser, watches the directory it is run from, and whenever it sees a file is changed, copies the contents of that file to the online editor.

### Usage

```
pip install -r requirements.txt
python copier [url]
```

Then open up a new file and start editing. Note, only one file works at a time.

### Notes

At the moment, only collabedit and stypi are supported. Please check `copier.py` for the most recent list. Also note, much of the support is limited. Again, refer to the source for details.

Also, because the copier is based on [easywatch](https://github.com/Ceasar/easywatch), if you are using vim you will need to disable backup files. To do so, add the following to your `.vimrc`.

```
set nobackup " Do not make a backup before overwriting a file
set nowritebackup " Do not make a backup before overwriting a file
set noswapfile " Don't create swapfiles
```

See easywatch for more details.
