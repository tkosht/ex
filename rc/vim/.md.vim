" vimrc for markdown
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'

Plugin 'kannokanno/previm'
Plugin 'tyru/open-browser.vim'

let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_folding_style_pythonic = 1
let g:vim_markdown_math = 1

"Plugin 'syui/cscroll.vim'
"Plugin 'kana/vim-submode'

nnoremap <silent> <F7> :PrevimOpen<CR>
