output
bash

python3 -c "
import math

# All geometry we need
r = 200  # SVG units for hull radius
cx, cy = 250, 250

# Dodecahedron face center vectors (normalized, then scaled)
# Standard dodecahedron face centers in spherical coords
phi = (1 + math.sqrt(5)) / 2  # golden ratio

# 12 face centers of dodecahedron
# Using the known face-center directions
faces = []

# Top cap
faces.append((0, 1, 0))

# Upper ring (5 faces)
for i in range(5):
    a = math.radians(72 * i)
    theta = math.radians(52.62)  # polar angle from top
    faces.append((math.sin(theta)*math.cos(a), math.cos(theta), math.sin(theta)*math.sin(a)))

# Lower ring (5 faces)  
for i in range(5):
    a = math.radians(72 * i + 36)
    theta = math.radians(127.38)
    faces.append((math.sin(theta)*math.cos(a), math.cos(theta), math.sin(theta)*math.sin(a)))

# Bottom cap
faces.append((0, -1, 0))

print('12 dodecahedron face centers (x,y,z normalized):')
for i, f in enumerate(faces):
    print(f'  {i+1:2d}: ({f[0]:6.3f}, {f[1]:6.3f}, {f[2]:6.3f})')

# Project to 2D for SVG (isometric-style)
def project(x, y, z, scale=170, cx=250, cy=250):
    # Simple perspective projection
    d = 4.0  # distance
    fac = d / (d - z*0.4)
    px = cx + x * scale * fac
    py = cy - y * scale * fac
    return px, py

print()
print('SVG projected positions:')
for i, f in enumerate(faces):
    px, py = project(*f)
    print(f'  {i+1:2d}: ({px:.1f}, {py:.1f})')
" 2>&1

output
json

{
  "returncode" : 0,
  "stdout" : "12 dodecahedron face centers (x,y,z normalized):\n   1: ( 0.000,  1.000,  0.000)\n   2: ( 0.795,  0.607,  0.000)\n   3: ( 0.246,  0.607,  0.756)\n   4: (-0.643,  0.607,  0.467)\n   5: (-0.643,  0.607, -0.467)\n   6: ( 0.246,  0.607, -0.756)\n   7: ( 0.643, -0.607,  0.467)\n   8: (-0.246, -0.607,  0.756)\n   9: (-0.795, -0.607,  0.000)\n  10: (-0.246, -0.607, -0.756)\n  11: ( 0.643, -0.607, -0.467)\n  12: ( 0.000, -1.000,  0.000)\n\nSVG projected positions:\n   1: (250.0, 80.0)\n   2: (385.1, 146.8)\n   3: (295.2, 138.4)\n   4: (135.4, 141.7)\n   5: (145.6, 151.4)\n   6: (288.8, 154.0)\n   7: (364.6, 358.3)\n   8: (204.8, 361.6)\n   9: (114.9, 353.2)\n  10: (211.2, 346.0)\n  11: (354.4, 348.6)\n  12: (250.0, 420.0)\n",
  "stderr" : ""
}

python3 << 'PYEOF'
import math

# Generate all SVG diagrams as strings we'll embed in HTML

phi = (1 + math.sqrt(5)) / 2

# 12 dodecahedron face centers
faces_3d = [
    (0.000,  1.000,  0.000),
    (0.795,  0.607,  0.000),
    (0.246,  0.607,  0.756),
    (-0.643, 0.607,  0.467),
    (-0.643, 0.607, -0.467),
    (0.246,  0.607, -0.756),
    (0.643, -0.607,  0.467),
    (-0.246,-0.607,  0.756),
    (-0.795,-0.607,  0.000),
    (-0.246,-0.607, -0.756),
    (0.643, -0.607, -0.467),
    (0.000, -1.000,  0.000),
]

def proj(x, y, z, scale=155, cx=260, cy=260):
    d = 4.5
    fac = d / (d - z * 0.38)
    px = cx + x * scale * fac
    py = cy - y * scale * fac
    sz = 0.5 + 0.5 * fac
    return px, py, sz

