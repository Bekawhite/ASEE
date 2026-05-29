import streamlit as st
import math

st.set_page_config(
    page_title="ENGAGE 2.0 — Visual Story",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PURPLE   = "#534AB7"
PURPLE_L = "#EEEDFE"
PURPLE_D = "#3C3489"
TEAL     = "#1D9E75"
TEAL_L   = "#E1F5EE"
TEAL_D   = "#085041"
CORAL    = "#D85A30"
CORAL_L  = "#FAECE7"
CORAL_D  = "#712B13"
AMBER    = "#BA7517"
AMBER_L  = "#FAEEDA"
GRAY_L   = "#F5F4F0"
GRAY_MID = "#888780"
GRAY_D   = "#2C2C2A"
WHITE    = "#FFFFFF"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');
html,body,[class*="css"]{{font-family:'DM Sans',sans-serif;background:#FAFAF8;color:{GRAY_D};}}
.stApp{{background:#FAFAF8;}}
section[data-testid="stSidebar"]{{display:none;}}
.block-container{{padding:0!important;max-width:100%!important;}}
.hero{{background:{PURPLE};padding:64px 8vw 52px;position:relative;overflow:hidden;}}
.hero::before{{content:"";position:absolute;top:-60px;right:-60px;width:380px;height:380px;border-radius:50%;background:{PURPLE_D};opacity:0.45;}}
.hero-kicker{{font-family:'Sora',sans-serif;font-size:11px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#AFA9EC;margin-bottom:14px;}}
.hero-title{{font-family:'DM Serif Display',serif;font-size:clamp(32px,5vw,58px);color:{WHITE};line-height:1.1;margin-bottom:14px;position:relative;}}
.hero-sub{{font-size:15px;color:#CECBF6;max-width:520px;line-height:1.75;margin-bottom:26px;}}
.hero-tags{{display:flex;gap:8px;flex-wrap:wrap;}}
.hero-tag{{background:{PURPLE_D};color:#AFA9EC;border-radius:20px;padding:5px 14px;font-size:11px;font-weight:500;}}
.sec{{padding:48px 8vw 0;}}
.sec-last{{padding-bottom:64px;}}
.kicker{{font-family:'Sora',sans-serif;font-size:10px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:{GRAY_MID};margin-bottom:8px;}}
.sec-title{{font-family:'DM Serif Display',serif;font-size:clamp(20px,3vw,30px);color:{GRAY_D};margin-bottom:6px;}}
.sec-body{{font-size:14px;color:{GRAY_MID};line-height:1.8;max-width:600px;margin-bottom:24px;}}
.divider{{height:1px;background:#E8E6E0;margin:48px 8vw;}}
.stat-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:32px;}}
.stat-card{{background:{WHITE};border:1px solid #E8E6E0;border-radius:14px;padding:22px 18px;text-align:center;}}
.stat-num{{font-family:'Sora',sans-serif;font-size:40px;font-weight:700;line-height:1;margin-bottom:4px;}}
.stat-lbl{{font-size:11px;color:{GRAY_MID};font-weight:500;letter-spacing:0.04em;}}
.pipe{{display:flex;flex-wrap:wrap;align-items:center;gap:0;margin-bottom:28px;}}
.pipe-step{{border-radius:10px;padding:10px 16px;font-size:12px;font-weight:500;white-space:nowrap;border:1px solid transparent;}}
.pipe-arr{{color:{GRAY_MID};font-size:16px;padding:0 5px;}}
.card{{background:{WHITE};border:1px solid #E8E6E0;border-radius:14px;padding:20px 22px;margin-bottom:12px;}}
.phase-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:28px;}}
.phase-card{{border-radius:14px;padding:20px 18px;}}
.phase-lbl{{font-family:'Sora',sans-serif;font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;margin-bottom:10px;}}
.phase-item{{font-size:12px;line-height:2;display:flex;align-items:center;gap:7px;}}
.dot{{width:5px;height:5px;border-radius:50%;flex-shrink:0;display:inline-block;}}
.milestone{{border-radius:10px;padding:10px 14px;margin-bottom:8px;font-size:13px;font-weight:500;}}
.eco-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:28px;}}
.eco-card{{border-radius:12px;padding:16px 14px;text-align:center;}}
.eco-icon{{font-size:24px;margin-bottom:6px;}}
.eco-label{{font-size:12px;font-weight:500;}}
.partner-card{{background:{WHITE};border:1px solid #E8E6E0;border-left:4px solid;border-radius:14px;padding:20px 22px;margin-bottom:12px;}}
.cta-box{{background:{TEAL_L};border:1px solid #9FE1CB;border-radius:18px;padding:44px 48px;text-align:center;margin:0 8vw 64px;}}
.cta-title{{font-family:'DM Serif Display',serif;font-size:26px;color:{TEAL_D};margin-bottom:10px;}}
.cta-body{{font-size:14px;color:{TEAL_D};opacity:0.85;max-width:500px;margin:0 auto;line-height:1.75;}}
.bar-row{{display:flex;align-items:center;gap:10px;margin-bottom:8px;}}
.bar-bg{{height:10px;border-radius:5px;background:#ECEAE4;flex:1;overflow:hidden;}}
.bar-fill{{height:10px;border-radius:5px;}}
.region-grid{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px;}}
.rtag{{border-radius:8px;padding:8px 14px;font-size:12px;font-weight:500;}}
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-kicker">Takeda Pharmaceuticals Initiative · 2024–2028</div>
  <div class="hero-title">ENabling Girls in AI<br>&amp; Growing Expertise</div>
  <div class="hero-sub">Training girls and young women across Kenya in data science, machine learning,
  and AI — to solve Africa's greatest public health challenges.</div>
  <div class="hero-tags">
    <span class="hero-tag">University of Nairobi</span>
    <span class="hero-tag">UCSF</span>
    <span class="hero-tag">6 Regional Universities</span>
    <span class="hero-tag">MoE Approved</span>
    <span class="hero-tag">329 Trained</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

tabs = st.tabs([
    "🌍  The Problem",
    "🎯  Vision & Why Girls",
    "⚙️  How It Works",
    "📍  Regional Network",
    "📊  Achievements",
    "🚀  Phase 2 Roadmap",
    "🌐  Ecosystem",
    "🤝  Partnerships",
])

# ── TAB 1: PROBLEM ────────────────────────────────────────────────────────────
with tabs[0]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">The Challenge</div>
      <div class="sec-title">Africa's opportunity — and its gap</div>
      <div class="sec-body">The future of employment is driven by technology. Yet women make up only
      30% of AI experts globally. Africa faces a double burden of disease demanding locally-built,
      data-driven solutions.</div>
      <div class="stat-grid">
        <div class="stat-card"><div class="stat-num" style="color:{PURPLE}">30%</div>
          <div class="stat-lbl">of global AI experts are women</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{CORAL}">2×</div>
          <div class="stat-lbl">disease burden — infectious + chronic</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{TEAL}">&lt;5%</div>
          <div class="stat-lbl">African women in data science roles</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{AMBER}">4B+</div>
          <div class="stat-lbl">Africans by 2050 — pipeline is now</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Gender gap in AI expertise**")
        for label, pct, color in [("Women in AI", 30, PURPLE), ("Men in AI", 70, "#E8E6E0")]:
            st.markdown(f"""
            <div class="bar-row">
              <div style="min-width:110px;font-size:13px;color:{GRAY_D};">{label}</div>
              <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
              <div style="min-width:36px;font-size:13px;font-weight:600;color:{color if color!='{GRAY_D}' else GRAY_D};">{pct}%</div>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**Africa's disease burden breakdown**")
        for label, pct, color in [
            ("Infectious diseases", 45, CORAL),
            ("Chronic conditions", 32, AMBER),
            ("Maternal health", 13, PURPLE),
            ("Injuries", 10, GRAY_MID),
        ]:
            st.markdown(f"""
            <div class="bar-row">
              <div style="min-width:150px;font-size:13px;color:{GRAY_D};">{label}</div>
              <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
              <div style="min-width:36px;font-size:13px;font-weight:600;color:{GRAY_D};">{pct}%</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── TAB 2: VISION ─────────────────────────────────────────────────────────────
with tabs[1]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">The Vision</div>
      <div class="sec-title">From survey insight to national programme</div>
      <div class="sec-body">A 2022 survey revealed stark gender disparity in data science.
      That evidence became the foundation for a deliberate, targeted intervention.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Why girls?")
        for label, bg, fg in [
            ("2022 Gender Gap Survey", PURPLE_L, PURPLE_D),
            ("Women underrepresented in AI", PURPLE_L, PURPLE_D),
            ("Focused intervention designed", TEAL_L, TEAL_D),
            ("Evidence-based curriculum built", TEAL_L, TEAL_D),
            ("National rollout approved", CORAL_L, CORAL_D),
        ]:
            st.markdown(
                f'<div style="background:{bg};color:{fg};border-radius:10px;'
                f'padding:11px 16px;margin-bottom:8px;font-size:13px;font-weight:500;">'
                f'&#10142;  {label}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### The ENGAGE vision chain")
        vision = [
            ("Girls & Young Women selected", PURPLE, PURPLE_L, PURPLE_D),
            ("Data Science & AI skills built", PURPLE, PURPLE_L, PURPLE_D),
            ("Public Health applications", TEAL, TEAL_L, TEAL_D),
            ("African Innovators emerge", TEAL, TEAL_L, TEAL_D),
            ("Healthier Communities", TEAL, TEAL_L, TEAL_D),
        ]
        widths = [100, 86, 72, 58, 44]
        for (label, color, bg, fg), w in zip(vision, widths):
            st.markdown(
                f'<div style="background:{bg};color:{fg};border-radius:10px;'
                f'padding:11px 16px;margin-bottom:6px;font-size:13px;font-weight:500;'
                f'width:{w}%;border-left:4px solid {color};">{label}</div>',
                unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{PURPLE_L};border-radius:14px;padding:22px 26px;margin:28px 8vw 40px;">
      <div style="font-family:'Sora',sans-serif;font-size:10px;font-weight:700;
        letter-spacing:0.14em;text-transform:uppercase;color:{PURPLE};margin-bottom:12px;">
        Project Timeline</div>
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;text-align:center;">
        {''.join([f'<div style="background:white;border-radius:10px;padding:12px 6px;">'
          f'<div style="font-weight:700;color:{PURPLE_D};font-size:15px;">{y}</div>'
          f'<div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">{d}</div></div>'
          for y,d in [("2022","Survey &amp; research"),("2023","Programme design"),
                      ("2024","Phase 1 launch"),("2026","Phase 2 begins"),("2028","National scale")]])}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 3: HOW IT WORKS ───────────────────────────────────────────────────────
with tabs[2]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">Programme Design</div>
      <div class="sec-title">From application to employment</div>
      <div class="sec-body">A rigorous selection process followed by tiered training ensures
      quality at every stage — from high school curiosity to university-level AI projects.</div>
    </div>
    """, unsafe_allow_html=True)

    pipeline = [
        ("Advertisement", PURPLE_L, PURPLE_D),
        ("Applications", PURPLE_L, PURPLE_D),
        ("Math Contest", PURPLE_L, PURPLE_D),
        ("Interviews", PURPLE_L, PURPLE_D),
        ("Selection", PURPLE_L, PURPLE_D),
        ("Tier 1 Training", TEAL_L, TEAL_D),
        ("Tier 2 Training", TEAL_L, TEAL_D),
        ("Tier 3 Training", TEAL_L, TEAL_D),
        ("Internship", AMBER_L, AMBER),
        ("Employment / Innovation", CORAL_L, CORAL_D),
    ]
    pipe_html = '<div class="pipe" style="padding:0 8vw 28px;">'
    for i, (step, bg, fg) in enumerate(pipeline):
        pipe_html += f'<div class="pipe-step" style="background:{bg};color:{fg};border-color:{bg};">{step}</div>'
        if i < len(pipeline)-1:
            pipe_html += '<div class="pipe-arr">→</div>'
    pipe_html += '</div>'
    st.markdown(pipe_html, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, tier, level, color, bg, fg, items in [
        (c1,"Tier 1","High School",PURPLE,PURPLE_L,PURPLE_D,
         ["Foundational data literacy","Introduction to Python","Basic statistics","Public health concepts"]),
        (c2,"Tier 2","TVET & College",TEAL,TEAL_L,TEAL_D,
         ["Intermediate data analysis","Machine learning basics","Health data projects","Real-world datasets"]),
        (c3,"Tier 3","University",CORAL,CORAL_L,CORAL_D,
         ["Advanced AI/ML methods","Research-grade projects","Publications","Innovation leadership"]),
    ]:
        with col:
            st.markdown(
                f'<div style="background:{bg};border-radius:14px;padding:20px 18px;">'
                f'<div style="font-family:Sora,sans-serif;font-size:10px;font-weight:700;'
                f'letter-spacing:0.14em;text-transform:uppercase;color:{fg};margin-bottom:4px;">{tier}</div>'
                f'<div style="font-size:15px;font-weight:600;color:{fg};margin-bottom:12px;">{level}</div>'
                + "".join([f'<div style="font-size:12px;color:{fg};opacity:0.9;line-height:1.9;">'
                           f'<span style="display:inline-block;width:5px;height:5px;border-radius:50%;'
                           f'background:{color};margin-right:8px;vertical-align:middle;"></span>{item}</div>'
                           for item in items])
                + '</div>', unsafe_allow_html=True)
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ── TAB 4: REGIONAL NETWORK ───────────────────────────────────────────────────
with tabs[3]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">Geography</div>
      <div class="sec-title">A national training network</div>
      <div class="sec-body">Six regional universities — chosen for geographic equity across Kenya —
      form the backbone of the ENGAGE ecosystem, with UoN and UCSF providing technical oversight.</div>
    </div>
    """, unsafe_allow_html=True)

    try:
        import pandas as pd
        df = pd.DataFrame({
            "University": ["Pwani University","SEKU","Meru University","DeKUT","Kabarak","JOOUST","UoN Hub"],
            "Region": ["Coast","South East","East","Central","Rift Valley","Nyanza/Western","Nairobi"],
            "lat": [-3.32,-1.87,0.05,-0.39,-0.22,0.09,-1.286],
            "lon": [40.12,38.54,37.65,36.97,35.99,34.76,36.817],
        })
        st.markdown('<div style="padding:0 8vw 20px;">', unsafe_allow_html=True)
        st.map(df, latitude="lat", longitude="lon", size=80000, color="#534AB7")
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception:
        pass

    region_html = '<div class="region-grid" style="padding:0 8vw 16px;">'
    for region, uni, bg, fg in [
        ("Coast","Pwani University",PURPLE_L,PURPLE_D),
        ("South East","SEKU",CORAL_L,CORAL_D),
        ("East","Meru University",AMBER_L,AMBER),
        ("Central","DeKUT",TEAL_L,TEAL_D),
        ("Rift Valley","Kabarak",CORAL_L,CORAL_D),
        ("Nyanza/Western","JOOUST",PURPLE_L,PURPLE_D),
    ]:
        region_html += (f'<div class="rtag" style="background:{bg};color:{fg};">'
                        f'<strong>{region}</strong> · {uni}</div>')
    region_html += '</div>'
    st.markdown(region_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{GRAY_L};border-radius:14px;padding:20px 24px;margin:0 8vw 40px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;
        color:{GRAY_MID};margin-bottom:12px;">Coordination structure</div>
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
        <div style="background:{PURPLE};color:white;border-radius:10px;padding:10px 16px;
          font-size:13px;font-weight:500;">UoN + UCSF<br><span style="font-size:11px;opacity:0.8;">Technical hub</span></div>
        <div style="font-size:18px;color:{GRAY_MID};">↔</div>
        {''.join([f'<div style="background:{WHITE};border:1px solid #E8E6E0;border-radius:10px;padding:10px 14px;font-size:12px;font-weight:500;color:{GRAY_D};">{u}</div>'
                  for u in ["Pwani","SEKU","Meru","DeKUT","Kabarak","JOOUST"]])}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 5: ACHIEVEMENTS ───────────────────────────────────────────────────────
with tabs[4]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">Phase 1 · Impact</div>
      <div class="sec-title">Proof of success</div>
      <div class="sec-body">In two years, ENGAGE built validated systems, trained hundreds,
      and secured national recognition — a foundation ready to scale.</div>
      <div class="stat-grid">
        <div class="stat-card"><div class="stat-num" style="color:{PURPLE}">329</div>
          <div class="stat-lbl">Total beneficiaries trained</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{TEAL}">6</div>
          <div class="stat-lbl">Regional universities</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{CORAL}">50</div>
          <div class="stat-lbl">Internship sites</div></div>
        <div class="stat-card"><div class="stat-num" style="color:{AMBER}">3</div>
          <div class="stat-lbl">Validated curricula</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown("**Trainees by tier**")
        for label, count, total, color in [
            ("Tier 1 — High School", 120, 329, PURPLE),
            ("Tier 2 — TVET / College", 104, 329, TEAL),
            ("Tier 3 — University", 105, 329, CORAL),
        ]:
            pct = round(count/329*100)
            st.markdown(f"""
            <div class="bar-row" style="margin-bottom:14px;">
              <div style="min-width:180px;font-size:13px;color:{GRAY_D};">{label}</div>
              <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
              <div style="min-width:40px;font-size:13px;font-weight:700;color:{color};text-align:right;">{count}</div>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**Programme milestones**")
        for text, bg, fg in [
            ("Curricula developed & validated", TEAL_L, TEAL_D),
            ("Infrastructure at 6 sites", TEAL_L, TEAL_D),
            ("Faculty capacity built", TEAL_L, TEAL_D),
            ("50 internship sites secured", TEAL_L, TEAL_D),
            ("MoE approval — national rollout", PURPLE_L, PURPLE_D),
        ]:
            st.markdown(
                f'<div class="milestone" style="background:{bg};color:{fg};">✓  {text}</div>',
                unsafe_allow_html=True)

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ── TAB 6: ROADMAP ────────────────────────────────────────────────────────────
with tabs[5]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">Phase 2.0</div>
      <div class="sec-title">The expansion roadmap</div>
      <div class="sec-body">Building on proven success, Phase 2 scales intake, broadens
      inclusion, and plants the seeds of a national innovation ecosystem.</div>
    </div>
    """, unsafe_allow_html=True)

    roadmap_html = '<div class="phase-grid" style="padding:0 8vw 28px;">'
    for phase, color, bg, fg, items in [
        ("Short term", PURPLE, PURPLE_L, PURPLE_D,
         ["25 trainees per centre","New UoN UNITID centre","Self-sponsored module",
          "Remote jobs pipeline","Strengthen internship sites"]),
        ("Medium term", TEAL, TEAL_L, TEAL_D,
         ["Open to boys & young men","Disability-inclusive content",
          "Accessible equipment","Online self-paced modules"]),
        ("Long term", CORAL, CORAL_L, CORAL_D,
         ["5 new regional centres","Marsabit, Garissa, Kakamega",
          "Kisii, West Pokot","National innovation hub"]),
    ]:
        roadmap_html += (
            f'<div class="phase-card" style="background:{bg};border-top:4px solid {color};">'
            f'<div class="phase-lbl" style="color:{color};">{phase}</div>'
            + "".join([f'<div class="phase-item" style="color:{fg};">'
                       f'<span class="dot" style="background:{color};"></span>{item}</div>'
                       for item in items])
            + '</div>'
        )
    roadmap_html += '</div>'
    st.markdown(roadmap_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{GRAY_L};border-radius:14px;padding:20px 24px;margin:0 8vw 40px;">
      <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;
        color:{GRAY_MID};margin-bottom:14px;">Indicative timeline</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;text-align:center;">
        {''.join([f'<div style="background:{bg};border-radius:10px;padding:14px 10px;">'
          f'<div style="font-weight:700;color:{fg};font-size:14px;">{yr}</div>'
          f'<div style="font-size:11px;color:{fg};opacity:0.8;margin-top:3px;">{desc}</div></div>'
          for yr,desc,bg,fg in [
            ("2026","Short-term actions",PURPLE_L,PURPLE_D),
            ("2027","Medium-term expansion",TEAL_L,TEAL_D),
            ("2028","Long-term national scale",CORAL_L,CORAL_D),
          ]])}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 7: ECOSYSTEM ──────────────────────────────────────────────────────────
with tabs[6]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">The Bigger Picture</div>
      <div class="sec-title">A national innovation ecosystem</div>
      <div class="sec-body">ENGAGE is not just a training programme. It is the seed of a
      national ecosystem connecting AI talent, public health research, employment, and innovation.</div>
    </div>
    """, unsafe_allow_html=True)

    ecosystem = [
        ("🤖", "AI Workforce", PURPLE_L, PURPLE_D),
        ("🏥", "Public Health Innovation", TEAL_L, TEAL_D),
        ("💼", "Employment", CORAL_L, CORAL_D),
        ("⚤", "Gender Equity", PURPLE_L, PURPLE_D),
        ("🔬", "Research", AMBER_L, AMBER),
        ("🚀", "Startups", CORAL_L, CORAL_D),
        ("🌿", "Community Health", TEAL_L, TEAL_D),
        ("💻", "Remote Jobs", AMBER_L, AMBER),
    ]
    st.markdown(f"""
    <div style="padding:0 8vw;">
      <div style="text-align:center;margin-bottom:20px;">
        <div style="display:inline-block;background:{PURPLE};color:white;border-radius:50%;
          width:110px;height:110px;line-height:110px;font-family:'Sora',sans-serif;
          font-size:18px;font-weight:700;">ENGAGE</div>
      </div>
      <div class="eco-grid">
        {''.join([f'<div class="eco-card" style="background:{bg};">'
          f'<div class="eco-icon">{icon}</div>'
          f'<div class="eco-label" style="color:{fg};">{label}</div></div>'
          for icon,label,bg,fg in ecosystem])}
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{PURPLE_L};border-radius:14px;padding:20px 26px;margin:0 8vw 40px;">
      <div style="font-size:13px;color:{PURPLE_D};line-height:1.8;text-align:center;">
        <strong>ENGAGE graduates</strong> enter as <strong>AI workforce</strong> →
        drive <strong>public health innovation</strong> → create <strong>startups</strong> →
        build <strong>community health</strong> solutions → advance <strong>gender equity</strong> →
        attract <strong>research partnerships</strong> → generate <strong>remote job opportunities</strong>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 8: PARTNERSHIPS ───────────────────────────────────────────────────────
with tabs[7]:
    st.markdown(f"""
    <div class="sec">
      <div class="kicker">Support Needed</div>
      <div class="sec-title">Partnership opportunities</div>
      <div class="sec-body">ENGAGE 2.0 needs partners at every level —
      from hardware to human capital. Here is where your support creates greatest leverage.</div>
    </div>
    """, unsafe_allow_html=True)

    for title, badge, orgs, color, bg, fg, items in [
        ("Corporate CSR & tech sector","Most strategic fit",
         "Google · Microsoft · Safaricom · IBM · AWS · local telcos",
         PURPLE,PURPLE_L,PURPLE_D,
         "Fund hardware · Provide internet · Offer internship placements · Co-brand innovation hub"),
        ("Bilateral & multilateral funders","High impact",
         "USAID · UK FCDO · GIZ · World Bank · Gates Foundation",
         TEAL,TEAL_L,TEAL_D,
         "Cover stipends & salaries · Fund 5 new centres · Support disability-inclusive content"),
        ("Academic & research partners","Strong fit",
         "NIH Fogarty · Wellcome Trust · African Academy of Sciences",
         CORAL,CORAL_L,CORAL_D,
         "Fund curriculum R&D · Develop online modules · Publish programme impact globally"),
        ("Revenue-generating models","Complementary",
         "Self-sponsored cohorts · Curriculum licensing",
         AMBER,AMBER_L,AMBER,
         "Fee-paying module cross-subsidises scholarships · Licensing generates operational revenue"),
    ]:
        st.markdown(
            f'<div class="partner-card" style="border-left-color:{color};">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:8px;">'
            f'<div><div style="font-family:Sora,sans-serif;font-size:14px;font-weight:600;color:{GRAY_D};">{title}</div>'
            f'<div style="font-size:12px;color:{GRAY_MID};margin-top:2px;">{orgs}</div></div>'
            f'<div style="background:{bg};color:{fg};border-radius:20px;padding:3px 12px;'
            f'font-size:10px;font-weight:700;letter-spacing:0.06em;white-space:nowrap;">{badge}</div></div>'
            f'<div style="font-size:13px;color:{GRAY_MID};border-top:1px solid #F0EEE8;padding-top:8px;line-height:1.8;">{items}</div>'
            f'</div>',
            unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{GRAY_L};border-radius:14px;padding:20px 24px;margin:8px 0 40px;">
      <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;
        color:{GRAY_MID};margin-bottom:14px;">What it takes to open one centre</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;">
        {''.join([f'<div style="background:white;border-radius:10px;padding:12px 14px;">'
          f'<div style="font-weight:700;color:{PURPLE_D};font-size:16px;">{n}</div>'
          f'<div style="font-size:11px;color:{GRAY_MID};margin-top:2px;">{d}</div></div>'
          for n,d in [("25","Desktop computers"),("2","Laptops"),("1","Projector"),
                      ("1","Internet connection"),("1","Training room"),("1+3","Coordinator + Faculty")]])}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="cta-box">
  <div class="cta-title">Partner with ENGAGE 2.0</div>
  <div class="cta-body">Help unlock Africa's AI potential — one girl, one dataset,
  one discovery at a time.<br><br>
  <strong>University of Nairobi · Institute of Tropical and Infectious Diseases</strong>
  </div>
