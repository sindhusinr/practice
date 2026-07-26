## Git Commands
```bash
git clone <repo>
git add .
git commit -m "Added new code"
git push -u origin main 
```

## Check Remote Repository

```bash
git remote -v
git branch
```
To add remote repository
```bash
git remote add origin <repo>
```

Remove the old remote repository:
```bash
git remote remove origin
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
