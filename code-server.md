# Using Coder code server

Install

    curl -fsSL https://code-server.dev/install.sh | sh

Run

    code-server

By default, code-server will be serve with `127.0.0.1:8080`, to connect we need port forwarding

    ssh -L 8080:127.0.0.1:8080 root@192.168.0.x

To expose web to local network

    code-server --bind-addr 0.0.0.0:8080

**NOTE**: When using VSCode's `Remote Development` to connect ssh. Need to override as bellow

    VSCODE_IPC_HOOK_CLI= code-server

# Using VSCode 

## Option 1
Run bellow command in server

    code serve-web --host=0.0.0.0 --port=8080 --without-connection-token

Then we can access VSCode by browser `<server local ip>:8080` 

## Option 2

Run bellow command

    code tunnel

This command will createa a tunnel that's accessible on `vscode.dev` from anywhere

## Option 3

Install `Remote Development` extension package in Client' VSCode
Connect to server by `ssh`. VSCode will then automatically setup VSCode server.
Navigate to project folder and run `code .`

## Ref
- https://coder.com/docs/code-server/install
- https://code.visualstudio.com/docs/remote/vscode-server
- https://code.visualstudio.com/docs/remote/tunnels