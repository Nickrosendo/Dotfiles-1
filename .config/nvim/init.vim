set undodir=$XDG_DATA_HOME/vim/undo
syntax on
set nocompatible
set noerrorbells                         " no error bells
set shiftwidth=4
set nohlsearch
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir              " set a undo directory 
set undofile
set incsearch
set number relativenumber               " sets relative line number
set nu rnu
set cursorline                          " highliht current line
set cmdheight=1
set ignorecase                          " ignore case while searching
set laststatus=2                        " always show status line
set termguicolors                       " true colors
set clipboard=unnamedplus              " set clipboard to system clipboard
set path+=**                            " ** for recursive search on all dir
set wildmenu
filetype plugin indent on
filetype plugin on
set ttyfast                             "for faster scrolling
set lazyredraw                          "faster scrolling

let g:currentmode={
       \ 'n'  : 'NORMAL ',
       \ 'v'  : 'VISUAL ',
       \ 'V'  : 'V·Line ',
       \ '' : 'V·Block ',
       \ 'i'  : 'INSERT ',
       \ 'R'  : 'R ',
       \ 'Rv' : 'V·Replace ',
       \ 'c'  : 'Command ',
       \}
" so $VIMRUNTIME/syntax/hitest.vim for colors name
" status line
"set statusline=
"set statusline+=%#DraculaTodo#
"set statusline+=\ %{toupper(g:currentmode[mode()])}
"set statusline+=%{&modified?'[+]':''}
"set statusline+=%r
"set statusline+=%y
"set statusline+=%r
"set statusline+=\ %F
"set statusline+=\ %=                     "rightside
"set statusline+=%#DraculaSearch#
"set statusline+=\ %c:%l/%L
"set statusline+=\ %p%%
"set statusline+=\ [%n]

function! GitBranch()
  return system("git rev-parse --abbrev-ref HEAD 2>/dev/null | tr -d '\n'")
endfunction

function! StatuslineGit()
  let l:branchname = GitBranch()
  return strlen(l:branchname) > 0?'  '.l:branchname.' ':''
endfunction

set statusline=
set statusline+=%#DraculaSearch#
set statusline+=%{StatuslineGit()}

set statusline+=%#DraculaTodo#
set statusline+=\ 
set statusline+=%{toupper(g:currentmode[mode()])}

set statusline+=%#WildMenu#
set statusline+=\ 
set statusline+=\ %F
set statusline+=\ 
set statusline+=\ 

set statusline+=%#StatusLineTerm#
set statusline+=%=

set statusline+=%#DraculaSearch#
" filetype
set statusline+=%y
" line info
set statusline+=\ %c:%l/%L
set statusline+=\ %p%%
set statusline+=\ [%n]
"set statusline+=\ %{&fileencoding?&fileencoding:&encoding}
"set statusline+=\[%{&fileformat}\]
"set statusline+=\ %p%%
"set statusline+=\ %l:%c
"set statusline+=\

source $HOME/.config/nvim/plug-config/coc.vim
" plugins
call plug#begin('~/.vim/plugged')
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'ap/vim-css-color'
Plug 'vifm/vifm.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'valloric/youcompleteme'
call plug#end()

" color scheme
colorscheme dracula
hi Normal guibg=none
hi Normal ctermbg=none

"netrw
let g:loaded_netrw       = 1
let g:loaded_netrwPlugin = 1


" vifm
let g:vifm_replace_netrw = 1
let g:vifm_replace_netrw_cmd = "Vifm"
let g:vifm_embed_term = 1
"let g:vifm_embed_split = 1



" leader
nnoremap <SPACE> <Nop>
let mapleader=" "

" " Copy to clipboard
vnoremap  <leader>y  "+y
nnoremap  <leader>Y  "+yg_
nnoremap  <leader>y  "+y
nnoremap  <leader>yy  "+yy

" netew
let g:netrw_banner = 0
let g:netrw_winsize = 20

map <leader><C-s> :source ~/.config/nvim/init.vim<CR>

" fzf
map <silent> <Leader>ff :Files<CR>
map <silent> <Leader>fg :GFiles<CR>
map <silent> <Leader>fF :Rg<CR>
map <silent> <Leader>fh :History<CR>
map <silent> <Leader>fb :Buffer<CR>
map <silent> <Leader>fl :Lines<CR>
map <silent> <Leader>fL :BLines<CR>
map <silent> <Leader>fc :Commands<CR>

" vifm
map <silent> <Leader>ve :EditVifm<CR>
map <silent> <Leader>vv :VsplitVifm<CR>
map <silent> <Leader>vh :SplitVifm<CR>
