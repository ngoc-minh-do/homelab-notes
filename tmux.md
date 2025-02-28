# tmux

New session:
```sh
tmux
# or
tmux new -s <session-name>
```

Detach from current session

        Ctrol + B, then D

List session
```sh
tmux ls
```

Attach to session
```sh
# attach to recent session
tmux a
# attach to a specific session
tmux a -t <target-session>
```

Kill a session
```sh
tmux kill-session -t <target-session>
```