# ── DIAGRAM 1: Dodecahedral conduit layout ────────────────────────────────
def make_diagram1():
    W, H = 520, 520
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append('<rect width="100%" height="100%" fill="#0b1e36" rx="6"/>')
    
    # Title
    lines.append('<text x="260" y="28" text-anchor="middle" font-family="Arial" font-size="11" font-weight="800" fill="#64b4ff" letter-spacing="2">DODECAHEDRAL CONDUIT LAYOUT</text>')
    lines.append('<text x="260" y="44" text-anchor="middle" font-family="Arial" font-size="9" fill="rgba(255,255,255,0.45)">12 Through-Body Plasma Conduits — SD&amp;N F=12 Encoding</text>')
    
    # Draw hull circle
    lines.append('<circle cx="260" cy="275" r="195" fill="none" stroke="rgba(100,180,255,0.15)" stroke-width="1.5" stroke-dasharray="6,4"/>')
    lines.append('<circle cx="260" cy="275" r="185" fill="rgba(46,84,150,0.08)" stroke="rgba(100,180,255,0.35)" stroke-width="2"/>')
    
    # Draw conduits as lines through center
    proj_pts = []
    for f in faces_3d:
        px, py, sz = proj(f[0], f[1], f[2], scale=155, cx=260, cy=275)
        proj_pts.append((px, py, sz, f[2]))
    
    # Sort by z for depth
    indexed = [(i, p) for i, p in enumerate(proj_pts)]
    
    # Draw conduit lines (from face center to opposite face center through plenum)
    drawn = set()
    for i, (px, py, sz, fz) in indexed:
        opp = (i + 6) % 12
        if (min(i,opp), max(i,opp)) not in drawn:
            drawn.add((min(i,opp), max(i,opp)))
            ox, oy = proj_pts[opp][0], proj_pts[opp][1]
            alpha = 0.25 if fz < 0 else 0.55
            lines.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{ox:.1f}" y2="{oy:.1f}" stroke="rgba(100,180,255,{alpha})" stroke-width="2.5"/>')
    
    # Draw central plenum
    lines.append('<circle cx="260" cy="275" r="22" fill="#0b1e36" stroke="#64b4ff" stroke-width="2.5"/>')
    lines.append('<circle cx="260" cy="275" r="14" fill="rgba(100,180,255,0.3)"/>')
    lines.append('<text x="260" y="279" text-anchor="middle" font-family="Arial" font-size="8" font-weight="800" fill="#64b4ff">PLENUM</text>')
    
    # Draw conduit endpoints
    labels = ['C01','C02','C03','C04','C05','C06','C07','C08','C09','C10','C11','C12']
    for i, (px, py, sz, fz) in enumerate(proj_pts):
        vis = fz >= 0
        fill = '#64b4ff' if vis else 'rgba(100,180,255,0.4)'
        stroke = '#fff' if vis else 'rgba(255,255,255,0.3)'
        r = 10 * sz
        lines.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        # Label offset
        dx = px - 260; dy = py - 275
        mag = math.sqrt(dx*dx+dy*dy) or 1
        lx = px + dx/mag * (r + 14)
        ly = py + dy/mag * (r + 14)
        col = '#ffffff' if vis else 'rgba(255,255,255,0.4)'
        lines.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" font-family="Arial" font-size="8" font-weight="700" fill="{col}" dominant-baseline="middle">{labels[i]}</text>')
    
    # Legend
    lines.append('<text x="20" y="485" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.6)">● Visible conduit port (front hemisphere)  ● Hidden port (rear hemisphere)</text>')
    lines.append('<text x="20" y="500" font-family="Arial" font-size="8.5" fill="#64b4ff">SD&amp;N: F=12 Faces → V=20 Gate Nodes → E=30 Structural Paths  |  φ=8.0  |  Euler: F-E+V=2 ✓</text>')
    
    lines.append('</svg>')
    return '\n'.join(lines)

