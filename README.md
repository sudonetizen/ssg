# ssg
Static Site Generator
- This Static Site Generator converts Markdown file to HTML files.
- Nested format is not included (**__italic and bold__**)
- Blocks must be seprated by one blank line
- Markdown files (source) at content folder 
- HTML files (destination) at docs folder

Run local:
```shell
./main.sh
```

Run via github pages
- change and update markdown files on content folder based on your need, current markdown files are about LOTR
- change and update static folder where currently images are saved for markdown files and css stylesheet  
- create github repo and replace "/ssg/" on build.sh with your repo name
- run build.sh 
- go to your repo's settings and select pages section
- set source to main branch and docs directory
- save settings
- push your local repo to github repo
- open live URL https://username.github.io/repo_name/

