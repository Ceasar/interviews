interview_tools
===============

Tools to make online interviews easy.

# Tools

## Copier

The first and most important step is to find a way to copy text from a local file to a code-sharing website. This enables editing in our native environment, which means we get to use our favorite editor, we can write and run tests, and we can import modules.

Copier opens a browser and watches a file for changes, copying the contents of that file to the online editor on change.

### Usage

```
pip install -r requirements.txt
python copier [url] [file_to_copy]
```

Then open up `file_to_copy` and start editing.

### Notes

At the moment, only collabedit and stypi are supported. Please check `copier.py` for the most recent list. Support is limited for some sites. Again, refer to the source for details.

Also, because the copier is based on [easywatch](https://github.com/Ceasar/easywatch), vim-users will need to disable backup files. To do so, add the following to your `.vimrc`.

```
set nobackup " Do not make a backup before overwriting a file
set nowritebackup " Do not make a backup before overwriting a file
set noswapfile " Don't create swapfiles
```

See easywatch for more details.
