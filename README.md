# Personal Page

个人主页项目，用于承载 AI 评测、Agent 产品、数据科学背景、作品集和文章。

## Files

- `index.html`: 个人主页页面
- `articles/`: 大模型科普系列落地页和文章页
- `site.css`: 页面样式
- `assets/images/`: 首页视觉素材
- `assets/images/profile-professional.jpg`: 首页职业照

## Preview

直接在浏览器打开 `index.html` 即可预览。后续可以部署到 GitHub Pages、Vercel 或绑定个人域名。

也可以在项目目录启动本地静态服务器：

```bash
python3 -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000/
```

## Deploy to GitHub Pages

1. 在 GitHub 新建一个仓库，例如 `personal-page`。
2. 将本地项目推送到仓库：

```bash
git remote add origin <your-repo-url>
git push -u origin main
```

3. 在 GitHub 仓库中打开 `Settings` -> `Pages`。
4. `Build and deployment` 选择 `Deploy from a branch`。
5. Branch 选择 `main`，目录选择 `/root`，保存。
