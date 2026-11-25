# Open source developer tools

Open-source code editors, self-hosted Git forges, API clients, and SQL workspaces let engineering teams avoid vendor lock-in and keep proprietary source code and API collections inside their own network.

[Back to main catalog](../README.md)

## Comparison table

<!-- START:CATEGORY_TABLE -->
| Software | Alternative to | Platform | License | Stars | Last release | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [VSCodium](https://vscodium.com/) | Visual Studio Code | Win, Mac, Linux | MIT | 34.3k | 2026-10-28 | Active | Low | VS Code binary builds without Microsoft telemetry |
| [Eclipse IDE](https://www.eclipse.org/) | IntelliJ IDEA | Win, Mac, Linux | EPL-2.0 | 173 | 2026-11-25 | Active | Medium | Enterprise Java, C/C++, and embedded development |
| [Neovim](https://neovim.io/) | Sublime Text, VS Code | Win, Mac, Linux | Apache-2.0 | 103.9k | 2026-10-09 | Active | High | Keyboard-driven terminal editor with Lua plugins and LSP |
| [Zed](https://zed.dev/) | VS Code, Sublime Text | Mac, Linux, Win | GPL-3.0 / Apache-2.0 * | 95.7k | 2026-11-20 | Active | Low | GPU-accelerated code editing written in Rust |
| [GitLab CE](https://about.gitlab.com/) | GitHub Enterprise, Bitbucket | Web | MIT (Community Edition) * | - | - | Active | Medium | All-in-one self-hosted Git, CI/CD, and container registry |
| [Gitea](https://about.gitea.com/) | GitHub, Bitbucket | Web | MIT * | 59.3k | 2026-11-15 | Active | Low | Lightweight Go-based Git forge with built-in Actions |
| [Forgejo](https://forgejo.org/) | GitHub, GitLab | Web | GPL-3.0 | - | - | Active | Low | Community-governed self-hosted Git forge forked from Gitea |
| [Bruno](https://www.usebruno.com/) | Postman, Insomnia | Win, Mac, Linux | MIT * | 48.6k | 2026-11-24 | Active | Low | Offline-first API client storing collections in Git |
| [Hoppscotch](https://hoppscotch.io/) | Postman | Web, Win, Mac, Linux | MIT * | 81.0k | 2026-11-23 | Active | Low | Fast browser and desktop REST, GraphQL, and WebSocket testing |
| [DBeaver Community](https://dbeaver.io/) | DataGrip, Navicat | Win, Mac, Linux | Apache-2.0 (Community) * | 52.5k | 2026-11-24 | Active | Low | Universal SQL client supporting dozens of database engines |
<!-- END:CATEGORY_TABLE -->

## Practical trade-offs

- VSCodium removes Microsoft telemetry from VS Code while keeping Open VSX extension support. Zed focuses on low-latency editing in Rust, Neovim fits terminal-first workflows, and Eclipse remains standard for large Java and embedded codebases.
- GitLab CE bundles CI/CD, issue tracking, and container registries in one stack, though it requires more RAM than Gitea or Forgejo. Pick Forgejo if community governance and GPL licensing matter to your organization.
- Bruno saves API requests as plain text files inside your Git repository, avoiding cloud sync requirements. Hoppscotch works well when teams prefer a browser interface.
- DBeaver Community connects to PostgreSQL, MySQL, SQLite, ClickHouse, and dozens of other engines through JDBC drivers.
