# ZSH and Oh My Zsh Setup

## Zsh

Install `zsh` on Debian
```
sudo apt install zsh
```
Confirm Installation:
```
zsh --version
cat /etc/shells
```
Set `zsh` as Default Shell for current user or specific user:
```
chsh -s $(which zsh) <optional:username>
```
Verify the Default Shell:
```
echo $SHELL
```
Rollback to Bash (if needed):
```
chsh -s /bin/bash <optional:username>
```
## Oh My Zsh
Install for current user
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
### Plugins

zsh-autosuggestions
```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```
zsh-syntax-highlighting
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Add the plugin to the list of plugins for Oh My Zsh to load (inside ~/.zshrc):
```
plugins=( 
	# other plugins...
	zsh-autosuggestions
	zsh-syntax-highlighting
)
```