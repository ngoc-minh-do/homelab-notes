# Code Server

## Using Coder code server

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

## Using VSCode 

### Install VSCode on Server

Ref:
- https://code.visualstudio.com/docs/setup/linux

### Option 1: Access VSCode by browser locally
Run bellow command in server

    code serve-web --host=0.0.0.0 --port=8080 --without-connection-token

Then we can access VSCode by browser `<server local ip>:8080` 

### Option 2: Access VSCode by VS Code client locally

Install `Remote Development` extension package in Client' VSCode
Connect to server by `ssh`. VSCode will then automatically setup VSCode server.
Navigate to project folder and run `code .`

### Option 3: Access VSCode by browser or VSCode client from anywhere using VSCode Tunnel

Run bellow command

    code tunnel

You will be prompted to signin via Github to register device with code.

Then you can access from anywhere using:
1. Browser by `https://vscode.dev`
2. VSCode client
   - Install `Remote Tunnels` extension
   - Login with same Github account
   - Then, the computer name will show up and ready to be connected

#### Run as a service
To ensure that your tunnel is always running and does not terminate after the non-root user disconnects from the virtual machine, run the following commands:

    code tunnel service install

**NOTE**: If above command failed with error `Error creating dbus session`. You might have to set `UsePAM yes` in `sshd` config to install it.

To ensure the service stays running after you disconnect.

    sudo loginctl enable-linger $USER

**NOTE**: Above command will allows processes for a user to continue running after their session ends/ users who are not logged in to run long-running services.

For more information, check `code tunnel service --help`

You can use `code tunnel service log` to monitor it, and `code tunnel service uninstall` to remove it.

Check service status

    systemctl --user status code-tunnel

### Ref
- https://coder.com/docs/code-server/install
- https://code.visualstudio.com/docs/remote/vscode-server
- https://code.visualstudio.com/docs/remote/tunnels