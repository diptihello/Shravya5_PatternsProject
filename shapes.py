# ── SVG Shape Renderer ─────────────────────────────────────────────────────
# Returns an inline SVG string for a given shape name.

import math

COLORS = ["#a855f7", "#06b6d4", "#f97316", "#fbbf24", "#22c55e", "#ec4899"]

SHAPE_LABELS = {
    "circle":       "○ Circle",
    "square":       "□ Square",
    "triangle":     "△ Triangle",
    "star":         "★ Star",
    "pentagon":     "⬠ Pentagon",
    "hexagon":      "⬡ Hexagon",
    "heptagon":     "⬡ Heptagon",
    "octagon":      "⬡ Octagon",
    "small-circle": "○ Small Circle",
    "medium-circle":"○ Med Circle",
    "large-circle": "○ Large Circle",
    "xlarge-circle":"○ XL Circle",
    "line":         "— Line",
}


def _polygon_pts(n, cx, cy, r, offset=0):
    pts = []
    for i in range(n):
        angle = (i * 2 * math.pi / n) + offset
        pts.append(f"{cx + r * math.cos(angle):.2f},{cy + r * math.sin(angle):.2f}")
    return " ".join(pts)


def get_shape_svg(name: str, color_idx: int = 0, size: int = 48) -> str:
    color = COLORS[color_idx % len(COLORS)]
    cx = cy = size / 2
    r  = size * 0.40

    open_tag  = f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    close_tag = '</svg>'

    if name == "circle":
        inner = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.9"/>'

    elif name == "small-circle":
        inner = f'<circle cx="{cx}" cy="{cy}" r="{size*0.18:.1f}" fill="{color}" opacity="0.9"/>'

    elif name == "medium-circle":
        inner = f'<circle cx="{cx}" cy="{cy}" r="{size*0.28:.1f}" fill="{color}" opacity="0.9"/>'

    elif name in ("large-circle", "xlarge-circle"):
        rad = size * 0.42 if name == "large-circle" else size * 0.47
        inner = f'<circle cx="{cx}" cy="{cy}" r="{rad:.1f}" fill="{color}" opacity="0.9"/>'

    elif name == "square":
        pad = size * 0.14
        w   = size - pad * 2
        inner = f'<rect x="{pad:.1f}" y="{pad:.1f}" width="{w:.1f}" height="{w:.1f}" rx="3" fill="{color}" opacity="0.9"/>'

    elif name == "triangle":
        pts = f"{cx:.1f},{size*0.1:.1f} {size*0.92:.1f},{size*0.9:.1f} {size*0.08:.1f},{size*0.9:.1f}"
        inner = f'<polygon points="{pts}" fill="{color}" opacity="0.9"/>'

    elif name == "star":
        outer, inner_r = cx * 0.9, cx * 0.38
        pts = []
        for i in range(10):
            angle = i * math.pi / 5 - math.pi / 2
            rad   = outer if i % 2 == 0 else inner_r
            pts.append(f"{cx + rad * math.cos(angle):.2f},{cy + rad * math.sin(angle):.2f}")
        inner = f'<polygon points="{" ".join(pts)}" fill="{color}" opacity="0.9"/>'

    elif name == "pentagon":
        inner = f'<polygon points="{_polygon_pts(5, cx, cy, r, -math.pi/2)}" fill="{color}" opacity="0.9"/>'

    elif name == "hexagon":
        inner = f'<polygon points="{_polygon_pts(6, cx, cy, r)}" fill="{color}" opacity="0.9"/>'

    elif name == "heptagon":
        inner = f'<polygon points="{_polygon_pts(7, cx, cy, r, -math.pi/2)}" fill="{color}" opacity="0.9"/>'

    elif name == "octagon":
        inner = f'<polygon points="{_polygon_pts(8, cx, cy, r, -math.pi/8)}" fill="{color}" opacity="0.9"/>'

    elif name == "line":
        inner = f'<line x1="4" y1="{cy:.1f}" x2="{size-4}" y2="{cy:.1f}" stroke="{color}" stroke-width="4" stroke-linecap="round" opacity="0.9"/>'

    else:
        inner = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="0.4"/>'

    return f"{open_tag}{inner}{close_tag}"
