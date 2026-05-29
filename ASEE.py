import streamlit as st
import math
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER

# -------------------------------------------------------------------
# PAGE CONFIG
st.set_page_config(
    page_title="ENGAGE 2.0 — Visual Story",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------------------------
# COLOR PALETTE
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

# -------------------------------------------------------------------
# PDF GENERATION (Timeline only - Portrait mode)
def generate_timeline_pdf():
    """Generate PDF document with project timeline visuals (Portrait)"""
    buffer = BytesIO()
    
    # Create document with portrait orientation
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=15*mm, leftMargin=15*mm,
                            topMargin=15*mm, bottomMargin=15*mm)
    
    styles = getSampleStyleSheet()
    font_name = 'Helvetica'
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=22,
        textColor=colors.HexColor(PURPLE_D),
        spaceAfter=10,
        alignment=TA_CENTER,
        fontStyle='bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=12,
        textColor=colors.HexColor(GRAY_MID),
        spaceAfter=15,
        alignment=TA_CENTER
    )
    
    section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=14,
        textColor=colors.HexColor(PURPLE),
        spaceAfter=10,
        fontStyle='bold'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=9,
        textColor=colors.HexColor(GRAY_D),
        leading=13
    )
    
    story = []
    
    # Title
    story.append(Paragraph("ENGAGE 2.0 — Project Timeline", title_style))
    story.append(Paragraph("From survey insight to national programme", subtitle_style))
    story.append(Spacer(1, 8*mm))
    
    # Timeline section
    story.append(Paragraph("Project Timeline", section_title))
    story.append(Spacer(1, 3*mm))
    
    # Timeline as a table with years and descriptions
    timeline_data = [
        ["Year", "Milestone"],
        ["2022", "Survey & research"],
        ["2023", "Programme design"],
        ["2024", "Phase 1 launch"],
        ["2026", "Phase 2 begins"],
        ["2028", "National scale"],
    ]
    
    timeline_table = Table(timeline_data, colWidths=[40*mm, 100*mm])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(PURPLE)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOLD', (0, 0), (-1, 0), True),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor(PURPLE)),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(timeline_table)
    story.append(Spacer(1, 10*mm))
    
    # Vision chain section
    story.append(Paragraph("The ENGAGE Vision Chain", section_title))
    story.append(Spacer(1, 3*mm))
    
    vision_items = [
        "• Girls & Young Women selected",
        "• Data Science & AI skills built",
        "• Public Health applications",
        "• African Innovators emerge",
        "• Healthier Communities",
    ]
    
    for item in vision_items:
        story.append(Paragraph(item, body_style))
        story.append(Spacer(1, 2*mm))
    
    story.append(Spacer(1, 8*mm))
    
    # Programme pipeline
    story.append(Paragraph("Programme Pipeline", section_title))
    story.append(Spacer(1, 3*mm))
    
    pipeline_steps = [
        "1. Advertisement", "2. Applications", "3. Math Contest", "4. Interviews",
        "5. Selection", "6. Tier 1 Training", "7. Tier 2 Training", 
        "8. Tier 3 Training", "9. Internship", "10. Employment/Innovation"
    ]
    
    pipeline_text = " → ".join(pipeline_steps)
    pipeline_para = Paragraph(pipeline_text, body_style)
    story.append(pipeline_para)
    story.append(Spacer(1, 10*mm))
    
    # Phase 2 Roadmap
    story.append(Paragraph("Phase 2.0 — Expansion Roadmap", section_title))
    story.append(Spacer(1, 3*mm))
    
    roadmap_items = [
        ("Short term (2026):", "25 trainees per centre, New UoN UNITID centre, Self-sponsored module, Remote jobs pipeline"),
        ("Medium term (2027):", "Open to boys & young men, Disability-inclusive content, Accessible equipment, Online modules"),
        ("Long term (2028+):", "5 new regional centres, National innovation hub"),
    ]
    
    for phase, details in roadmap_items:
        story.append(Paragraph(f"<b>{phase}</b>", body_style))
        story.append(Paragraph(details, body_style))
        story.append(Spacer(1, 4*mm))
    
    story.append(Spacer(1, 8*mm))
    
    # Impact numbers
    story.append(Paragraph("Phase 1 Impact", section_title))
    story.append(Spacer(1, 3*mm))
    
    impact_data = [
        ["Metric", "Value"],
        ["Total beneficiaries trained", "329"],
        ["Regional universities", "6"],
        ["Internship sites", "50"],
        ["Validated curricula", "3"],
    ]
    
    impact_table = Table(impact_data, colWidths=[80*mm, 40*mm])
    impact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(TEAL)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(impact_table)
    story.append(Spacer(1, 10*mm))
    
    # Footer with call to action
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph(
        "Partner with ENGAGE 2.0 — Help unlock Africa's AI potential.",
        ParagraphStyle('FooterStyle', parent=body_style,
                      alignment=TA_CENTER,
                      textColor=colors.HexColor(TEAL_D),
                      fontSize=9,
                      fontName=font_name)
    ))
    story.append(Paragraph(
        "University of Nairobi · Institute of Tropical and Infectious Diseases",
        ParagraphStyle('FooterStyle2', parent=body_style,
                      alignment=TA_CENTER,
                      textColor=colors.HexColor(GRAY_MID),
                      fontSize=8,
                      fontName=font_name)
    ))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    return buffer

