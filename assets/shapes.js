/* ── SHAPE SVG DEFINITIONS ──────────────────────────────────────────────────
   Each shape is rendered as an inline SVG string via JS.
   Colours cycle through the accent palette for visual variety.
   ─────────────────────────────────────────────────────────────────────────── */

const SHAPE_COLORS = [
  '#a855f7', // purple
  '#06b6d4', // teal
  '#f97316', // coral
  '#fbbf24', // yellow
  '#22c55e', // green
  '#ec4899', // pink
];

/**
 * Returns an SVG string for a given shape name.
 * @param {string} name  - shape identifier (circle, square, triangle, etc.)
 * @param {number} colorIndex - index into SHAPE_COLORS array
 * @param {number} size  - width/height in px (default 40)
 */
function getShapeSVG(name, colorIndex = 0, size = 40) {
  const color = SHAPE_COLORS[colorIndex % SHAPE_COLORS.length];
  const half  = size / 2;
  const r     = size * 0.42;

  const svgOpen = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">`;
  const svgClose = `</svg>`;

  switch (name) {
    case 'circle':
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${r}" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'square':
      const sq = size * 0.15;
      return `${svgOpen}<rect x="${sq}" y="${sq}" width="${size - sq*2}" height="${size - sq*2}" rx="4" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'triangle': {
      const pts = `${half},${size * 0.1} ${size * 0.92},${size * 0.9} ${size * 0.08},${size * 0.9}`;
      return `${svgOpen}<polygon points="${pts}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'star': {
      const outerR = half * 0.9, innerR = half * 0.4;
      const points = [];
      for (let i = 0; i < 10; i++) {
        const angle = (i * Math.PI) / 5 - Math.PI / 2;
        const rad   = i % 2 === 0 ? outerR : innerR;
        points.push(`${half + rad * Math.cos(angle)},${half + rad * Math.sin(angle)}`);
      }
      return `${svgOpen}<polygon points="${points.join(' ')}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'pentagon': {
      const pts = [];
      for (let i = 0; i < 5; i++) {
        const angle = (i * 2 * Math.PI) / 5 - Math.PI / 2;
        pts.push(`${half + r * Math.cos(angle)},${half + r * Math.sin(angle)}`);
      }
      return `${svgOpen}<polygon points="${pts.join(' ')}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'hexagon': {
      const pts = [];
      for (let i = 0; i < 6; i++) {
        const angle = (i * 2 * Math.PI) / 6;
        pts.push(`${half + r * Math.cos(angle)},${half + r * Math.sin(angle)}`);
      }
      return `${svgOpen}<polygon points="${pts.join(' ')}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'heptagon': {
      const pts = [];
      for (let i = 0; i < 7; i++) {
        const angle = (i * 2 * Math.PI) / 7 - Math.PI / 2;
        pts.push(`${half + r * Math.cos(angle)},${half + r * Math.sin(angle)}`);
      }
      return `${svgOpen}<polygon points="${pts.join(' ')}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'octagon': {
      const pts = [];
      for (let i = 0; i < 8; i++) {
        const angle = (i * 2 * Math.PI) / 8 - Math.PI / 8;
        pts.push(`${half + r * Math.cos(angle)},${half + r * Math.sin(angle)}`);
      }
      return `${svgOpen}<polygon points="${pts.join(' ')}" fill="${color}" opacity="0.9"/>${svgClose}`;
    }

    case 'small-circle':
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${size * 0.2}" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'medium-circle':
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${size * 0.32}" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'large-circle':
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${r}" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'xlarge-circle':
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${half * 0.95}" fill="${color}" opacity="0.9"/>${svgClose}`;

    case 'line':
      return `${svgOpen}<line x1="4" y1="${half}" x2="${size-4}" y2="${half}" stroke="${color}" stroke-width="4" stroke-linecap="round" opacity="0.9"/>${svgClose}`;

    default:
      return `${svgOpen}<circle cx="${half}" cy="${half}" r="${r}" fill="${color}" opacity="0.5"/>${svgClose}`;
  }
}
