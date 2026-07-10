## Git Commands

- git clone <repo>
- git add .
- git commit -m "Added new code"
- git push origin main 


## Check Remote Repository

```bash
git remote -v
git branch
```

## Pull Latest Changes

```bash
git pull origin main
```

## Remove Changes

Discard all modified files:

```bash
git reset --hard HEAD
```

Remove untracked files:

```bash
git clean -fd
```
To add git ignore 
```bash
New-Item .gitignore -ItemType File
```
