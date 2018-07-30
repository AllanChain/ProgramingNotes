# Push without Password
### on Linux
- First
```shell
cd ~
touch .git-credentials
vim .git-credentials
```
- Then type:
`https://{username}:{password}@github.com`
- Finally:
```shell
git config --global credential.helper store
```
- And you will see `[credential]helper = store` in `.gitconfig`
### on Windows
Just install `Git-Credential-Manager-for-Windows` or `GCMW` for short
