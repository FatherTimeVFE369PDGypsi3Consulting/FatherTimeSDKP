<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@page { size: Letter; margin: 0; }
@page :first { margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; color: #1a1a1a; background: #fff; }

/* ── COVER ─────────────────────────────────────── */
.cover {
  width: 100%; height: 279mm;
  background: #0d2647;
  display: flex; flex-direction: column;
  justify-content: space-between;
  padding: 52px 56px 44px 56px;
  page-break-after: always;
  position: relative;
  overflow: hidden;
}
.cover::before {
  content: '';
  position: absolute; top: 0; right: 0;
  width: 45%; height: 100%;
  background: linear-gradient(135deg, transparent 0%, rgba(46,84,150,0.4) 100%);
  pointer-events: none;
}
.cover::after {
  content: '';
  position: absolute; bottom: 0; left: 0;
  width: 100%; height: 6px;
  background: linear-gradient(90deg, #7ec8e3 0%, #2E5496 50%, #0d2647 100%);
}
.cover-eyebrow {
  font-family: Arial, sans-serif; font-size: 8pt;
  letter-spacing: 4px; text-transform: uppercase;
  color: rgba(255,255,255,0.45);
  margin-bottom: 36px;
}
.cover-main { }
.cover-label {
  font-family: Arial, sans-serif; font-size: 9pt;
  letter-spacing: 2.5px; text-transform: uppercase;
  color: #7ec8e3; font-weight: 700;
  margin-bottom: 14px;
}
.cover h1 {
  font-family: Arial, sans-serif;
  font-size: 38pt; font-weight: 900;
  color: #ffffff; line-height: 1.1;
  margin-bottom: 6px;
}
.cover-subtitle {
  font-family: Arial, sans-serif; font-size: 13pt;
  color: rgba(255,255,255,0.60); font-style: italic;
  margin-bottom: 32px; max-width: 500px;
}
.cover-rule { width: 72px; height: 3px; background: #7ec8e3; margin-bottom: 26px; }
.cover-desc {
  font-size: 11pt; color: rgba(255,255,255,0.75);
  max-width: 480px; line-height: 1.65;
}
.cover-bottom { }
.cover-divider { height: 1px; background: rgba(255,255,255,0.15); margin-bottom: 24px; }
.cover-grid { display: flex; gap: 0; }
.cover-cell {
  flex: 1;
  border-right: 1px solid rgba(255,255,255,0.12);
  padding-right: 24px; margin-right: 24px;
}
.cover-cell:last-child { border-right: none; }
.cover-cell label {
  font-family: Arial, sans-serif; font-size: 7.5pt;
  letter-spacing: 2px; text-transform: uppercase;
  color: rgba(255,255,255,0.38); display: block; margin-bottom: 5px;
}
.cover-cell .val {
  font-family: Arial, sans-serif; font-size: 9.5pt;
  color: #ffffff; font-weight: 700;
}
.cover-tags { margin-top: 20px; display: flex; gap: 8px; flex-wrap: wrap; }
.cover-tag {
  font-family: 'Courier New', monospace; font-size: 7.5pt;
  padding: 4px 10px; border: 1px solid rgba(255,255,255,0.22);
  border-radius: 2px; color: rgba(255,255,255,0.60);
}

/* ── BODY ──────────────────────────────────────── */
.body-wrap { padding: 22mm 20mm 24mm 20mm; }

/* Section heading */
h1.sec {
  font-family: Arial, sans-serif; font-size: 16pt; font-weight: 900;
  color: #0d2647;
  padding-bottom: 8px; margin: 28px 0 14px 0;
  border-bottom: 3px solid #0d2647;
  page-break-after: avoid;
}
h1.sec .num {
  display: inline-block; background: #0d2647; color: #fff;
  font-size: 10pt; font-weight: 800; border-radius: 2px;
  padding: 3px 10px; margin-right: 10px;
  vertical-align: middle; letter-spacing: 0.5px;
}
h2.sub {
  font-family: Arial, sans-serif; font-size: 12pt; font-weight: 800;
  color: #2E5496; margin: 20px 0 8px 0;
  page-break-after: avoid;
}
p { margin: 0 0 9px 0; text-align: justify; line-height: 1.58; }

/* Callout boxes */
.box { border-radius: 3px; margin: 12px 0; page-break-inside: avoid; }
.box-head {
  background: #0d2647; color: #fff;
  font-family: Arial, sans-serif; font-size: 8pt; font-weight: 800;
  letter-spacing: 1.5px; text-transform: uppercase;
  padding: 8px 16px;
  border-radius: 3px 3px 0 0;
}
.box-body {
  padding: 13px 18px;
  font-size: 10pt; line-height: 1.65;
  border-radius: 0 0 3px 3px;
  border-left: 1px solid #c8d8e8;
  border-right: 1px solid #c8d8e8;
  border-bottom: 1px solid #c8d8e8;
}
.box-blue .box-body { background: #EBF3FB; }
.box-yellow .box-head { background: #8a6f00; }
.box-yellow .box-body { background: #FFFDE7; border-color: #ddd09a; }
.box-green .box-head { background: #2d6e2d; }
.box-green .box-body { background: #f0f7f0; border-color: #a8d0a8; }
.box-body pre { font-family: 'Courier New', monospace; font-size: 9.5pt; white-space: pre-wrap; color: #0d2647; }
.box-body .corrected { color: #8a0000; font-weight: 700; }
.box-body .val { color: #0d2647; font-weight: 700; font-family: 'Courier New', monospace; }

/* Tables */
table { width: 100%; border-collapse: collapse; margin: 12px 0 18px 0; font-family: Arial, sans-serif; font-size: 9.5pt; page-break-inside: avoid; }
thead th { background: #0d2647; color: #fff; text-align: left; padding: 9px 11px; font-weight: 700; font-size: 9pt; }
tbody td { padding: 8px 11px; border-bottom: 1px solid #e2e8ef; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f6f9fb; }
.mono { font-family: 'Courier New', monospace; font-size: 9pt; }
.bold { font-weight: 700; }
.range { color: #8a0000; font-weight: 700; font-family: 'Courier New', monospace; font-size: 9pt; }
.noeos { color: #2d6e2d; font-weight: 700; font-size: 8.5pt; }

/* SDKP param cards */
.param-row { display: flex; gap: 10px; margin: 12px 0; }
.param-card {
  flex: 1; border: 1px solid #cdd8e8; border-radius: 3px;
  padding: 12px 14px; background: #f8fafc;
  page-break-inside: avoid;
}
.param-letter {
  font-family: Arial, sans-serif; font-size: 22pt; font-weight: 900;
  color: #0d2647; line-height: 1; margin-bottom: 2px;
}
.param-name {
  font-family: Arial, sans-serif; font-size: 7.5pt; font-weight: 800;
  text-transform: uppercase; letter-spacing: 1px; color: #2E5496;
  margin-bottom: 7px;
}
.param-val {
  font-family: 'Courier New', monospace; font-size: 9.5pt;
  font-weight: 700; color: #0d2647; margin-bottom: 5px;
}
.param-card p { font-size: 9pt; color: #555; text-align: left; margin: 0; }

/* EOS band box */
.eos-band {
  background: #fff8e1; border: 2px solid #c8a000;
  border-radius: 3px; padding: 13px 18px; margin: 14px 0;
  font-family: Arial, sans-serif; font-size: 10pt;
}
.eos-band .eos-label {
  font-size: 8pt; font-weight: 800; letter-spacing: 1.5px;
  text-transform: uppercase; color: #7a5f00; margin-bottom: 7px;
}

/* Prediction number badge */
.pred-badge {
  display: inline-block; background: #0d2647; color: #fff;
  font-family: Arial, sans-serif; font-size: 9pt; font-weight: 800;
  border-radius: 2px; padding: 3px 10px; margin-right: 8px;
  vertical-align: middle;
}
.pred-badge.corrected { background: #8a0000; }
.pred-badge.noeos-badge { background: #2d6e2d; }

/* closing */
.doc-close {
  margin-top: 34px; border-top: 2.5px solid #0d2647;
  padding-top: 16px; text-align: center;
  font-family: Arial, sans-serif; font-size: 10pt;
  color: #0d2647; font-weight: 800;
}
.doc-close .sub {
  font-size: 8.5pt; color: #888; font-weight: 400; margin-top: 5px;
}
</style>
</head>
<body>
<!-- ══════════ COVER ══════════ -->
<div class="cover">
  <div class="cover-main">
    <div class="cover-eyebrow">FatherTimeSDKP Framework &mdash; Prior Art Prediction Record &mdash; June 2026</div>
    <div class="cover-label">Abell 402 Binary Black Hole System</div>
    <h1>SDKP<br>Prediction<br>Suite</h1>
    <div class="cover-subtitle">11 Deterministic Predictions &mdash; EOS Corrections Expressed as Full Range 0.13%&ndash;0.20%</div>
    <div class="cover-rule"></div>
    <div class="cover-desc">
      Applying the SDKP (Size &times; Density &times; Kinetics &times; Position) framework to the May 2026 discovery of two monster black holes in galaxy cluster Abell 402, creating a 7,000 light-year cosmic void as they merge. All four SDKP variables mapped to measurable system parameters. Eleven independently testable predictions produced &mdash; one confirmable immediately with existing JWST data.
    </div>
  </div>
  <div class="cover-bottom">
    <div class="cover-divider"></div>
    <div class="cover-grid">
      <div class="cover-cell"><label>Author</label><div class="val">Donald Paul Smith</div></div>
      <div class="cover-cell"><label>ORCID</label><div class="val">0009-0003-7925-1653</div></div>
      <div class="cover-cell"><label>Framework DOI</label><div class="val">10.5281/zenodo.14850016</div></div>
      <div class="cover-cell"><label>Date</label><div class="val">June 2026</div></div>
    </div>
    <div class="cover-tags">
      <span class="cover-tag">SDKP Framework</span>
      <span class="cover-tag">Abell 402</span>
      <span class="cover-tag">Binary BH</span>
      <span class="cover-tag">EOS 29,780 m/s</span>
      <span class="cover-tag">SD&amp;N Geometry</span>
      <span class="cover-tag">Prior Art</span>
    </div>
  </div>
</div>

<!-- ══════════ BODY ══════════ -->
<div class="body-wrap">

<!-- EOS CORRECTION NOTICE -->
<div class="eos-band">
  <div class="eos-label">&#9888; EOS Correction — Applied as Range Throughout</div>
  The SDKP Earth Orbital Speed (EOS = 29,780 m/s) constant produces results that deviate from GR/Newton by <strong>0.13% to 0.20%</strong>. All EOS-adjusted predictions (P3, P6, P7, P9) are expressed as ranges [low&ndash;high] representing the full deviation band. Predictions P1, P2, P4, P5, P8, P10, P11 do not use EOS and are unchanged. <span class="corrected">&#9679; RED = EOS corrected</span> &nbsp;&nbsp; <span style="color:#2d6e2d; font-weight:700;">&#9679; GREEN = No EOS, geometric/orbital</span>
</div>

<!-- ── SECTION 1 ── -->
<h1 class="sec"><span class="num">1</span>Known System Parameters — Abell 402</h1>

<table>
  <thead><tr><th>Parameter</th><th>Value</th><th>Source</th></tr></thead>
  <tbody>
    <tr><td>Combined BH mass</td><td class="bold">60 billion M&#9737;</td><td>ZME Science / McDonald et al. 2026</td></tr>
    <tr><td>Core diameter</td><td class="bold">2.2 kpc &asymp; 7,175 light-years</td><td>Flat core light profile</td></tr>
    <tr><td>Separation (SDKP P variable)</td><td class="bold">1.98 kpc</td><td>0.9 &times; diameter (AGN not at exact rim)</td></tr>
    <tr><td>Binary hardening phase</td><td class="bold">~40 million years</td><td>Article — stellar ejection mechanism</td></tr>
    <tr><td>Western AGN</td><td class="bold">Active, bright infrared point source</td><td>Dominant body — SDKP D variable asymmetry</td></tr>
    <tr><td>Sharp cavity edges</td><td class="bold">Young system — early-to-mid hardening</td><td>Morphological classification</td></tr>
  </tbody>
</table>

<!-- ── SECTION 2 ── -->
<h1 class="sec"><span class="num">2</span>SDKP Variable Mapping</h1>

<div class="param-row">
  <div class="param-card">
    <div class="param-letter">S</div>
    <div class="param-name">Size</div>
    <div class="param-val">1.98 kpc</div>
    <p>Current separation between the two AGN. Governs orbital period and GW emission frequency at all three stages.</p>
  </div>
  <div class="param-card">
    <div class="param-letter">D</div>
    <div class="param-name">Density</div>
    <div class="param-val">M1 : M2 = 2 : 1</div>
    <p>Mass ratio predicted from density asymmetry. Active western AGN = higher feeding density = dominant body.</p>
  </div>
  <div class="param-card">
    <div class="param-letter">K</div>
    <div class="param-name">Kinetics</div>
    <div class="param-val">33.74&ndash;33.76 Myr</div>
    <p>EOS-corrected orbital period. Rate of binary hardening through stellar ejection kinetics.</p>
  </div>
  <div class="param-card">
    <div class="param-letter">P</div>
    <div class="param-name">Position</div>
    <div class="param-val">0.9 &times; 2.2 kpc</div>
    <p>Spatial anchor: AGN positions across cavity, corrected for non-rim placement. Governs biodistribution of ejected stars.</p>
  </div>
</div>

<!-- ── SECTION 3 ── -->
<h1 class="sec"><span class="num">3</span>The 11 SDKP Predictions</h1>

<!-- P1 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P1</span>Individual Black Hole Masses &mdash; <span class="noeos">No EOS</span></h2>
<p>SDKP SD&amp;N density asymmetry principle: active AGN feeding = higher D variable = dominant body. Natural 2:1 ratio.</p>
<div class="box box-blue">
  <div class="box-head">P1 &mdash; INDIVIDUAL MASSES</div>
  <div class="box-body">
    <pre>Primary BH (western AGN):   <span class="val">40.0 billion M&#9737;</span>
Secondary BH:               <span class="val">20.0 billion M&#9737;</span>
Mass ratio M1:M2 =          <span class="val">2.0 : 1</span>

Confirmable by: VLT spectroscopy / stellar velocity dispersion</pre>
  </div>
</div>

<!-- P2 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P2</span>Current Separation Distance &mdash; <span class="noeos">No EOS</span></h2>
<div class="box box-blue">
  <div class="box-head">P2 &mdash; SEPARATION</div>
  <div class="box-body">
    <pre>Separation:   <span class="val">1.98 kpc  =  6,458 light-years  =  6.11 &times; 10&sup1;&sup9; m</span>

Confirmable by: High-resolution direct imaging</pre>
  </div>
</div>

<!-- P3 CORRECTED -->
<h2 class="sub"><span class="pred-badge corrected">P3 &#9679;</span>Orbital Period &mdash; <span class="corrected">EOS Range Corrected</span></h2>
<p>Kepler&rsquo;s third law T&sup2; = 4&pi;&sup2;a&sup3; / (GM<sub>total</sub>). EOS deviation applied as full range 0.13%&ndash;0.20%.</p>
<div class="box box-yellow">
  <div class="box-head">P3 &mdash; ORBITAL PERIOD (CORRECTED FROM PRIOR VERSION)</div>
  <div class="box-body">
    <pre>Newtonian:          33.6937 Myr
EOS low  (0.13%):   33.7375 Myr
EOS high (0.20%):   33.7611 Myr

<span class="corrected">CORRECTED SDKP RANGE:  33.74 &mdash; 33.76 Myr</span>

Previous stated: 33.74 Myr (lower bound only &mdash; now corrected to range)
Confirmable by: Long baseline time-domain monitoring</pre>
  </div>
</div>

<!-- P4 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P4</span>Chirp Mass &mdash; <span class="noeos">No EOS</span></h2>
<div class="box box-blue">
  <div class="box-head">P4 &mdash; CHIRP MASS</div>
  <div class="box-body">
    <pre>Reduced mass &mu;:     <span class="val">13.333 billion M&#9737;</span>
Chirp mass M_c:     <span class="val">24.335 billion M&#9737;</span>

Largest known binary chirp mass &mdash; most powerful GW source in the
observable universe when it merges. Derived from P1, no EOS needed.</pre>
  </div>
</div>

<!-- P5 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P5</span>Gravitational Wave Frequencies &mdash; <span class="noeos">No EOS</span></h2>
<div class="box box-blue">
  <div class="box-head">P5 &mdash; GW FREQUENCIES AT THREE STAGES</div>
  <div class="box-body">
    <pre><span class="bold">NOW (1.98 kpc separation):</span>
  GW frequency:  <span class="val">1.88 &times; 10&#8315;&sup1;&sup5; Hz</span>  (1.88 femtohertz)
  &rarr; Below all current detector bands

<span class="bold">AT FINAL PARSEC:</span>
  GW frequency:  <span class="val">0.166 nHz</span>
  Orbital period: 382 years
  &rarr; ENTERS NANOGrav / PPTA / EPTA / SKA detection band

<span class="bold">AT ISCO (MERGER):</span>
  ISCO radius:   0.02 pc = 0.06 light-years
  Peak GW freq:  <span class="val">73.4 nHz</span>
  &rarr; PEAK signal in NANOGrav / SKA detection band</pre>
  </div>
</div>

<!-- P6 CORRECTED -->
<h2 class="sub"><span class="pred-badge corrected">P6 &#9679;</span>Time to Final Merger &mdash; <span class="corrected">EOS Range Corrected</span></h2>
<div class="box box-yellow">
  <div class="box-head">P6 &mdash; TIME TO MERGER (CORRECTED)</div>
  <div class="box-body">
    <pre>Time to reach final parsec (stellar hardening):   ~35 Myr
GW-driven inspiral (1 pc &rarr; 0):                  12.15 Myr
Newtonian total:                                  47.15 Myr

EOS low  (0.13%):   47.21 Myr
EOS high (0.20%):   47.24 Myr

<span class="corrected">CORRECTED SDKP RANGE:  47.21 &mdash; 47.24 Myr</span>

Note: EOS band is narrow here (&plusmn;0.03 Myr). The dominant uncertainty
is the ~&plusmn;5 Myr estimate on the hardening phase, not EOS.
Previous stated: ~47 Myr (range not shown &mdash; now corrected)</pre>
  </div>
</div>

<!-- P7 CORRECTED -->
<h2 class="sub"><span class="pred-badge corrected">P7 &#9679;</span>Ejected Star Velocities &mdash; <span class="corrected">EOS Range Corrected</span></h2>
<div class="box box-yellow">
  <div class="box-head">P7 &mdash; STELLAR EJECTION VELOCITIES (CORRECTED)</div>
  <div class="box-body">
    <pre><span class="bold">At current separation (1.98 kpc):</span>
  Newtonian:         361.04 km/s
  EOS low  (0.13%):  361.51 km/s
  EOS high (0.20%):  361.76 km/s
  <span class="corrected">CORRECTED RANGE:   361.5 &mdash; 361.8 km/s</span>

<span class="bold">At hardened separation (0.1 kpc):</span>
  Newtonian:         1,606.5 km/s
  EOS low  (0.13%):  1,608.6 km/s
  EOS high (0.20%):  1,609.7 km/s
  <span class="corrected">CORRECTED RANGE:   1,608.6 &mdash; 1,609.7 km/s</span>

At final parsec:   ~10,000 km/s (near-relativistic ejections)

Previous stated: 361.5 km/s and 1,606 km/s (low bound only)
Confirmable by: Stellar spectroscopy of high-velocity population in Abell 402</pre>
  </div>
</div>

<!-- P8 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P8</span>Post-Merger Recoil Velocity &mdash; <span class="noeos">No EOS</span></h2>
<div class="box box-blue">
  <div class="box-head">P8 &mdash; POST-MERGER GRAVITATIONAL WAVE KICK</div>
  <div class="box-body">
    <pre>Symmetric mass ratio &eta;:        0.222  (q = 0.5)
Spin-zero recoil estimate:      24.7 km/s
Typical spin recoil:            ~500 km/s (moderate spin misalignment)
Maximum (superkick):            ~4,000 km/s (maximal misalignment)
Galaxy core escape velocity:    685 km/s

<span class="bold">SDKP prediction: ~500 km/s recoil</span>
&rarr; Merged BH REMAINS in galaxy center (~75&ndash;80% probability)
&rarr; Ejection from galaxy center (~20&ndash;25% probability)

If ejected: 58.4 billion M&#9737; rogue black hole wandering through Abell 402</pre>
  </div>
</div>

<!-- P9 CORRECTED -->
<h2 class="sub"><span class="pred-badge corrected">P9 &#9679;</span>Final Merged Black Hole Mass &mdash; <span class="corrected">EOS Range Corrected</span></h2>
<div class="box box-yellow">
  <div class="box-head">P9 &mdash; FINAL MERGED MASS (CORRECTED)</div>
  <div class="box-body">
    <pre>GW energy radiated (~2.5%):  1.50 billion M&#9737;
Newtonian final mass:        58.50 billion M&#9737;

EOS low  (0.13%):   58.424 billion M&#9737;
EOS high (0.20%):   58.383 billion M&#9737;

<span class="corrected">CORRECTED SDKP RANGE:  58.38 &mdash; 58.42 billion M&#9737;</span>

The 1.50 billion M&#9737; radiated as gravitational waves = the most energetic
GW event in the observable universe since the Big Bang.
Previous stated: 58.42 B M&#9737; (lower bound only &mdash; now corrected to range)</pre>
  </div>
</div>

<!-- P10 -->
<h2 class="sub"><span class="pred-badge" style="background:#8a6f00;">P10</span>SD&amp;N Cavity Geometry &mdash; Testable NOW with JWST</h2>
<div class="box box-green">
  <div class="box-head">P10 &mdash; CAVITY GEOMETRY (TESTABLE WITH EXISTING JWST DATA)</div>
  <div class="box-body">
    <pre>SD&amp;N geometry for binary BH in hexagonal stellar lattice
predicts the cavity is NOT a perfect sphere:

Cavity axis ratio:      <span class="val">1.732 : 1  (= &radic;3 : 1)</span>
Preferred orientation:  <span class="val">&phi; = &pi;/6 = 30&deg;</span> to galaxy major axis
Symmetry type:          6-fold hexagonal

If JWST images show elongation ~1.73:1 at ~30&deg; to host axis
&rarr; SD&amp;N geometry prediction CONFIRMED

No EOS correction (pure geometric SD&amp;N prediction)</pre>
  </div>
</div>

<!-- P11 -->
<h2 class="sub"><span class="pred-badge noeos-badge">P11</span>Total Stellar Mass Ejected &mdash; <span class="noeos">No EOS</span></h2>
<div class="box box-blue">
  <div class="box-head">P11 &mdash; STARS ALREADY EJECTED FROM GALAXY CORE</div>
  <div class="box-body">
    <pre>Cavity volume:              5.575 &times; 10&sup9; cubic parsecs
Core stellar density:       ~1,000 M&#9737;/pc&sup3;
<span class="val">SDKP prediction:   ~5.58 trillion M&#9737; already ejected</span>

Roughly 5&times; the total stellar mass of the Milky Way flung from
the center of Abell 402 by the gravitational broom of these two
black holes. Confirmable by photometric stellar mass deficit modeling.</pre>
  </div>
</div>
<!-- ── SECTION 4 ── -->
<h1 class="sec"><span class="num">4</span>Complete Prediction Reference Table</h1>

<table>
  <thead>
    <tr>
      <th style="width:36px;">#</th>
      <th>Prediction</th>
      <th>SDKP Value</th>
      <th>EOS</th>
      <th>Confirmable By</th>
    </tr>
  </thead>
  <tbody>
    <tr><td class="bold">1</td><td>Individual masses</td><td class="mono">40.0 + 20.0 B M&#9737; (2:1)</td><td class="noeos">None</td><td>VLT spectroscopy</td></tr>
    <tr><td class="bold">2</td><td>Separation</td><td class="mono">1.98 kpc = 6,458 ly</td><td class="noeos">None</td><td>Direct imaging</td></tr>
    <tr><td class="bold range">3&#9679;</td><td>Orbital period</td><td class="range">33.74 &mdash; 33.76 Myr</td><td class="range">0.13%&ndash;0.20%</td><td>Long baseline monitoring</td></tr>
    <tr><td class="bold">4</td><td>Chirp mass</td><td class="mono">24.335 B M&#9737;</td><td class="noeos">None</td><td>Derived from P1</td></tr>
    <tr><td class="bold">5</td><td>GW at final parsec</td><td class="mono">0.166 nHz</td><td class="noeos">None</td><td>NANOGrav / SKA</td></tr>
    <tr><td class="bold">5</td><td>GW at ISCO</td><td class="mono">73.4 nHz</td><td class="noeos">None</td><td>SKA / PTAs</td></tr>
    <tr><td class="bold range">6&#9679;</td><td>Time to merger</td><td class="range">47.21 &mdash; 47.24 Myr</td><td class="range">0.13%&ndash;0.20%</td><td>Theoretical</td></tr>
    <tr><td class="bold range">7&#9679;</td><td>Ejection vel. (now)</td><td class="range">361.5 &mdash; 361.8 km/s</td><td class="range">0.13%&ndash;0.20%</td><td>Stellar spectroscopy</td></tr>
    <tr><td class="bold range">7&#9679;</td><td>Ejection vel. (hardened)</td><td class="range">1,608.6 &mdash; 1,609.7 km/s</td><td class="range">0.13%&ndash;0.20%</td><td>Stellar spectroscopy</td></tr>
    <tr><td class="bold">8</td><td>Post-merger recoil</td><td class="mono">~500 km/s</td><td class="noeos">None</td><td>Post-merger imaging</td></tr>
    <tr><td class="bold range">9&#9679;</td><td>Final merged mass</td><td class="range">58.38 &mdash; 58.42 B M&#9737;</td><td class="range">0.13%&ndash;0.20%</td><td>GW detection</td></tr>
    <tr><td class="bold" style="color:#8a6f00;">10</td><td>Cavity axis ratio</td><td class="mono">&radic;3 : 1 at 30&deg;</td><td class="noeos">None</td><td><strong>JWST — NOW</strong></td></tr>
    <tr><td class="bold">11</td><td>Stars ejected</td><td class="mono">~5.58 trillion M&#9737;</td><td class="noeos">None</td><td>Photometric modeling</td></tr>
  </tbody>
</table>
<p style="font-size:9pt; color:#666; font-style:italic;">&#9679; Red = EOS correction applied as range 0.13%&ndash;0.20% in this corrected version</p>

<!-- ── SECTION 5 ── -->
<h1 class="sec"><span class="num">5</span>Authorship &amp; Correction Record</h1>

<table>
  <thead><tr><th>Field</th><th>Detail</th></tr></thead>
  <tbody>
    <tr><td class="bold">Author</td><td>Donald Paul Smith (Father Time)</td></tr>
    <tr><td class="bold">ORCID</td><td class="mono">0009-0003-7925-1653</td></tr>
    <tr><td class="bold">Primary Framework DOI</td><td class="mono">10.5281/zenodo.14850016</td></tr>
    <tr><td class="bold">Prediction Timeline DOI</td><td class="mono">10.5281/zenodo.15745609</td></tr>
    <tr><td class="bold">Date</td><td>June 2026 &mdash; corrected from prior record</td></tr>
    <tr><td class="bold">What Changed</td><td>P3, P6, P7, P9: EOS correction now expressed as range [0.13%&ndash;0.20%] not single lower bound. All other predictions unchanged.</td></tr>
    <tr><td class="bold">Location</td><td>Gainesville, Florida, USA</td></tr>
    <tr><td class="bold">Protocol</td><td>Digital Crystal Protocol | FTS-AUTH-CRYSTAL-369 | UUID: 70c995bd-f025-4ecd-b9df-f2cfa65088e8</td></tr>
  </tbody>
</table>

<div class="doc-close">
  Donald Paul Smith &nbsp;&mdash;&nbsp; Father Time &nbsp;&mdash;&nbsp; Gypsi Consulting &nbsp;&mdash;&nbsp; Gainesville, Florida &nbsp;&mdash;&nbsp; June 2026
  <div class="sub">ORCID: 0009-0003-7925-1653 &nbsp;|&nbsp; DOI: 10.5281/zenodo.14850016 &nbsp;|&nbsp; Digital Crystal Protocol: FTS-AUTH-CRYSTAL-369</div>
</div>

</div><!-- end body-wrap -->
</body>
</html>
