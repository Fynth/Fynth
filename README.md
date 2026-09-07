<div align="center">
  <img src="assets/header.svg" alt="Rasul — backend and systems" width="100%" />
</div>

<br/>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3400&pause=1100&color=58A6FF&center=true&vCenter=true&width=720&lines=Desktop+apps%2C+HTTP+APIs%2C+Linux+packages;Rust+%C2%B7+Go+%C2%B7+Python;Moscow+%C2%B7+open+to+backend+roles" alt="typing" />
</div>

<div align="center">
  <a href="#map">map</a> ·
  <a href="#projects">projects</a> ·
  <a href="#stack">stack</a> ·
  <a href="#github">github</a> ·
  <a href="mailto:rasulmagomedsaidov2002@gmail.com">email</a>
</div>

<br/>

<div align="center">
  <img src="https://skillicons.dev/icons?i=rust,go,python,c,postgres,mysql,redis,docker,linux,nginx,githubactions,git" alt="skills" />
</div>

---

I build software that talks to databases, networks, and Linux. Public work is split across desktop tools, REST services, and small utilities, not one repo.

Open to backend, Rust, and Go roles.

## Map

How the public work sits together.

```mermaid
flowchart LR
  subgraph Languages
    R[Rust]
    G[Go]
    P[Python]
    C[C]
  end

  subgraph Desktop
    S[Shovel]
    L[Lanius]
  end

  subgraph APIs
    T[tz]
    T2[tz2]
    W[whenwas]
    D[django store]
    TD[todoshka]
  end

  subgraph Data
    PG[(PostgreSQL)]
    SQ[(SQLite)]
    MY[(MySQL)]
    CH[(ClickHouse)]
    RD[(Redis)]
  end

  R --> S
  R --> L
  G --> T
  G --> W
  G --> TD
  P --> T2
  P --> D
  C --> CI[Cinter]

  S --> PG
  S --> SQ
  S --> MY
  S --> CH
  T --> PG
  T2 --> PG
  T2 --> RD
  TD --> SQ
```

```mermaid
timeline
    title What showed up on GitHub
    2019 : Account created
    2021 : Bank calculator in C++
    2022 : Cinter, a small C interpreter
    2023 : Qt client / server experiment
    2025 : Go and Django APIs, Docker Compose
    2026 : Shovel, packaging, Lanius
```

<details>
<summary>A more literal stack view</summary>

```mermaid
flowchart TB
  code[Code] --> test[Tests / CI]
  test --> pack[Docker · deb · AUR · Flatpak · MSI]
  pack --> run[Linux and desktop users]

  code --- rust[Rust / Dioxus / Tokio]
  code --- go[Go net/http]
  code --- py[Django / DRF / Celery]
```

</details>

## Projects

Click a card. Stars and language update on their own.

<div align="center">
  <a href="https://github.com/Fynth/Shovel">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=Shovel&theme=transparent&hide_border=true" alt="Shovel" />
  </a>
  <a href="https://github.com/Fynth/tz">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=tz&theme=transparent&hide_border=true" alt="tz" />
  </a>
</div>
<div align="center">
  <a href="https://github.com/Fynth/tz2">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=tz2&theme=transparent&hide_border=true" alt="tz2" />
  </a>
  <a href="https://github.com/Fynth/whenwas">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=whenwas&theme=transparent&hide_border=true" alt="whenwas" />
  </a>
</div>
<div align="center">
  <a href="https://github.com/Fynth/awesome-django-store">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=awesome-django-store&theme=transparent&hide_border=true" alt="awesome-django-store" />
  </a>
  <a href="https://github.com/Fynth/todoshka">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Fynth&repo=todoshka&theme=transparent&hide_border=true" alt="todoshka" />
  </a>
</div>

<table>
<tr>
<td valign="top" width="50%">

**Shovel** — native database client in Rust. SQLite, PostgreSQL, MySQL, ClickHouse. Chat-first SQL, ACP agents, `.deb` / AUR / Flatpak / MSI.

[repo](https://github.com/Fynth/Shovel) · [install](https://fynth.github.io/Shovel/) · [releases](https://github.com/Fynth/Shovel/releases)

</td>
<td valign="top" width="50%">

**tz** — Go REST service for subscription records. PostgreSQL, migrations, Swagger, Docker Compose, `net/http`.

[repo](https://github.com/Fynth/tz)

</td>
</tr>
<tr>
<td valign="top">

**tz2** — Django REST task API plus a Telegram bot. Celery, Redis, PostgreSQL, Docker Compose.

[repo](https://github.com/Fynth/tz2)

</td>
<td valign="top">

**whenwas** — tiny Go service. Pass a domain, get the first Wayback Machine snapshot. Stdlib only.

[repo](https://github.com/Fynth/whenwas)

</td>
</tr>
<tr>
<td valign="top">

**awesome-django-store** — Django 5 shop: catalog, cart, orders, accounts.

[repo](https://github.com/Fynth/awesome-django-store)

</td>
<td valign="top">

**todoshka** — Go REST todo API. SQLite, Gorilla Mux, tests.

[repo](https://github.com/Fynth/todoshka)

</td>
</tr>
</table>

<details>
<summary>Older / smaller</summary>

- [Cinter](https://github.com/Fynth/Cinter) — C interpreter, written to learn how languages run
- [calculator](https://github.com/Fynth/calculator) — C++ calculator
- Lanius — agentless Linux configuration in Rust, not public yet

</details>

## Stack

| Layer | What I use |
| --- | --- |
| Languages | Rust, Go, Python, some C |
| Data | PostgreSQL, SQLite, MySQL, ClickHouse, Redis |
| Backend | REST, Django / DRF, Go `net/http`, Tokio, Celery |
| Desktop | Dioxus, SSH connections |
| Ship | Docker, Compose, GitHub Actions, Nginx, deb / AUR / Flatpak |

## GitHub

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Fynth&show_icons=true&theme=transparent&hide_border=true&count_private=true&include_all_commits=true" alt="stats" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Fynth&layout=compact&theme=transparent&hide_border=true&hide=html,css,makefile,scss&langs_count=6" alt="top languages" height="165" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=Fynth&theme=transparent&hide_border=true" alt="streak" />
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Fynth&bg_color=00000000&color=8b949e&line=58a6ff&point=f78166&area=true&hide_border=true&area_color=58a6ff" alt="activity graph" />
</div>

<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Fynth/Fynth/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Fynth/Fynth/output/github-contribution-grid-snake.svg" />
    <img alt="github contribution snake" src="https://raw.githubusercontent.com/Fynth/Fynth/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

## Contact

<div align="center">

[rasulmagomedsaidov2002@gmail.com](mailto:rasulmagomedsaidov2002@gmail.com)

[Shovel](https://github.com/Fynth/Shovel) · [tz](https://github.com/Fynth/tz) · [tz2](https://github.com/Fynth/tz2) · [whenwas](https://github.com/Fynth/whenwas)

</div>
