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
