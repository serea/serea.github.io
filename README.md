This is my personal github page repository. This was forked by [academic websites](https://github.com/academicpages/academicpages.github.io).


### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

## AI 使用说明 / AI Contributor Instructions

AI 修改本项目之前必须阅读 [AGENTS.md](AGENTS.md)。个人主页的中文与英文必须在同一 PR 中同步更新，论文须同步主页列表及详情。提交前运行 `python3 scripts/check_bilingual.py`；构建后运行 `python3 scripts/check_bilingual.py --site _site`。

AI contributors must follow [AGENTS.md](AGENTS.md): update both languages together and verify the source, rendered pages, and deployment.

# Instructions

1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://serea.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.
