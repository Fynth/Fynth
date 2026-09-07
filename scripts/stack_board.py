#!/usr/bin/env python3
"""Build assets/stack-board.svg from the CV stack."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "stack-board.svg"

SECTIONS = [
    ("RUST", "#ff7b54", "#3a1710", "#ffd4c4",
     ["Tokio", "Axum", "Actix", "Reqwest", "Serde", "SQLx", "Diesel", "Dioxus", "Tauri"]),
    ("GO", "#4da3ff", "#0a2744", "#c8e4ff",
     ["Gin", "Fiber", "Echo", "GORM"]),
    ("PYTHON", "#3dd68c", "#0d2f18", "#c0f0d2",
     ["Django", "DRF", "FastAPI", "Flask", "Pydantic", "SQLAlchemy", "Celery", "pytest", "Pandas", "Requests"]),
    ("DATA", "#4da3ff", "#102433", "#c8e4ff",
     ["PostgreSQL", "MySQL", "SQLite", "ClickHouse", "Redis", "MongoDB"]),
    ("BACKEND", "#b692f6", "#1a1428", "#ead9ff",
     ["REST", "WebSockets", "gRPC", "RabbitMQ", "Kafka"]),
    ("SHIP", "#ff7b54", "#2a140e", "#ffd4c4",
     ["Docker", "Compose", "Linux", "Nginx", "Git", "GitHub Actions", "CI/CD"]),
]


def chip_w(label: str) -> int:
    return max(72, 28 + len(label) * 8)


def layout():
    x0, y = 48, 88
    max_x = 1080 - 48
    gap, h = 10, 34
    rows = []
    for name, stroke, fill, text, chips in SECTIONS:
        rows.append(("label", name, stroke, y))
        y += 22
        x = x0
        line_y = y
        placed = []
        for c in chips:
            w = chip_w(c)
            if x + w > max_x:
                x = x0
                line_y += h + gap
            placed.append((c, x, line_y, w, fill, stroke, text))
            x += w + gap
        rows.append(("chips", placed))
        y = line_y + h + 28
    return rows, y + 16


def svg() -> str:
    rows, height = layout()
    parts = []
    delay = 0.0
    for item in rows:
        if item[0] == "label":
            _, name, color, y = item
            tracking = "2" if len(name) > 3 else "1"
            parts.append(
                f'<text x="48" y="{y}" fill="{color}" font-size="12" letter-spacing="{tracking}" font-weight="700">{name}</text>'
            )
        else:
            for label, x, y, w, fill, stroke, text in item[1]:
                parts.append(
                    f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{fill}" stroke="{stroke}" stroke-opacity="0.55">'
                    f'<animate attributeName="stroke-opacity" values="0.35;0.85;0.35" dur="4s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
                    f"</rect>"
                    f'<text x="{x + w / 2:.1f}" y="{y + 22}" text-anchor="middle" fill="{text}" font-size="13">{label}</text>'
                )
                delay += 0.08
    inner = "\n    ".join(parts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="{height}" viewBox="0 0 1080 {height}" role="img" aria-labelledby="title">
  <title id="title">Full stack</title>
  <defs>
    <clipPath id="board">
      <rect width="1080" height="{height}" rx="24"/>
    </clipPath>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ff7b54"/>
      <stop offset="50%" stop-color="#4da3ff"/>
      <stop offset="100%" stop-color="#b692f6"/>
    </linearGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="28"/>
    </filter>
  </defs>
  <g clip-path="url(#board)">
    <rect width="1080" height="{height}" fill="#070b12"/>
    <circle cx="980" cy="40" r="160" fill="#4da3ff" opacity="0.18" filter="url(#soft)">
      <animate attributeName="opacity" values="0.1;0.24;0.1" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="80" cy="{height - 40}" r="140" fill="#ff7b54" opacity="0.14" filter="url(#soft)">
      <animate attributeName="opacity" values="0.08;0.2;0.08" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="540" cy="{height // 2}" r="180" fill="#3dd68c" opacity="0.08" filter="url(#soft)">
      <animate attributeName="opacity" values="0.05;0.14;0.05" dur="8s" repeatCount="indefinite"/>
    </circle>
  </g>
  <rect x="1.5" y="1.5" width="1077" height="{height - 3}" rx="23" fill="none" stroke="url(#edge)" stroke-opacity="0.45"/>
  <text x="48" y="48" fill="#ffffff" font-size="22" font-weight="700" font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif">Stack</text>
  <g font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif">
    {inner}
  </g>
</svg>
'''


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(svg(), encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
