# Push without Password
### on Linux
- Just
```shell
echo https://{username}:{password}@github.com > ~/.git-credentials
git config --global credential.helper store
```
- And you will see `[credential]helper = store` in `.gitconfig`

### on Windows
Just install `Git-Credential-Manager-for-Windows` or `GCMW` for short