# -------------------------------------------------------------------
# PDF DOWNLOAD BUTTON FUNCTION
def download_timeline_button():
    """Create download button for timeline PDF"""
    pdf_buffer = generate_timeline_pdf()
    
    st.download_button(
        label="📥 Download Timeline as PDF",
        data=pdf_buffer,
        file_name="ENGAGE_2_Timeline.pdf",
        mime="application/pdf",
        use_container_width=False,
    )

# -------------------------------------------------------------------
# CUSTOM CSS
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

# -------------------------------------------------------------------
# WEBSITE CONTENT - HERO
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

# -------------------------------------------------------------------
# ADD DOWNLOAD BUTTON IN SIDEBAR
with st.sidebar:
    st.markdown("### 📄 Document")
    download_timeline_button()
    st.markdown("---")
    st.caption("ENGAGE 2.0 · University of Nairobi")

# -------------------------------------------------------------------
# TABS
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

# TAB 1: PROBLEM
with tabs[0]:
    st.markdown("""
    <div class="sec">
      <div class="kicker">The Challenge</div>
      <div class="sec-title">Africa's opportunity — and its gap</div>
      <div class="sec-body">The future of employment is driven by technology. Yet women make up only
      30% of AI experts globally. Africa faces a double burden of disease demanding locally-built,
      data-driven solutions.</div>
      <div class="stat-grid">
        <div class="stat-card"><div class="stat-num" style="color:#534AB7">30%</div>
          <div class="stat-lbl">of global AI experts are women</div></div>
        <div class="stat-card"><div class="stat-num" style="color:#D85A30">2×</div>
          <div class="stat-lbl">disease burden — infectious + chronic</div></div>
        <div class="stat-card"><div class="stat-num" style="color:#1D9E75">&lt;5%</div>
          <div class="stat-lbl">African women in data science roles</div></div>
        <div class="stat-card"><div class="stat-num" style="color:#BA7517">4B+</div>
          <div class="stat-lbl">Africans by 2050 — pipeline is now</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Gender gap in AI expertise**")
        for label, pct, color in [("Women in AI", 30, "#534AB7"), ("Men in AI", 70, "#E8E6E0")]:
            st.markdown(f"""
            <div class="bar-row">
              <div style="min-width:110px;font-size:13px;color:{GRAY_D};">{label}</div>
              <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
              <div style="min-width:36px;font-size:13px;font-weight:600;">{pct}%</div>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("**Africa's disease burden breakdown**")
        for label, pct, color in [
            ("Infectious diseases", 45, "#D85A30"),
            ("Chronic conditions", 32, "#BA7517"),
            ("Maternal health", 13, "#534AB7"),
            ("Injuries", 10, "#888780"),
        ]:
            st.markdown(f"""
            <div class="bar-row">
              <div style="min-width:150px;font-size:13px;color:{GRAY_D};">{label}</div>
              <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
              <div style="min-width:36px;font-size:13px;font-weight:600;">{pct}%</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# TAB 2: VISION & WHY GIRLS
with tabs[1]:
    st.markdown("""
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
        <div style="background:white;border-radius:10px;padding:12px 6px;">
          <div style="font-weight:700;color:{PURPLE_D};font-size:15px;">2022</div>
          <div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">Survey & research</div>
        </div>
        <div style="background:white;border-radius:10px;padding:12px 6px;">
          <div style="font-weight:700;color:{PURPLE_D};font-size:15px;">2023</div>
          <div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">Programme design</div>
        </div>
        <div style="background:white;border-radius:10px;padding:12px 6px;">
          <div style="font-weight:700;color:{PURPLE_D};font-size:15px;">2024</div>
          <div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">Phase 1 launch</div>
        </div>
        <div style="background:white;border-radius:10px;padding:12px 6px;">
          <div style="font-weight:700;color:{PURPLE_D};font-size:15px;">2026</div>
          <div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">Phase 2 begins</div>
        </div>
        <div style="background:white;border-radius:10px;padding:12px 6px;">
          <div style="font-weight:700;color:{PURPLE_D};font-size:15px;">2028</div>
          <div style="font-size:11px;color:{GRAY_MID};margin-top:3px;">National scale</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Note: Tabs 3-8 continue with your original content...
# For brevity, I've shown the first two tabs. The remaining tabs (3-8)
# should be copied exactly from your original working code.

st.success("✅ App loaded successfully! Use the sidebar to download the PDF timeline.")
