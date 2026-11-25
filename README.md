# Best Open Source Software (OSS)

A curated directory of the best open-source software organized by category, platform, license, commercial alternative, and migration difficulty. Every project listed here publishes its source code under an open-source license, and open-core editions are marked explicitly so you know what is free to self-host and what requires a paid tier.

<!-- START:STATS -->
Catalog size: 115 open-source projects across 16 categories (30 use an open-core model, marked with `*` in the license column). Last automated sync: 2026-11-25.
<!-- END:STATS -->

## Popular commercial software and open-source alternatives

If you want a fast starting point before browsing the full OSS software catalog, this table pairs widely used proprietary tools with mature open-source replacements.

<!-- START:FEATURED -->
| Software | Alternative to | Platform | License | Best for | Migration |
| --- | --- | --- | --- | --- | --- |
| [GIMP](https://www.gimp.org/) | Adobe Photoshop | Win, Mac, Linux | GPL-3.0 | Raster photo editing and image manipulation | Medium |
| [Blender](https://www.blender.org/) | Autodesk Maya, 3ds Max | Win, Mac, Linux | GPL-3.0 | 3D modeling, sculpting, VFX, rendering, and animation | Medium |
| [LibreOffice](https://www.libreoffice.org/) | Microsoft Office | Win, Mac, Linux | MPL-2.0 | Full desktop office suite (Writer, Calc, Impress) | Low |
| [Penpot](https://penpot.app/) | Figma | Web | MPL-2.0 | Collaborative UI/UX design with native CSS Grid and Flexbox | Medium |
| [Twenty](https://twenty.com/) | Salesforce, HubSpot | Web | AGPL-3.0 | Modern CRM with custom objects, Kanban views, and GraphQL API | Medium |
| [Matomo](https://matomo.org/) | Google Analytics | Web | GPL-3.0 | Full-featured self-hosted web analytics with 100% data ownership | Medium |
| [Nextcloud](https://nextcloud.com/) | Google Drive, Dropbox | Web, Win, Mac, Linux, Mobile | AGPL-3.0 | Self-hosted file sync, calendar, contacts, and groupware | Medium |
| [Ollama](https://ollama.com/) | OpenAI API, LM Studio | Win, Mac, Linux | MIT | Running open-weight LLMs locally via CLI and HTTP API | Low |
| [PostgreSQL](https://www.postgresql.org/) | Oracle Database, SQL Server | Win, Mac, Linux | PostgreSQL | Production OLTP, JSONB, geospatial, and vector workloads | Medium |
| [KeePassXC](https://keepassxc.org/) | 1Password, LastPass | Win, Mac, Linux | GPL-3.0 | Offline local KDBX vault with browser autofill and SSH agent | Low |
| [Kdenlive](https://kdenlive.org/) | Adobe Premiere Pro | Win, Mac, Linux | GPL-3.0 | Multi-track video editing with proxy clips and keyframing | Medium |
| [Audacity](https://www.audacityteam.org/) | Adobe Audition | Win, Mac, Linux | GPL-3.0 | Podcast recording, noise reduction, and quick waveform edits | Low |
<!-- END:FEATURED -->

## Categories

<!-- START:TOC -->
- [Office & Productivity](#office--productivity) (8)
- [Design & Graphics](#design--graphics) (8)
- [Video Editing](#video-editing) (7)
- [Audio Editing](#audio-editing) (6)
- [CRM](#crm) (7)
- [Project Management](#project-management) (8)
- [Artificial Intelligence](#artificial-intelligence) (8)
- [Development](#development) (10)
- [Password Managers](#password-managers) (6)
- [Analytics](#analytics) (7)
- [Cloud Storage](#cloud-storage) (6)
- [Automation](#automation) (7)
- [E-commerce](#e-commerce) (7)
- [Accounting](#accounting) (6)
- [Databases](#databases) (8)
- [3D Modeling](#3d-modeling) (6)
<!-- END:TOC -->

## Full open source software directory

Projects marked with `*` in the License column use an open-core business model. In those cases, the listed license applies to the Community or OSS edition, while enterprise modules such as SSO, audit logs, or multi-region clustering may sit under a commercial license.

<!-- START:CATALOG -->
### Office & Productivity

Document suites, note-taking apps, email clients, and collaborative workspaces. See the [detailed Office & Productivity notes](categories/office.md).

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [LibreOffice](https://www.libreoffice.org/) | Microsoft Office | Win, Mac, Linux | MPL-2.0 | 4.7k | Active | Low | Full desktop office suite (Writer, Calc, Impress) |
| [ONLYOFFICE Docs](https://www.onlyoffice.com/) | Microsoft 365, Google Docs | Web, Win, Mac, Linux | AGPL-3.0 (Community) * | 7.2k | Active | Low | Collaborative DOCX, XLSX, and PPTX editing |
| [CryptPad](https://cryptpad.org/) | Google Workspace | Web | AGPL-3.0 | 8.1k | Active | Medium | End-to-end encrypted real-time collaboration |
| [Collabora Online](https://www.collaboraonline.com/) | Microsoft 365 Online | Web | MPL-2.0 * | 3.4k | Active | Medium | Browser-based LibreOffice integrated with Nextcloud |
| [Logseq](https://logseq.com/) | Roam Research, Notion | Win, Mac, Linux, Mobile | AGPL-3.0 | 45.7k | Active | Medium | Local-first Markdown outliner and knowledge base |
| [Joplin](https://joplinapp.org/) | Evernote | Win, Mac, Linux, Mobile | AGPL-3.0 | 57.4k | Active | Low | Encrypted Markdown notebooks with multi-device sync |
| [AppFlowy](https://appflowy.io/) | Notion | Win, Mac, Linux, Mobile | AGPL-3.0 * | 79.5k | Active | Medium | Self-hosted docs, wikis, and lightweight databases |
| [Thunderbird](https://www.thunderbird.net/) | Microsoft Outlook | Win, Mac, Linux, Android | MPL-2.0 | 264 | Active | Low | Desktop email, calendar, and RSS client |

### Design & Graphics

Raster editors, vector graphics tools, UI prototyping, RAW photo editors, and desktop publishing. See the [detailed Design & Graphics notes](categories/design.md).

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [GIMP](https://www.gimp.org/) | Adobe Photoshop | Win, Mac, Linux | GPL-3.0 | - | Active | Medium | Raster photo editing and image manipulation |
| [Inkscape](https://inkscape.org/) | Adobe Illustrator | Win, Mac, Linux | GPL-2.0 | - | Active | Low | SVG vector illustration and logo design |
| [Krita](https://krita.org/) | Corel Painter, Clip Studio Paint | Win, Mac, Linux, Android | GPL-3.0 | 10.8k | Active | Low | Digital painting, concept art, and 2D animation |
| [Penpot](https://penpot.app/) | Figma | Web | MPL-2.0 | 62.7k | Active | Medium | Collaborative UI/UX design with native CSS Grid and Flexbox |
| [Darktable](https://www.darktable.org/) | Adobe Lightroom | Win, Mac, Linux | GPL-3.0 | 13.5k | Active | Medium | Non-destructive RAW photography workflow |
| [Scribus](https://www.scribus.net/) | Adobe InDesign | Win, Mac, Linux | GPL-2.0 | 659 | Active | High | Print page layout, CMYK brochures, and PDF publishing |
| [RawTherapee](https://www.rawtherapee.com/) | Adobe Camera Raw | Win, Mac, Linux | GPL-3.0 | 4.3k | Active | Medium | Detailed RAW color grading and lens correction |
| [Excalidraw](https://excalidraw.com/) | Miro, Lucidchart | Web | MIT * | 136.3k | Active | Low | Hand-drawn style architecture diagrams and whiteboarding |

### Video Editing

Non-linear video editors, screen recorders, streaming tools, and media transcoders.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Kdenlive](https://kdenlive.org/) | Adobe Premiere Pro | Win, Mac, Linux | GPL-3.0 | 6.2k | Active | Medium | Multi-track video editing with proxy clips and keyframing |
| [Shotcut](https://www.shotcut.org/) | iMovie, Filmora | Win, Mac, Linux | GPL-3.0 | 15.8k | Active | Low | Cross-platform timeline video editing without format import |
| [OpenShot](https://www.openshot.org/) | iMovie, Camtasia | Win, Mac, Linux | GPL-3.0 | 6.8k | Active | Low | Beginner-friendly cuts, titles, and simple transitions |
| [LosslessCut](https://mifi.no/losslesscut/) | QuickTime Pro, Premiere Trim | Win, Mac, Linux | GPL-2.0 | 46.4k | Active | Low | Instant lossless video and audio trimming without re-encoding |
| [OBS Studio](https://obsproject.com/) | XSplit, Wirecast | Win, Mac, Linux | GPL-2.0 | 80.1k | Active | Low | Live streaming, screen capture, and virtual cameras |
| [HandBrake](https://handbrake.fr/) | Adobe Media Encoder | Win, Mac, Linux | GPL-2.0 | 25.1k | Active | Low | Batch video compression and format conversion |
| [FFmpeg](https://ffmpeg.org/) | Commercial media transcoders | Win, Mac, Linux | LGPL-2.1 / GPL-2.0 | 68.2k | Active | High | Scriptable CLI audio and video processing pipelines |

### Audio Editing

Digital audio workstations, waveform editors, music notation software, and DJ decks.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Audacity](https://www.audacityteam.org/) | Adobe Audition | Win, Mac, Linux | GPL-3.0 | 19.2k | Active | Low | Podcast recording, noise reduction, and quick waveform edits |
| [Ardour](https://ardour.org/) | Pro Tools, Logic Pro | Win, Mac, Linux | GPL-2.0 | 5.5k | Active | High | Multi-track studio recording, mixing, and mastering |
| [LMMS](https://lmms.io/) | FL Studio | Win, Mac, Linux | GPL-2.0 | 10.7k | Active | Medium | Beat making, synthesizer sequencing, and electronic music |
| [Tenacity](https://tenacityaudio.org/) | Adobe Audition | Win, Mac, Linux | GPL-2.0 | - | Active | Low | Privacy-focused Audacity fork without telemetry |
| [MuseScore](https://musescore.org/) | Sibelius, Finale | Win, Mac, Linux | GPL-3.0 | 15.5k | Active | Low | Sheet music composition and MusicXML engraving |
| [Mixxx](https://mixxx.org/) | Serato DJ, Traktor | Win, Mac, Linux | GPL-2.0 | 7.4k | Active | Low | Live DJ mixing with MIDI controller support |

### CRM

Customer relationship management platforms for sales pipelines, support teams, and personal contacts. See the [detailed CRM notes](categories/crm.md).

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Twenty](https://twenty.com/) | Salesforce, HubSpot | Web | AGPL-3.0 * | 61.5k | Active | Medium | Modern CRM with custom objects, Kanban views, and GraphQL API |
| [EspoCRM](https://www.espocrm.com/) | Salesforce, Zoho CRM | Web | AGPL-3.0 * | 3.7k | Active | Medium | Lightweight B2B CRM for sales, leads, and email sync |
| [SuiteCRM](https://suitecrm.com/) | Salesforce Enterprise | Web | AGPL-3.0 | 5.9k | Active | High | Enterprise-scale CRM with quotes, contracts, and workflows |
| [Monica](https://www.monicahq.com/) | Clay, Dex | Web | AGPL-3.0 | 25.8k | Active | Low | Personal CRM for tracking relationships, notes, and reminders |
| [Frappe CRM](https://frappe.io/crm) | HubSpot, Pipedrive | Web | AGPL-3.0 | 4.0k | Active | Medium | Clean deal pipeline that connects natively to ERPNext |
| [Krayin CRM](https://krayincrm.com/) | Pipedrive, Zoho CRM | Web | MIT | 24.2k | Active | Medium | Laravel-based CRM for small and mid-sized teams |
| [Dolibarr](https://www.dolibarr.org/) | Salesforce, NetSuite | Web | GPL-3.0 | 7.9k | Active | High | Combined CRM and ERP for SMEs and freelancers |

### Project Management

Issue trackers, Kanban boards, sprint planners, and portfolio management tools.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [OpenProject](https://www.openproject.org/) | Microsoft Project, Jira | Web | GPL-3.0 (Community) * | 17.7k | Active | Medium | Gantt charts, agile boards, and enterprise project portfolios |
| [Taiga](https://taiga.io/) | Jira, Trello | Web | MPL-2.0 | 858 | Active | Low | Scrum and Kanban workflows for cross-functional product teams |
| [Plane](https://plane.so/) | Jira, Linear | Web | AGPL-3.0 (Community) * | 63.1k | Active | Low | Fast issue tracking, sprint cycles, and roadmap modules |
| [Leantime](https://leantime.io/) | Asana, Monday.com | Web | AGPL-3.0 * | 12.1k | Active | Low | Goal-oriented project planning for non-technical teams |
| [Redmine](https://www.redmine.org/) | Jira | Web | GPL-2.0 | 6.1k | Active | Medium | Long-running issue tracking with per-project wikis and time logs |
| [Vikunja](https://vikunja.io/) | Todoist, Trello | Web, Win, Mac, Linux, Mobile | AGPL-3.0 | 6.2k | Active | Low | Self-hosted task lists, Kanban boards, and Gantt views |
| [Planka](https://planka.app/) | Trello | Web | AGPL-3.0 | 12.7k | Active | Low | Minimal real-time Kanban boards with simple Docker setup |
| [Focalboard](https://github.com/mattermost-community/focalboard) | Trello, Notion Boards | Web, Win, Mac, Linux | MIT | 26.6k | Maintained | Low | Self-hosted boards, tables, and personal project templates |

### Artificial Intelligence

Local LLM runners, chat interfaces, inference servers, and image generation pipelines. See the [detailed Artificial Intelligence notes](categories/artificial-intelligence.md).

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Ollama](https://ollama.com/) | OpenAI API, LM Studio | Win, Mac, Linux | MIT | 188.1k | Active | Low | Running open-weight LLMs locally via CLI and HTTP API |
| [Open WebUI](https://openwebui.com/) | ChatGPT Web UI | Web | Open WebUI License (BSD-3-Clause based) * | 159.5k | Active | Low | Self-hosted chat interface for Ollama and OpenAI-compatible APIs |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Proprietary LLM runtimes | Win, Mac, Linux | MIT | 136.2k | Active | Medium | Low-overhead C/C++ inference for quantized GGUF models |
| [vLLM](https://vllm.ai/) | Proprietary LLM serving platforms | Linux | Apache-2.0 | 97.6k | Active | Medium | High-throughput GPU model serving with PagedAttention |
| [ComfyUI](https://www.comfy.org/) | Midjourney, Adobe Firefly | Win, Mac, Linux, Web | GPL-3.0 | 148.6k | Active | Medium | Node-based image and video diffusion workflows |
| [LocalAI](https://localai.io/) | OpenAI API | Linux, Mac, Win | MIT | 50.5k | Active | Low | Drop-in local REST API for text, audio, and image models |
| [AnythingLLM](https://anythingllm.com/) | ChatGPT Team, Custom GPTs | Win, Mac, Linux, Web | MIT | 68.6k | Active | Low | Desktop and server RAG workspaces over local documents |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Commercial speech-to-text APIs | Win, Mac, Linux | MIT | 55.5k | Active | Low | Fast offline audio transcription on CPU or Apple Silicon |

### Development

Code editors, IDEs, self-hosted Git platforms, API clients, and database GUIs. See the [detailed Development notes](categories/developer-tools.md).

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [VSCodium](https://vscodium.com/) | Visual Studio Code | Win, Mac, Linux | MIT | 34.3k | Active | Low | VS Code binary builds without Microsoft telemetry |
| [Eclipse IDE](https://www.eclipse.org/) | IntelliJ IDEA | Win, Mac, Linux | EPL-2.0 | 173 | Active | Medium | Enterprise Java, C/C++, and embedded development |
| [Neovim](https://neovim.io/) | Sublime Text, VS Code | Win, Mac, Linux | Apache-2.0 | 103.9k | Active | High | Keyboard-driven terminal editor with Lua plugins and LSP |
| [Zed](https://zed.dev/) | VS Code, Sublime Text | Mac, Linux, Win | GPL-3.0 / Apache-2.0 * | 95.7k | Active | Low | GPU-accelerated code editing written in Rust |
| [GitLab CE](https://about.gitlab.com/) | GitHub Enterprise, Bitbucket | Web | MIT (Community Edition) * | - | Active | Medium | All-in-one self-hosted Git, CI/CD, and container registry |
| [Gitea](https://about.gitea.com/) | GitHub, Bitbucket | Web | MIT * | 59.3k | Active | Low | Lightweight Go-based Git forge with built-in Actions |
| [Forgejo](https://forgejo.org/) | GitHub, GitLab | Web | GPL-3.0 | - | Active | Low | Community-governed self-hosted Git forge forked from Gitea |
| [Bruno](https://www.usebruno.com/) | Postman, Insomnia | Win, Mac, Linux | MIT * | 48.6k | Active | Low | Offline-first API client storing collections in Git |
| [Hoppscotch](https://hoppscotch.io/) | Postman | Web, Win, Mac, Linux | MIT * | 81.0k | Active | Low | Fast browser and desktop REST, GraphQL, and WebSocket testing |
| [DBeaver Community](https://dbeaver.io/) | DataGrip, Navicat | Win, Mac, Linux | Apache-2.0 (Community) * | 52.5k | Active | Low | Universal SQL client supporting dozens of database engines |

### Password Managers

Encrypted password vaults for individuals, families, and self-hosted engineering teams.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [KeePassXC](https://keepassxc.org/) | 1Password, LastPass | Win, Mac, Linux | GPL-3.0 | 30.1k | Active | Low | Offline local KDBX vault with browser autofill and SSH agent |
| [Bitwarden](https://bitwarden.com/) | 1Password, Dashlane | Web, Win, Mac, Linux, Mobile | GPL-3.0 / AGPL-3.0 * | 14.3k | Active | Low | Cross-device cloud or self-hosted password management |
| [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | Bitwarden Server, 1Password Teams | Web | AGPL-3.0 | 71.3k | Active | Low | Low-memory Rust backend compatible with official Bitwarden clients |
| [Passbolt](https://www.passbolt.com/) | 1Password Business | Web, Mobile | AGPL-3.0 (Community) * | 6.2k | Active | Medium | OpenPGP-based team credential sharing and auditing |
| [pass](https://www.passwordstore.org/) | 1Password CLI | Linux, Mac | GPL-2.0 | - | Active | Medium | Unix-style GPG-encrypted password files synced via Git |
| [KeePassDX](https://www.keepassdx.com/) | 1Password Mobile | Android | GPL-3.0 | 7.7k | Active | Low | Offline KeePass vault manager on Android with autofill |

### Analytics

Privacy-focused web analytics, product analytics, and business intelligence dashboards.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Matomo](https://matomo.org/) | Google Analytics | Web | GPL-3.0 * | 22.1k | Active | Medium | Full-featured self-hosted web analytics with 100% data ownership |
| [Metabase](https://www.metabase.com/) | Tableau, Power BI | Web | AGPL-3.0 (OSS) * | 50.5k | Active | Low | Self-service SQL and visual BI dashboards for product teams |
| [Plausible Analytics](https://plausible.io/) | Google Analytics | Web | AGPL-3.0 | 29.9k | Active | Low | Lightweight cookie-free web analytics under 1 KB script size |
| [Umami](https://umami.is/) | Google Analytics | Web | MIT | 40.3k | Active | Low | Simple privacy-friendly site analytics running on PostgreSQL |
| [Apache Superset](https://superset.apache.org/) | Tableau, Looker | Web | Apache-2.0 | 75.7k | Active | High | Enterprise data exploration and SQL-based BI charts |
| [PostHog](https://posthog.com/) | Mixpanel, Amplitude | Web | MIT (FOSS) * | 41.1k | Active | Medium | Product analytics, session replay, and feature flags |
| [Lightdash](https://www.lightdash.com/) | Looker | Web | MIT * | 6.3k | Active | Medium | BI platform built directly on top of dbt models |

### Cloud Storage

Self-hosted file sync, photo libraries, and peer-to-peer folder synchronization.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Nextcloud](https://nextcloud.com/) | Google Drive, Dropbox | Web, Win, Mac, Linux, Mobile | AGPL-3.0 | 37.6k | Active | Medium | Self-hosted file sync, calendar, contacts, and groupware |
| [Syncthing](https://syncthing.net/) | Dropbox, Resilio Sync | Win, Mac, Linux, Android | MPL-2.0 | 90.8k | Active | Low | Continuous peer-to-peer folder sync without a central server |
| [Seafile](https://www.seafile.com/) | Dropbox, OneDrive | Web, Win, Mac, Linux, Mobile | GPL-2.0 (Community) * | 15.5k | Active | Medium | High-speed encrypted file sync with virtual drive mounting |
| [ownCloud Infinite Scale](https://owncloud.com/) | Google Drive, SharePoint | Web, Win, Mac, Linux, Mobile | Apache-2.0 * | 2.2k | Active | Medium | Go-based enterprise file platform without a SQL database |
| [Immich](https://immich.app/) | Google Photos, iCloud Photos | Web, Mobile | AGPL-3.0 | 120.1k | Active | Low | Self-hosted photo and video backup with local ML search |
| [Rclone](https://rclone.org/) | Commercial cloud sync bridges | Win, Mac, Linux | MIT | 61.3k | Active | Medium | Encrypted CLI sync, backup, and mounting across 70+ cloud providers |

### Automation

Workflow engines, API connectors, IoT automation, and home control hubs.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Node-RED](https://nodered.org/) | Zapier, Make (IoT) | Web, Linux, Mac, Win | Apache-2.0 | 23.9k | Active | Medium | Flow-based programming for hardware devices, MQTT, and APIs |
| [Activepieces](https://www.activepieces.com/) | Zapier, Make | Web | MIT (Community) * | 25.7k | Active | Low | No-code SaaS and AI workflow automation with TypeScript pieces |
| [Automatisch](https://automatisch.io/) | Zapier | Web | AGPL-3.0 * | 14.0k | Maintained | Low | Self-hosted business workflow automation for GDPR compliance |
| [Huginn](https://github.com/huginn/huginn) | IFTTT, Zapier | Web | MIT | 50.6k | Active | Medium | Autonomous web monitoring agents and scheduled alerts |
| [Windmill](https://www.windmill.dev/) | Retool Workflows, Temporal | Web | AGPL-3.0 (Community) * | 18.7k | Active | Medium | Developer workflows turning Python, TS, or Bash scripts into apps |
| [Kestra](https://kestra.io/) | Prefect Cloud, Airflow Managed | Web | Apache-2.0 (OSS) * | 30.4k | Active | Medium | Declarative YAML orchestration for data and event workflows |
| [Home Assistant](https://www.home-assistant.io/) | Apple Home, Google Home | Web, Linux, Mobile | Apache-2.0 | 92.5k | Active | Medium | Local smart-home automation with thousands of device integrations |

### E-commerce

Online storefronts, headless commerce engines, and self-hosted shopping carts.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [PrestaShop](https://www.prestashop-project.org/) | Shopify, BigCommerce | Web | OSL-3.0 | 9.3k | Active | Medium | Complete PHP online store with multi-currency and EU tax support |
| [WooCommerce](https://woocommerce.com/) | Shopify | Web | GPL-3.0 | 10.6k | Active | Low | E-commerce stores running inside WordPress |
| [Medusa](https://medusajs.com/) | Shopify Plus, Commercetools | Web | MIT | 37.4k | Active | High | Headless TypeScript commerce engine with modular APIs |
| [Saleor](https://saleor.io/) | Shopify Plus | Web | BSD-3-Clause | 23.6k | Active | High | GraphQL-first Python headless commerce for multi-channel retail |
| [Bagisto](https://bagisto.com/) | Magento, Shopify | Web | MIT | 28.4k | Active | Medium | Laravel e-commerce storefront with multi-vendor extensions |
| [Vendure](https://www.vendure.io/) | Shopify Plus, Commercetools | Web | MIT | 8.6k | Active | High | Extensible NestJS and GraphQL headless commerce framework |
| [OpenCart](https://www.opencart.com/) | Shopify, BigCommerce | Web | GPL-3.0 | 8.2k | Active | Medium | Lightweight PHP shopping cart for traditional shared hosting |

### Accounting

Double-entry bookkeeping, small-business invoicing, ERP accounting, and personal finance.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [GnuCash](https://www.gnucash.org/) | QuickBooks Desktop, Quicken | Win, Mac, Linux | GPL-2.0 | 4.4k | Active | Medium | Desktop double-entry accounting for individuals and small firms |
| [Akaunting](https://akaunting.com/) | QuickBooks Online, Xero | Web | GPL-3.0 * | 10.3k | Active | Medium | Web invoicing, expense tracking, and small-business cash flow |
| [Firefly III](https://www.firefly-iii.org/) | Mint, YNAB | Web | AGPL-3.0 | 25.3k | Active | Low | Self-hosted personal finance, budgets, and bank rule automation |
| [Actual Budget](https://actualbudget.org/) | YNAB | Web, Win, Mac, Linux | MIT | 30.5k | Active | Low | Local-first envelope budgeting with optional self-hosted sync |
| [ERPNext](https://erpnext.com/) | NetSuite, SAP Business One | Web | GPL-3.0 | 41.6k | Active | High | Full ERP accounting, inventory, payroll, and manufacturing |
| [hledger](https://hledger.org/) | Quicken, Excel ledgers | Win, Mac, Linux | GPL-3.0 | 4.8k | Active | High | Plain-text double-entry accounting stored in version control |

### Databases

Relational databases, analytical engines, key-value stores, and embedded backends.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [PostgreSQL](https://www.postgresql.org/) | Oracle Database, SQL Server | Win, Mac, Linux | PostgreSQL | 22.9k | Active | Medium | Production OLTP, JSONB, geospatial, and vector workloads |
| [MariaDB](https://mariadb.org/) | MySQL Enterprise, SQL Server | Win, Mac, Linux | GPL-2.0 | 8.7k | Active | Low | Drop-in MySQL-compatible relational database for web apps |
| [SQLite](https://www.sqlite.org/) | Embedded commercial databases | Win, Mac, Linux, Mobile | Public Domain | 11.1k | Active | Low | Zero-configuration single-file SQL database for apps and edge |
| [ClickHouse](https://clickhouse.com/) | Snowflake, BigQuery | Linux, Mac | Apache-2.0 | 51.1k | Active | High | Real-time columnar analytics over billions of event rows |
| [DuckDB](https://duckdb.org/) | Snowflake (local), Databricks | Win, Mac, Linux | MIT | 43.3k | Active | Low | In-process OLAP SQL over Parquet, CSV, and JSON files |
| [Valkey](https://valkey.io/) | Redis Enterprise | Linux, Mac | BSD-3-Clause | 27.9k | Active | Low | High-performance in-memory cache, pub/sub, and message broker |
| [Meilisearch](https://www.meilisearch.com/) | Algolia | Linux, Mac, Win | MIT | 60.0k | Active | Low | Typo-tolerant instant full-text and hybrid search engine |
| [Supabase](https://supabase.com/) | Firebase | Web, Linux | Apache-2.0 * | 115.5k | Active | Low | Postgres-backed Backend-as-a-Service with auth, storage, and realtime |

### 3D Modeling

3D animation suites, parametric CAD tools, mesh processors, and game engines.

| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Blender](https://www.blender.org/) | Autodesk Maya, 3ds Max | Win, Mac, Linux | GPL-3.0 | 22.5k | Active | Medium | 3D modeling, sculpting, VFX, rendering, and animation |
| [FreeCAD](https://www.freecad.org/) | SolidWorks, Fusion 360 | Win, Mac, Linux | LGPL-2.1 | 35.8k | Active | High | Parametric 3D CAD for mechanical engineering and 3D printing |
| [OpenSCAD](https://openscad.org/) | Fusion 360 (parametric) | Win, Mac, Linux | GPL-2.0 | 10.7k | Active | Medium | Code-driven 3D solid CAD models for programmable parts |
| [Godot Engine](https://godotengine.org/) | Unity, Unreal Engine | Win, Mac, Linux, Web | MIT | 120.8k | Active | Medium | Cross-platform 2D and 3D game development without royalties |
| [LibreCAD](https://librecad.org/) | AutoCAD 2D | Win, Mac, Linux | GPL-2.0 | 6.6k | Active | Low | 2D technical drafting with native DXF file support |
| [MeshLab](https://www.meshlab.net/) | Geomagic Wrap | Win, Mac, Linux | GPL-3.0 | 5.9k | Active | Low | Processing, cleaning, and repairing 3D scanned triangular meshes |
<!-- END:CATALOG -->

## Migration guides

Switching away from proprietary tools usually fails on file formats, team habits, or missing integrations. These step-by-step guides document the trade-offs and export steps:

- [Migrating from Salesforce to Twenty CRM](migration-guides/salesforce-to-twenty.md)
- [Migrating from Adobe Photoshop to GIMP](migration-guides/photoshop-to-gimp.md)

## How licenses and open-core editions are verified

Many modern developer and business tools mix open-source cores with proprietary enterprise plugins. Before adopting any OSS software in production, check three details:

1. Check the exact edition you plan to install. For example, GitLab CE is MIT-licensed, while GitLab EE includes proprietary code under a commercial license.
2. Review copyleft obligations. AGPL-3.0 requires publishing source modifications if you offer the modified software over a network; GPL-2.0 and GPL-3.0 apply to distributed binaries; MIT, Apache-2.0, and BSD-3-Clause allow permissive commercial reuse.
3. Confirm maintenance activity. Star counts grow over time even on stalled repositories, so the catalog tracks recent commit activity and release dates alongside stars.

## Automation and data source

All comparison tables in this README and in the `categories/` pages are generated from [data/software.json](data/software.json) by [scripts/update-directory.py](scripts/update-directory.py). A scheduled GitHub Actions workflow runs weekly to:

- Update GitHub star counts from the GitHub REST API.
- Refresh the latest release date and recent commit activity status.
- Cross-check SPDX license metadata for GitHub-hosted repositories.
- Verify that homepage URLs respond without dead links.
- Rebuild the Markdown tables when metadata changes.

## Contributing

Corrections to licenses, migration ratings, and suggestions for actively maintained open-source software are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This directory and its automation scripts are released under the [MIT License](LICENSE). Individual software projects linked in the catalog remain under their own respective licenses.
