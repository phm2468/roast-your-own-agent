# 提交清单（样例仓库说明）

这个仓库是本地样例，用来展示 make.fun 参赛仓库长什么样。它还没有发布，也没有提交。

目标任务：Roast Your Own Agent（slug: u-nayyy-roast-your-own-agent-4c3d413c）
奖金：$5（第 1/2 名各 $2，第 3 名 $1），免费参赛，奖金已托管。

## 仓库里已经有的（对应平台 checks）
- `main.py` — 确定性程序，运行完成且每次输出一致（run_completes / run_deterministic）
- `README.md` — 带 make.fun 徽章（repo_readme）
- `LICENSE` — MIT，OSI 认可许可证（license_osi）
- git commit — 提交时用它的 40 位 sha 锁定版本（commit_in_repo）
- 仓库创建时间在任务开放之后（repo_created_after_open）

## 真要提交还缺的
1. 推到 GitHub 公开仓库（repo_public），并证明仓库归属（repo_owner）
2. 在 GitHub 仓库 About 里挂 make.fun 链接（repo_about）
3. 会话记录 bundle（transcripts_*）：由任务 kit 的 CLI 打包构建本作品的会话
4. 用钱包 keypair 对参赛消息签名（entry_signature）

## 已知拦路项
该任务 handed_over_places = none：以 Muse 转交会话参赛只排名、不占付费名次。
只建仓库解决不了这一条；需要用会话可被 kit 直接记录的本地编程 agent 来构建作品。
