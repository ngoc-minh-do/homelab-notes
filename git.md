# git

- Install git
- Edit git's global config

      [user]
        name = ngoc
        email = username@gmail.com
      [alias]
        log2 = log --all --graph --decorate --oneline --pretty=format:\"%C(auto)%d %h %C(reset)%s %C(red)| %C(cyan)%an %C(red)| %C(green)%ad\" --date=format:'%Y-%m-%d %H:%M:%S'
      [filter "lfs"]
        clean = git-lfs clean -- %f
        smudge = git-lfs smudge -- %f
        process = git-lfs filter-process
        required = true
      [core]
        editor = code --wait
        compression = 0
      [diff]
          tool = default-difftool
      [difftool "default-difftool"]
          cmd = code --wait --diff $LOCAL $REMOTE
      [merge]
          tool = code
      [mergetool "code"]
          cmd = code --wait --merge $REMOTE $LOCAL $BASE $MERGED

- Some personal convenience zsh functions in `~/.zshrc`

      # Checkout master, pull and fetch all
      function gcmc() {
          git checkout master && git pull && git fetch --prune --all
      }

      # Delete both local and remote branch
      function gdb() {
          if [ "$1" != "" ]
          then
              git push origin ":$1" --no-verify
              git branch -D "$1"
          else
              echo "Please input branch name!!!"
          fi
      }

      # Checkout master, pull and fetch all, then Delete both local and remote branch
      function gdbc() {
          if [ "$1" != "" ]
          then
          gcmc && gdb "$1"
          else
              echo "Please input branch name!!!"
          fi
      }

      # Checkout remote branch, delete local branch if same name
      function gcrb() {
          if [ "$1" != "" ]
          then
              gcmc
              git branch -D "$1"
              git fetch --prune --all && git checkout -b "$1" origin/$1
          else
              echo "Please input branch name!!!"
          fi
      }