# ── DIAGRAM 2: Cross-section with plasma flow ─────────────────────────────
def make_diagram2():
    W, H = 520, 480
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append('<rect width="100%" height="100%" fill="#0b1e36" rx="6"/>')
    
    lines.append('<text x="260" y="28" text-anchor="middle" font-family="Arial" font-size="11" font-weight="800" fill="#64b4ff" letter-spacing="2">PLASMA FLOW CROSS-SECTION</text>')
    lines.append('<text x="260" y="44" text-anchor="middle" font-family="Arial" font-size="9" fill="rgba(255,255,255,0.45)">Central Plenum Manifold — Pressure Equalization Architecture</text>')

    cx, cy = 260, 255
    R = 170  # hull radius

    # Hull outer
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(100,180,255,0.5)" stroke-width="3"/>')
    # Hull inner skin
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{R-12}" fill="none" stroke="rgba(100,180,255,0.2)" stroke-width="8" stroke-dasharray="none"/>')
    # Hull label
    lines.append(f'<text x="{cx+R+8}" y="{cy}" font-family="Arial" font-size="8" fill="rgba(255,255,255,0.6)" dominant-baseline="middle">Spherical hull</text>')

    # Conduit paths - show 4 conduits in cross section (top/bottom/left/right)
    conduit_dirs = [(0,-1),(0,1),(-1,0),(1,0)]
    conduit_labels = ['C01\n(Top)', 'C12\n(Bottom)', 'C09\n(Left)', 'C02\n(Right)']
    colors_plasma = ['#ff6644','#ff8833','#ffaa22','#ff5533']
    
    for i, (dx, dy) in enumerate(conduit_dirs):
        # Conduit walls
        perp_x, perp_y = -dy, dx
        w = 12
        x1a = cx + dx*(R-12) + perp_x*w
        y1a = cy + dy*(R-12) + perp_y*w
        x1b = cx + dx*(R-12) - perp_x*w
        y1b = cy + dy*(R-12) - perp_y*w
        x2a = cx - dx*(R-12) + perp_x*w
        y2a = cy - dy*(R-12) + perp_y*w
        x2b = cx - dx*(R-12) - perp_x*w
        y2b = cy - dy*(R-12) - perp_y*w
        
        # Conduit bore
        lines.append(f'<line x1="{x1a:.1f}" y1="{y1a:.1f}" x2="{x2a:.1f}" y2="{y2a:.1f}" stroke="rgba(100,180,255,0.4)" stroke-width="1.5"/>')
        lines.append(f'<line x1="{x1b:.1f}" y1="{y1b:.1f}" x2="{x2b:.1f}" y2="{y2b:.1f}" stroke="rgba(100,180,255,0.4)" stroke-width="1.5"/>')
        
        # Plasma flow arrows (from gate toward plenum)
        col = colors_plasma[i]
        # Show flow from one side only (gate open side)
        sx = cx + dx * (R-15)
        sy = cy + dy * (R-15)
        ex = cx + dx * 30
        ey = cy + dy * 30
        lines.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{col}" stroke-width="4" stroke-dasharray="8,4" opacity="0.8"/>')
        # Arrowhead
        ax = ex - dx*8 + perp_x*5
        ay = ey - dy*8 + perp_y*5
        bx = ex - dx*8 - perp_x*5
        by = ey - dy*8 - perp_y*5
        lines.append(f'<polygon points="{ex:.0f},{ey:.0f} {ax:.0f},{ay:.0f} {bx:.0f},{by:.0f}" fill="{col}" opacity="0.9"/>')
        
        # Port label
        lx = cx + dx * (R + 22)
        ly = cy + dy * (R + 22)
        lbl = conduit_labels[i].replace('\n', ' ')
        lines.append(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="700" fill="#64b4ff" dominant-baseline="middle">{lbl}</text>')

    # Magnetic flux gate symbols at exit ports
    for dx, dy in conduit_dirs:
        gx = cx + dx * (R - 20)
        gy = cy + dy * (R - 20)
        lines.append(f'<rect x="{gx-10:.0f}" y="{gy-10:.0f}" width="20" height="20" fill="rgba(255,180,0,0.2)" stroke="#ffb300" stroke-width="1.5" rx="2"/>')
        lines.append(f'<text x="{gx:.0f}" y="{gy:.0f}" text-anchor="middle" font-family="Arial" font-size="7" font-weight="800" fill="#ffb300" dominant-baseline="middle">GATE</text>')

    # Central Plenum
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="38" fill="rgba(255,80,30,0.15)" stroke="#ff6644" stroke-width="2.5"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="rgba(255,80,30,0.3)"/>')
    lines.append(f'<text x="{cx}" y="{cy-5}" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="800" fill="#ff9977" dominant-baseline="middle">CENTRAL</text>')
    lines.append(f'<text x="{cx}" y="{cy+7}" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="800" fill="#ff9977" dominant-baseline="middle">PLENUM</text>')

    # Toroidal tank region
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{R-25}" fill="none" stroke="rgba(100,200,100,0.3)" stroke-width="6" stroke-dasharray="12,6"/>')
    lines.append(f'<text x="{cx+85}" y="{cy-90}" font-family="Arial" font-size="8" fill="rgba(100,200,100,0.7)">Toroidal</text>')
    lines.append(f'<text x="{cx+85}" y="{cy-80}" font-family="Arial" font-size="8" fill="rgba(100,200,100,0.7)">propellant tank</text>')

    # Legend
    lines.append(f'<rect x="20" y="440" width="12" height="4" fill="#ff6644" rx="2"/>')
    lines.append(f'<text x="36" y="447" font-family="Arial" font-size="8" fill="rgba(255,255,255,0.6)">Plasma flow (gate OPEN)</text>')
    lines.append(f'<rect x="180" y="440" width="12" height="12" fill="none" stroke="#ffb300" stroke-width="1.5" rx="1"/>')
    lines.append(f'<text x="196" y="447" font-family="Arial" font-size="8" fill="rgba(255,255,255,0.6)">Magnetic flux gate</text>')
    lines.append(f'<line x1="340" y1="443" x2="360" y2="443" stroke="rgba(100,200,100,0.7)" stroke-width="4" stroke-dasharray="6,3"/>')
    lines.append(f'<text x="364" y="447" font-family="Arial" font-size="8" fill="rgba(255,255,255,0.6)">Propellant tank boundary</text>')

    lines.append('</svg>')
    return '\n'.join(lines)

# ── DIAGRAM 3: Thrust vector states ───────────────────────────────────────
def make_diagram3():
    W, H = 520, 380
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append('<rect width="100%" height="100%" fill="#0b1e36" rx="6"/>')
    
    lines.append('<text x="260" y="28" text-anchor="middle" font-family="Arial" font-size="11" font-weight="800" fill="#64b4ff" letter-spacing="2">THRUST VECTOR AUTHORITY — 360°</text>')
    lines.append('<text x="260" y="44" text-anchor="middle" font-family="Arial" font-size="9" fill="rgba(255,255,255,0.45)">Gate configurations: 2¹² = 4,096 discrete states | Angular resolution: 5.81°</text>')

    # Show 4 example configurations
    configs = [
        ("FORWARD BURN", [(0,-1,1.0)], "#64b4ff"),
        ("LATERAL MANEUVER", [(-1,0,1.0),(0.3,-0.9,0.6)], "#44ff88"),
        ("ATTITUDE CONTROL", [(-0.7,-0.7,0.5),(0.7,-0.7,0.5)], "#ffaa22"),
        ("RETROGRADE BRAKE", [(0,1,1.0),(-0.5,0.8,0.7),(0.5,0.8,0.7)], "#ff6644"),
    ]

    cols = 2
    for idx, (label, vectors, col) in enumerate(configs):
        col_i = idx % cols
        row_i = idx // cols
        bx = 60 + col_i * 230
        by = 80 + row_i * 160
        R = 52

        # Mini hull
        lines.append(f'<circle cx="{bx}" cy="{by}" r="{R}" fill="rgba(46,84,150,0.15)" stroke="rgba(100,180,255,0.4)" stroke-width="1.5"/>')
        
        # Conduit dots (simplified 8-point ring)
        for j in range(12):
            a = math.radians(j * 30)
            dx = math.cos(a); dy = math.sin(a)
            px = bx + dx * R
            py = by + dy * R
            lines.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="rgba(100,180,255,0.5)"/>')

        # Net thrust vector
        for vx, vy, mag in vectors:
            ex = bx + vx * R * 0.85 * mag
            ey = by + vy * R * 0.85 * mag
            lines.append(f'<line x1="{bx}" y1="{by}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{col}" stroke-width="3.5"/>')
            ax = ex - vx*8 + (-vy)*5
            ay = ey - vy*8 + vx*5
            bax = ex - vx*8 - (-vy)*5
            bay = ey - vy*8 - vx*5
            lines.append(f'<polygon points="{ex:.0f},{ey:.0f} {ax:.0f},{ay:.0f} {bax:.0f},{bay:.0f}" fill="{col}"/>')

        # Label
        lines.append(f'<text x="{bx}" y="{by+R+18}" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="800" fill="{col}">{label}</text>')
# Summary stats
    lines.append('<rect x="20" y="320" width="480" height="48" fill="rgba(100,180,255,0.08)" rx="3" stroke="rgba(100,180,255,0.2)" stroke-width="1"/>')
    lines.append('<text x="30" y="338" font-family="Arial" font-size="9" font-weight="800" fill="#64b4ff">VECTOR PERFORMANCE</text>')
    lines.append('<text x="30" y="353" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.7)">Discrete states: 4,096  |  Gate response: &lt;500 µs  |  Max slew: &lt;1 ms  |  Mechanical actuators: 0  |  Failure threshold: 9/12 conduits</text>')
    lines.append('<text x="30" y="364" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.5)">All vectors computed by Dynamic Distribution Algorithm from SD&amp;N V=20 gate node graph</text>')

    lines.append('</svg>')
    return '\n'.join(lines)

# ── DIAGRAM 4: Gate state schematic ───────────────────────────────────────
def make_diagram4():
    W, H = 520, 300
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append('<rect width="100%" height="100%" fill="#0b1e36" rx="6"/>')
    
    lines.append('<text x="260" y="25" text-anchor="middle" font-family="Arial" font-size="11" font-weight="800" fill="#64b4ff" letter-spacing="2">MAGNETIC FLUX GATE — FOUR STATES</text>')

    states = [
        ("CLOSED\n(Pinch)", "#ff4444", "Maximum field\nPlasma pinched\nNo thrust", [(0,0,0,60,'solid'),(0,60,0,0,'solid')]),
        ("OPEN\n(Full)", "#44ff88", "Field modulated\nFull plasma flow\nMax thrust", [(0,0,0,60,'flow')]),
        ("THROTTLE\n(Variable)", "#ffaa22", "0–100% in\n256 steps\nVariable thrust", [(0,0,0,60,'partial')]),
        ("EMERGENCY\n(Fail-Close)", "#ff8800", "Power loss →\nAuto pinch\n&lt;1 µs", [(0,0,0,60,'emerg')]),
    ]

    for i, (name, col, desc, _) in enumerate(states):
        bx = 65 + i * 100
        by = 140
        w, h = 60, 80

        # Conduit background
        lines.append(f'<rect x="{bx-w//2}" y="{by-h//2}" width="{w}" height="{h}" fill="rgba(0,0,0,0.4)" rx="4" stroke="rgba(100,180,255,0.3)" stroke-width="1.5"/>')
        
        # Gate symbol in middle
        gx, gy = bx, by
        
        if 'CLOSED' in name or 'EMERGENCY' in name:
            # Closed gate - crossed lines
            lines.append(f'<rect x="{gx-18}" y="{gy-8}" width="36" height="16" fill="{col}" opacity="0.3" rx="3"/>')
            lines.append(f'<line x1="{gx-15}" y1="{gy-5}" x2="{gx+15}" y2="{gy+5}" stroke="{col}" stroke-width="2.5"/>')
            lines.append(f'<line x1="{gx-15}" y1="{gy+5}" x2="{gx+15}" y2="{gy-5}" stroke="{col}" stroke-width="2.5"/>')
            # Blocked flow
            lines.append(f'<line x1="{bx}" y1="{by-40}" x2="{bx}" y2="{by-12}" stroke="rgba(100,180,255,0.3)" stroke-width="5" stroke-dasharray="4,3"/>')
        elif 'OPEN' in name:
            # Open gate - flowing
            lines.append(f'<rect x="{gx-18}" y="{gy-6}" width="36" height="12" fill="rgba(68,255,136,0.15)" rx="3" stroke="{col}" stroke-width="1.5"/>')
            for offset in [-6, 0, 6]:
                lines.append(f'<line x1="{bx}" y1="{by-40}" x2="{bx}" y2="{by+40}" stroke="{col}" stroke-width="4" opacity="0.7" stroke-dasharray="8,3"/>')
                break
            lines.append(f'<line x1="{bx}" y1="{by-40}" x2="{bx}" y2="{by+40}" stroke="{col}" stroke-width="5" opacity="0.6" stroke-dasharray="6,3"/>')
        else:
            # Throttle
            lines.append(f'<rect x="{gx-18}" y="{gy-6}" width="36" height="12" fill="rgba(255,170,34,0.15)" rx="3" stroke="{col}" stroke-width="1.5"/>')
            lines.append(f'<line x1="{bx}" y1="{by-40}" x2="{bx}" y2="{by-12}" stroke="{col}" stroke-width="3" opacity="0.6" stroke-dasharray="5,4"/>')
            lines.append(f'<line x1="{bx}" y1="{by+12}" x2="{bx}" y2="{by+40}" stroke="{col}" stroke-width="3" opacity="0.6" stroke-dasharray="5,4"/>')

        # State name
        name_clean = name.replace('\n', ' ')
        lines.append(f'<text x="{bx}" y="{by-52}" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="800" fill="{col}">{name_clean}</text>')
        
        # Description
        for j, dl in enumerate(desc.split('\n')):
            lines.append(f'<text x="{bx}" y="{by+58+j*13}" text-anchor="middle" font-family="Arial" font-size="7.5" fill="rgba(255,255,255,0.6)">{dl}</text>')

    # Response time bar
    lines.append('<text x="260" y="278" text-anchor="middle" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.5)">All state transitions: &lt;500 µs  |  Emergency fail-close: &lt;1 µs  |  No mechanical latency  |  Radiation-hardened fiber-optic control bus</text>')

    lines.append('</svg>')
    return '\n'.join(lines)

# ── DIAGRAM 5: SD&N encoding table visual ──────────────────────────────────
def make_diagram5():
    W, H = 520, 260
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    lines.append('<rect width="100%" height="100%" fill="#0b1e36" rx="6"/>')
    lines.append('<text x="260" y="25" text-anchor="middle" font-family="Arial" font-size="11" font-weight="800" fill="#64b4ff" letter-spacing="2">SD&amp;N DIMENSIONAL ENCODING — SHARONCARE1</text>')

    # Three columns: F V E
    cols_data = [
        ("F = 12", "FACES", "12 plasma conduits", "3D Propulsion State", "#64b4ff"),
        ("V = 20", "VERTICES", "20 gate control nodes", "4D Control State", "#ffaa22"),
        ("E = 30", "EDGES", "30 structural paths", "5D Stability Encoding", "#44ff88"),
    ]

    for i, (val, name, desc, dim, col) in enumerate(cols_data):
        bx = 86 + i * 116
        # Card
        lines.append(f'<rect x="{bx-56}" y="42" width="112" height="155" fill="rgba(255,255,255,0.04)" rx="4" stroke="{col}" stroke-width="1.5" opacity="0.8"/>')
        # Big number
        lines.append(f'<text x="{bx}" y="90" text-anchor="middle" font-family="Arial" font-size="32" font-weight="900" fill="{col}">{val}</text>')
        lines.append(f'<text x="{bx}" y="108" text-anchor="middle" font-family="Arial" font-size="8.5" font-weight="800" fill="{col}" letter-spacing="2">{name}</text>')
        # Separator
        lines.append(f'<line x1="{bx-40}" y1="118" x2="{bx+40}" y2="118" stroke="{col}" stroke-width="0.8" opacity="0.4"/>')
        # Physical meaning
        lines.append(f'<text x="{bx}" y="136" text-anchor="middle" font-family="Arial" font-size="9" fill="rgba(255,255,255,0.8)">{desc}</text>')
        # Dimensional label
        lines.append(f'<text x="{bx}" y="176" text-anchor="middle" font-family="Arial" font-size="8" fill="{col}" opacity="0.8">{dim}</text>')

    # Connecting arrows
    for bx in [86+116-14, 86+116*2-14]:
        lines.append(f'<text x="{bx+14}" y="125" text-anchor="middle" font-family="Arial" font-size="18" fill="rgba(255,255,255,0.2)">→</text>')

    # Bottom stats
    lines.append('<rect x="20" y="210" width="480" height="40" fill="rgba(100,180,255,0.06)" rx="3"/>')
    lines.append('<text x="260" y="226" text-anchor="middle" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.7)">Euler check: F − E + V = 12 − 30 + 20 = 2  ✓ &nbsp;|&nbsp; Shape factor φ = (F×V)/E = 8.000  &nbsp;|&nbsp; Phase factor = 2π/62 = 5.81°</text>')
    lines.append('<text x="260" y="242" text-anchor="middle" font-family="Arial" font-size="8.5" fill="rgba(255,255,255,0.5)">Dodecahedron ↔ Icosahedron dual pair: shared E=30 → identical 5D stability encoding  ✓</text>')

    lines.append('</svg>')
    return '\n'.join(lines)

# Write all diagrams
d1 = make_diagram1()
d2 = make_diagram2()
d3 = make_diagram3()
d4 = make_diagram4()
d5 = make_diagram5()

# Save as data files
with open('/tmp/diag1.svg','w') as f: f.write(d1)
with open('/tmp/diag2.svg','w') as f: f.write(d2)
with open('/tmp/diag3.svg','w') as f: f.write(d3)
with open('/tmp/diag4.svg','w') as f: f.write(d4)
with open('/tmp/diag5.svg','w') as f: f.write(d5)

print("All 5 diagrams generated successfully")
PYEOF
output
json
{
  "returncode" : 0,
  "stdout" : "All 5 diagrams generated successfully\n",
  "stderr" : ""
}
