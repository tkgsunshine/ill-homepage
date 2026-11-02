import os
import subprocess
import json
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "cases-refresh", "banners")
TEMP_DIR = "/tmp/case_banners_v2"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Common SVG defs for drop shadows and gradients
SVG_DEFS = """
  <defs>
    <filter id="shadow-main" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.08" />
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.04" />
    </filter>
    <filter id="shadow-card" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.07" />
      <feDropShadow dx="0" dy="1" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.03" />
    </filter>
    <linearGradient id="cyan-mint" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#10B981" />
    </linearGradient>
    <linearGradient id="mint-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#0EA5E9" />
    </linearGradient>
  </defs>
"""

# Dictionary of all 18 cases
CASES_DATA = [
    {
        "filename": "illust_case_security_recruitment_v2.webp",
        "title": "重い求人サイトを軽く安く作り直す",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Browser Window Frame -->
  <g filter="url(#shadow-main)">
    <rect x="70" y="35" width="260" height="165" rx="14" fill="#FFFFFF" />
    <path d="M70 49C70 41.268 76.268 35 84 35H316C323.732 35 330 41.268 330 49V68H70V49Z" fill="#F8FAFC" />
    <line x1="70" y1="68" x2="330" y2="68" stroke="#E2E8F0" stroke-width="1.5" />
    
    <!-- Window Controls -->
    <circle cx="88" cy="51.5" r="4.5" fill="#CBD5E1" />
    <circle cx="102" cy="51.5" r="4.5" fill="#E2E8F0" />
    <circle cx="116" cy="51.5" r="4.5" fill="#E2E8F0" />
    
    <!-- Abstract URL Bar -->
    <rect x="135" y="44" width="130" height="15" rx="7.5" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <rect x="145" y="49" width="50" height="5" rx="2.5" fill="#94A3B8" />

    <!-- Content: Hero Section -->
    <rect x="88" y="82" width="130" height="12" rx="4" fill="#0F172A" />
    <rect x="88" y="100" width="110" height="6" rx="3" fill="#94A3B8" />
    <rect x="88" y="111" width="90" height="6" rx="3" fill="#CBD5E1" />
    
    <!-- Fast Speed Indicator / Clean Light Badge -->
    <rect x="88" y="128" width="65" height="18" rx="9" fill="url(#cyan-mint)" />
    <rect x="96" y="134" width="49" height="6" rx="3" fill="#FFFFFF" />

    <!-- Right Side Content Card inside browser -->
    <rect x="225" y="82" width="90" height="64" rx="8" fill="#F1F5F9" />
    <circle cx="270" cy="106" r="14" fill="#E2E8F0" />
    <rect x="240" y="126" width="60" height="5" rx="2.5" fill="#CBD5E1" />
    <rect x="250" y="135" width="40" height="4" rx="2" fill="#E2E8F0" />
    
    <line x1="88" y1="172" x2="312" y2="172" stroke="#F1F5F9" stroke-width="2" stroke-linecap="round" />
  </g>

  <!-- Upward Fast Arrow -->
  <g filter="url(#shadow-card)">
    <circle cx="320" cy="55" r="26" fill="#FFFFFF" />
    <circle cx="320" cy="55" r="23" fill="url(#cyan-mint)" opacity="0.12" />
    <path d="M320 42L330 52M320 42L310 52M320 42V68" stroke="#10B981" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
  </g>

  <!-- Security Shield Badge -->
  <g filter="url(#shadow-card)">
    <path d="M45 125C45 125 75 120 75 95V70L45 60L15 70V95C15 120 45 125 45 125Z" fill="#FFFFFF" />
    <path d="M45 120C45 120 70 115 70 95V73.5L45 65L20 73.5V95C20 115 45 120 45 120Z" fill="url(#cyan-mint)" />
    <path d="M34 92L41 99L56 84" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_matching_v2.webp",
        "title": "安心して出会えるアプリを立ち上げる",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Connecting Arc Line -->
  <path d="M140 100C165 65 235 65 260 100" stroke="#0EA5E9" stroke-width="3" stroke-dasharray="6 6" opacity="0.6" />

  <!-- Left Smartphone -->
  <g filter="url(#shadow-card)">
    <rect x="85" y="42" width="85" height="156" rx="16" fill="#FFFFFF" />
    <rect x="91" y="48" width="73" height="144" rx="12" fill="#F8FAFC" />
    <!-- Speaker notch -->
    <rect x="115" y="53" width="25" height="3" rx="1.5" fill="#CBD5E1" />
    <!-- Profile Card on Phone 1 -->
    <rect x="97" y="66" width="61" height="75" rx="8" fill="#FFFFFF" />
    <circle cx="127.5" cy="95" r="15" fill="url(#cyan-mint)" opacity="0.8" />
    <rect x="105" y="118" width="45" height="5" rx="2.5" fill="#0F172A" />
    <rect x="110" y="126" width="35" height="4" rx="2" fill="#94A3B8" />
    <!-- Action buttons -->
    <circle cx="112" cy="162" r="10" fill="#E2E8F0" />
    <circle cx="143" cy="162" r="10" fill="url(#cyan-mint)" />
  </g>

  <!-- Right Smartphone -->
  <g filter="url(#shadow-card)">
    <rect x="230" y="42" width="85" height="156" rx="16" fill="#FFFFFF" />
    <rect x="236" y="48" width="73" height="144" rx="12" fill="#F8FAFC" />
    <rect x="260" y="53" width="25" height="3" rx="1.5" fill="#CBD5E1" />
    <!-- Profile Card on Phone 2 -->
    <rect x="242" y="66" width="61" height="75" rx="8" fill="#FFFFFF" />
    <circle cx="272.5" cy="95" r="15" fill="url(#mint-cyan)" opacity="0.8" />
    <rect x="250" y="118" width="45" height="5" rx="2.5" fill="#0F172A" />
    <rect x="255" y="126" width="35" height="4" rx="2" fill="#94A3B8" />
    <!-- Action buttons -->
    <circle cx="257" cy="162" r="10" fill="url(#mint-cyan)" />
    <circle cx="288" cy="162" r="10" fill="#E2E8F0" />
  </g>

  <!-- Center Floating Heart & Shield -->
  <g filter="url(#shadow-main)">
    <circle cx="200" cy="80" r="24" fill="#FFFFFF" />
    <!-- Heart Path -->
    <path d="M200 93C200 93 186 85 186 75.5C186 69.5 190.5 66 195.5 66C198.5 66 200 68 200 68C200 68 201.5 66 204.5 66C209.5 66 214 69.5 214 75.5C214 85 200 93 200 93Z" fill="url(#cyan-mint)" />
  </g>

  <g filter="url(#shadow-card)">
    <!-- Small Safety Shield Badge -->
    <path d="M200 152C200 152 216 148 216 136V122L200 116L184 122V136C184 148 200 152 200 152Z" fill="#FFFFFF" />
    <path d="M200 148C200 148 213 144 213 135V124L200 119L187 124V135C187 144 200 148 200 148Z" fill="#10B981" />
    <path d="M194 133L198 137L206 128" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_business_v2.webp",
        "title": "社内の資料をAIに聞いて探す",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Background Document Folder 1 -->
  <g filter="url(#shadow-main)">
    <rect x="75" y="65" width="145" height="115" rx="10" fill="#E2E8F0" />
    <path d="M75 75C75 69.477 79.477 65 85 65H115L128 78H210C215.523 78 220 82.477 220 88V170C220 175.523 215.523 180 210 180H85C79.477 180 75 175.523 75 170V75Z" fill="#CBD5E1" />
  </g>

  <!-- Foreground Main Folder with Documents -->
  <g filter="url(#shadow-card)">
    <rect x="88" y="78" width="145" height="115" rx="10" fill="#FFFFFF" />
    <path d="M88 88C88 82.477 92.477 78 98 78H128L141 91H223C228.523 91 233 95.477 233 101V183C233 188.523 228.523 193 223 193H98C92.477 193 88 188.523 88 183V88Z" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />
    
    <!-- Abstract Document Sheets Inside -->
    <rect x="105" y="110" width="70" height="6" rx="3" fill="#0F172A" />
    <rect x="105" y="123" width="95" height="5" rx="2.5" fill="#94A3B8" />
    <rect x="105" y="134" width="80" height="5" rx="2.5" fill="#CBD5E1" />
    <rect x="105" y="145" width="60" height="5" rx="2.5" fill="#E2E8F0" />

    <!-- Security Lock Badge on Folder -->
    <circle cx="195" cy="155" r="18" fill="#FFFFFF" filter="url(#shadow-card)" />
    <!-- Padlock Icon -->
    <rect x="187" y="150" width="16" height="13" rx="3" fill="#0EA5E9" />
    <path d="M190 150V144C190 141.791 191.791 140 194 140H196C198.209 140 200 141.791 200 144V150" stroke="#0EA5E9" stroke-width="2" stroke-linecap="round" />
    <circle cx="195" cy="156.5" r="1.5" fill="#FFFFFF" />
  </g>

  <!-- AI Response Chat Bubble -->
  <g filter="url(#shadow-main)">
    <!-- Speech Bubble Body -->
    <path d="M215 50C215 42.268 221.268 36 229 36H321C328.732 36 335 42.268 335 50V118C335 125.732 328.732 132 321 132H245L225 148V132H229C221.268 132 215 125.732 215 118V50Z" fill="#FFFFFF" />
    
    <!-- AI Sparkle Icon Header -->
    <path d="M236 58L238.5 64L244.5 66.5L238.5 69L236 75L233.5 69L227.5 66.5L233.5 64L236 58Z" fill="url(#cyan-mint)" />
    <rect x="252" y="62" width="60" height="7" rx="3.5" fill="#0F172A" />
    
    <!-- Answer lines inside bubble -->
    <rect x="232" y="80" width="85" height="5" rx="2.5" fill="#10B981" />
    <rect x="232" y="92" width="75" height="5" rx="2.5" fill="#94A3B8" />
    <rect x="232" y="104" width="55" height="5" rx="2.5" fill="#CBD5E1" />
  </g>

  <!-- Extra AI Sparkles -->
  <path d="M342 35L344 39L348 40.5L344 42L342 46L340 42L336 40.5L340 39L342 35Z" fill="#0EA5E9" />
  <path d="M205 32L206.5 35L209.5 36.5L206.5 38L205 41L203.5 38L200.5 36.5L203.5 35L205 32Z" fill="#10B981" />
</svg>
"""
    },
    {
        "filename": "illust_case_recruitment_v2.webp",
        "title": "履歴書から求人票づくりを助ける",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Left: Resume Sheet -->
  <g filter="url(#shadow-card)">
    <rect x="70" y="42" width="105" height="152" rx="10" fill="#FFFFFF" />
    <!-- Avatar circle -->
    <circle cx="98" cy="70" r="14" fill="#F1F5F9" />
    <circle cx="98" cy="66" r="6" fill="#94A3B8" />
    <path d="M89 78C89 74 93 72 98 72C103 72 107 74 107 78" stroke="#94A3B8" stroke-width="2" stroke-linecap="round" />
    <!-- Candidate Name and info lines -->
    <rect x="120" y="62" width="42" height="6" rx="3" fill="#0F172A" />
    <rect x="120" y="72" width="30" height="4" rx="2" fill="#94A3B8" />
    <!-- Divider -->
    <line x1="82" y1="94" x2="163" y2="94" stroke="#E2E8F0" stroke-width="1.5" />
    <!-- Experience bars -->
    <rect x="82" y="106" width="70" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="82" y="117" width="80" height="4" rx="2" fill="#CBD5E1" />
    <rect x="82" y="126" width="60" height="4" rx="2" fill="#E2E8F0" />
    <rect x="82" y="140" width="75" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="82" y="151" width="80" height="4" rx="2" fill="#CBD5E1" />
    <rect x="82" y="160" width="50" height="4" rx="2" fill="#E2E8F0" />
  </g>

  <!-- Center: Transition Arrow & AI Sparkles -->
  <g filter="url(#shadow-card)">
    <circle cx="200" cy="118" r="22" fill="#FFFFFF" />
    <path d="M192 118H208M208 118L202 112M208 118L202 124" stroke="url(#cyan-mint)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M200 85L202 89L206 90.5L202 92L200 96L198 92L194 90.5L198 89L200 85Z" fill="#10B981" />
  </g>

  <!-- Right: Generated Job Card -->
  <g filter="url(#shadow-main)">
    <rect x="225" y="42" width="115" height="152" rx="10" fill="#FFFFFF" />
    <!-- Job Title Badge -->
    <rect x="238" y="55" width="55" height="16" rx="8" fill="url(#cyan-mint)" />
    <rect x="245" y="61" width="41" height="4" rx="2" fill="#FFFFFF" />
    <!-- Job Heading -->
    <rect x="238" y="80" width="75" height="8" rx="4" fill="#0F172A" />
    <rect x="238" y="93" width="90" height="5" rx="2.5" fill="#94A3B8" />
    <!-- Checklist requirements -->
    <circle cx="244" cy="114" r="4" fill="#10B981" />
    <rect x="254" y="112" width="70" height="4" rx="2" fill="#0F172A" />
    <circle cx="244" cy="128" r="4" fill="#10B981" />
    <rect x="254" y="126" width="60" height="4" rx="2" fill="#0F172A" />
    <circle cx="244" cy="142" r="4" fill="#10B981" />
    <rect x="254" y="140" width="65" height="4" rx="2" fill="#0F172A" />
    <!-- Bottom Apply CTA Bar -->
    <rect x="238" y="160" width="89" height="18" rx="6" fill="#F1F5F9" />
    <rect x="260" y="166" width="45" height="6" rx="3" fill="#0EA5E9" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_video_feedback_v2.webp",
        "title": "面談の振り返りをAIが自動で作る",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Background: Video Player Screen -->
  <g filter="url(#shadow-main)">
    <rect x="65" y="42" width="195" height="135" rx="12" fill="#0F172A" />
    <!-- Video Player Screen UI -->
    <rect x="71" y="48" width="183" height="123" rx="8" fill="#1E293B" />
    
    <!-- Interview silhouette inside video -->
    <circle cx="140" cy="88" r="18" fill="#334155" />
    <path d="M115 125C115 110 126 108 140 108C154 108 165 110 165 125" fill="#334155" />
    
    <!-- Play Button (Cyan) -->
    <circle cx="185" cy="85" r="18" fill="url(#cyan-mint)" />
    <polygon points="181,77 193,85 181,93" fill="#FFFFFF" />

    <!-- Video Timeline Bar -->
    <rect x="80" y="152" width="165" height="6" rx="3" fill="#334155" />
    <rect x="80" y="152" width="95" height="6" rx="3" fill="#0EA5E9" />
    <circle cx="175" cy="155" r="6" fill="#FFFFFF" />
  </g>

  <!-- Foreground: AI Generated Report Sheet -->
  <g filter="url(#shadow-main)">
    <rect x="195" y="60" width="145" height="145" rx="10" fill="#FFFFFF" />
    
    <!-- Report Header & AI Sparkle -->
    <rect x="210" y="75" width="80" height="8" rx="4" fill="#0F172A" />
    <path d="M305 72L307.5 76L311.5 77.5L307.5 79L305 83L302.5 79L298.5 77.5L302.5 76L305 72Z" fill="url(#cyan-mint)" />
    
    <!-- Feedback Score Circle -->
    <circle cx="235" cy="115" r="18" stroke="#E2E8F0" stroke-width="4" />
    <path d="M235 97C244.941 97 253 105.059 253 115" stroke="#10B981" stroke-width="4" stroke-linecap="round" />
    <text x="235" y="119" font-family="'Noto Sans JP', sans-serif" font-weight="900" font-size="11" fill="#0F172A" text-anchor="middle">A+</text>

    <!-- Score Breakdown bars -->
    <rect x="265" y="105" width="60" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="265" y="116" width="50" height="5" rx="2.5" fill="#10B981" />
    <rect x="265" y="127" width="40" height="5" rx="2.5" fill="#CBD5E1" />

    <!-- Summary Checklist lines -->
    <line x1="210" y1="148" x2="325" y2="148" stroke="#F1F5F9" stroke-width="1.5" />
    <rect x="210" y="158" width="105" height="5" rx="2.5" fill="#94A3B8" />
    <rect x="210" y="170" width="85" height="5" rx="2.5" fill="#CBD5E1" />
    <rect x="210" y="182" width="95" height="5" rx="2.5" fill="#E2E8F0" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_staffing_crm_v2.webp",
        "title": "案件とスタッフ管理を<br>ひとつにまとめる",
        "multiline": True,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Convergence motion lines -->
  <path d="M85 65L120 85" stroke="#0EA5E9" stroke-width="2" stroke-dasharray="4 4" opacity="0.6" />
  <path d="M85 170L125 150" stroke="#10B981" stroke-width="2" stroke-dasharray="4 4" opacity="0.6" />
  <path d="M315 70L285 85" stroke="#0EA5E9" stroke-width="2" stroke-dasharray="4 4" opacity="0.6" />

  <!-- Center Unified CRM Dashboard -->
  <g filter="url(#shadow-main)">
    <rect x="110" y="42" width="200" height="152" rx="12" fill="#FFFFFF" />
    <!-- Top Header -->
    <path d="M110 54C110 47.373 115.373 42 122 42H298C304.627 42 310 47.373 310 54V64H110V54Z" fill="#F8FAFC" />
    <circle cx="125" cy="53" r="3.5" fill="#CBD5E1" />
    <circle cx="135" cy="53" r="3.5" fill="#E2E8F0" />
    <rect x="155" y="49" width="70" height="8" rx="4" fill="#0F172A" />

    <!-- Left Sidebar -->
    <rect x="110" y="64" width="45" height="130" fill="#F1F5F9" />
    <rect x="118" y="75" width="28" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="118" y="88" width="28" height="5" rx="2.5" fill="#CBD5E1" />
    <rect x="118" y="101" width="28" height="5" rx="2.5" fill="#CBD5E1" />
    <rect x="118" y="114" width="28" height="5" rx="2.5" fill="#CBD5E1" />

    <!-- Main Content Table & Cards -->
    <rect x="165" y="75" width="135" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <circle cx="178" cy="91" r="7" fill="url(#cyan-mint)" />
    <rect x="192" y="85" width="60" height="5" rx="2.5" fill="#0F172A" />
    <rect x="192" y="93" width="45" height="4" rx="2" fill="#94A3B8" />
    <rect x="268" y="86" width="24" height="10" rx="5" fill="#10B981" />

    <!-- Row 2 -->
    <rect x="165" y="115" width="135" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" />
    <circle cx="178" cy="131" r="7" fill="url(#mint-cyan)" />
    <rect x="192" y="125" width="55" height="5" rx="2.5" fill="#0F172A" />
    <rect x="192" y="133" width="40" height="4" rx="2" fill="#94A3B8" />
    <rect x="268" y="126" width="24" height="10" rx="5" fill="#0EA5E9" />

    <!-- Row 3 summary -->
    <rect x="165" y="155" width="135" height="26" rx="6" fill="#F1F5F9" />
    <rect x="175" y="165" width="50" height="6" rx="3" fill="#CBD5E1" />
    <rect x="250" y="165" width="40" height="6" rx="3" fill="url(#cyan-mint)" />
  </g>

  <!-- Left Top Card: Staff Profile -->
  <g filter="url(#shadow-card)">
    <rect x="45" y="45" width="60" height="50" rx="8" fill="#FFFFFF" />
    <circle cx="75" cy="62" r="9" fill="url(#cyan-mint)" />
    <rect x="55" y="78" width="40" height="4" rx="2" fill="#0F172A" />
    <rect x="60" y="85" width="30" height="3" rx="1.5" fill="#94A3B8" />
  </g>

  <!-- Left Bottom Card: Shift / Calendar -->
  <g filter="url(#shadow-card)">
    <rect x="48" y="145" width="60" height="50" rx="8" fill="#FFFFFF" />
    <!-- Clock / Shift Icon -->
    <circle cx="78" cy="162" r="9" fill="#10B981" opacity="0.15" stroke="#10B981" stroke-width="2" />
    <path d="M78 157V162H82" stroke="#10B981" stroke-width="2" stroke-linecap="round" />
    <rect x="58" y="178" width="40" height="4" rx="2" fill="#0F172A" />
    <rect x="63" y="185" width="30" height="3" rx="1.5" fill="#94A3B8" />
  </g>

  <!-- Right Top Card: Job Order -->
  <g filter="url(#shadow-card)">
    <rect x="295" y="60" width="60" height="50" rx="8" fill="#FFFFFF" />
    <rect x="307" y="70" width="36" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="307" y="80" width="36" height="4" rx="2" fill="#94A3B8" />
    <rect x="307" y="88" width="24" height="4" rx="2" fill="#CBD5E1" />
    <rect x="307" y="96" width="30" height="4" rx="2" fill="#10B981" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_disabled_community_v2.webp",
        "title": "だれもが使いやすい交流の場をつくる",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Left Friendly Speech Bubble -->
  <g filter="url(#shadow-card)">
    <path d="M75 58C75 49.163 82.163 42 91 42H135C143.837 42 151 49.163 151 58V92C151 100.837 143.837 108 135 108H105L88 120V108H91C82.163 108 75 100.837 75 92V58Z" fill="#FFFFFF" />
    <!-- Large Readable Text Bars -->
    <rect x="90" y="60" width="48" height="8" rx="4" fill="#0EA5E9" />
    <rect x="90" y="74" width="40" height="7" rx="3.5" fill="#0F172A" />
    <rect x="90" y="87" width="32" height="6" rx="3" fill="#94A3B8" />
  </g>

  <!-- Right Heart Message Bubble -->
  <g filter="url(#shadow-card)">
    <path d="M255 105C255 96.163 262.163 89 271 89H315C323.837 89 331 96.163 331 105V139C331 147.837 323.837 155 315 155H295L278 167V155H271C262.163 155 255 147.837 255 139V105Z" fill="#FFFFFF" />
    <!-- Heart Icon -->
    <path d="M293 125C293 125 282 119 282 112C282 107.5 285.5 105 289 105C291.5 105 293 106.5 293 106.5C293 106.5 294.5 105 297 105C300.5 105 304 107.5 304 112C304 119 293 125 293 125Z" fill="#10B981" />
    <rect x="276" y="134" width="34" height="6" rx="3" fill="#94A3B8" />
  </g>

  <!-- Center Accessible Smartphone -->
  <g filter="url(#shadow-main)">
    <rect x="145" y="32" width="110" height="176" rx="18" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <rect x="153" y="40" width="94" height="160" rx="12" fill="#F8FAFC" />
    
    <!-- Top Speaker Notch -->
    <rect x="185" y="46" width="30" height="3" rx="1.5" fill="#CBD5E1" />
    
    <!-- Audio Waveform / Speech Assist Feature -->
    <rect x="162" y="62" width="76" height="50" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
    <!-- Speaker Icon -->
    <path d="M172 87H177L183 93V81L177 87H172V87Z" fill="#0EA5E9" />
    <!-- Waveform Lines -->
    <rect x="192" y="82" width="3" height="10" rx="1.5" fill="url(#cyan-mint)" />
    <rect x="199" y="76" width="3" height="22" rx="1.5" fill="url(#cyan-mint)" />
    <rect x="206" y="72" width="3" height="30" rx="1.5" fill="url(#cyan-mint)" />
    <rect x="213" y="78" width="3" height="18" rx="1.5" fill="url(#cyan-mint)" />
    <rect x="220" y="83" width="3" height="8" rx="1.5" fill="url(#cyan-mint)" />

    <!-- Accessible Card with High Contrast UI -->
    <rect x="162" y="122" width="76" height="42" rx="8" fill="#FFFFFF" />
    <!-- Big Text Bar -->
    <rect x="170" y="132" width="55" height="10" rx="5" fill="#0F172A" />
    <rect x="170" y="146" width="40" height="7" rx="3.5" fill="#10B981" />

    <!-- Easy Tap Bottom Button -->
    <rect x="162" y="172" width="76" height="18" rx="9" fill="url(#cyan-mint)" />
    <circle cx="200" cy="181" r="4" fill="#FFFFFF" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_ma_contracts_v2.webp",
        "title": "契約書の下書きと確認をAIで速くする",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Main Contract Clipboard -->
  <g filter="url(#shadow-main)">
    <!-- Clipboard Board -->
    <rect x="110" y="32" width="150" height="175" rx="10" fill="#E2E8F0" />
    <!-- Clip on top -->
    <rect x="155" y="24" width="60" height="16" rx="4" fill="#0F172A" />
    <circle cx="185" cy="32" r="3.5" fill="#FFFFFF" />

    <!-- Contract Paper Sheet -->
    <rect x="120" y="42" width="130" height="155" rx="6" fill="#FFFFFF" />
    
    <!-- Title: Contract Header -->
    <rect x="135" y="58" width="75" height="9" rx="4.5" fill="#0F172A" />
    <line x1="135" y1="74" x2="235" y2="74" stroke="#E2E8F0" stroke-width="1.5" />
    
    <!-- Contract Clauses Lines -->
    <rect x="135" y="84" width="100" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="135" y="94" width="85" height="4" rx="2" fill="#94A3B8" />
    <rect x="135" y="103" width="95" height="4" rx="2" fill="#CBD5E1" />
    
    <rect x="135" y="117" width="90" height="5" rx="2.5" fill="#0EA5E9" />
    <rect x="135" y="127" width="100" height="4" rx="2" fill="#94A3B8" />
    <rect x="135" y="136" width="70" height="4" rx="2" fill="#CBD5E1" />

    <rect x="135" y="150" width="85" height="5" rx="2.5" fill="#94A3B8" />
    <rect x="135" y="160" width="90" height="4" rx="2" fill="#CBD5E1" />

    <!-- Official Seal / Stamp Symbol -->
    <circle cx="225" cy="175" r="9" stroke="#10B981" stroke-width="2" />
    <rect x="221" y="171" width="8" height="8" fill="#10B981" rx="1" />
  </g>

  <!-- Big Magnifying Glass (AI Audit & Inspection) -->
  <g filter="url(#shadow-main)">
    <!-- Lens Rim & Glass -->
    <circle cx="245" cy="115" r="38" fill="#FFFFFF" fill-opacity="0.85" stroke="#0EA5E9" stroke-width="6" />
    <circle cx="245" cy="115" r="33" fill="url(#cyan-mint)" fill-opacity="0.1" />
    
    <!-- Big Green Verification Checkmark Inside Lens -->
    <path d="M232 114L241 123L258 106" stroke="#10B981" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />

    <!-- Lens Glass Reflection Arc -->
    <path d="M225 95C235 88 255 88 265 95" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />

    <!-- Handle -->
    <line x1="272" y1="142" x2="305" y2="175" stroke="#0F172A" stroke-width="10" stroke-linecap="round" />
    <line x1="273" y1="143" x2="303" y2="173" stroke="#334155" stroke-width="6" stroke-linecap="round" />
  </g>

  <!-- AI Fast Analysis Sparkles -->
  <path d="M305 60L308 65L313 67L308 69L305 74L302 69L297 67L302 65L305 60Z" fill="url(#cyan-mint)" />
  <path d="M100 45L102 48L105 49.5L102 51L100 54L98 51L95 49.5L98 48L100 45Z" fill="#10B981" />
</svg>
"""
    },
    {
        "filename": "illust_case_filemaker_v2.webp",
        "title": "遅い社内データベースを速くする",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Left: 3-Tier Database Cylinder -->
  <g filter="url(#shadow-main)">
    <!-- Base / Tier 3 -->
    <path d="M80 145C80 137 105 130 135 130C165 130 190 137 190 145V170C190 178 165 185 135 185C105 185 80 178 80 170V145Z" fill="#E2E8F0" />
    <ellipse cx="135" cy="145" rx="55" ry="14" fill="#FFFFFF" />
    <circle cx="170" cy="162" r="3.5" fill="#10B981" />
    <rect x="98" y="158" width="40" height="5" rx="2.5" fill="#94A3B8" />

    <!-- Tier 2 -->
    <path d="M80 105C80 97 105 90 135 90C165 90 190 97 190 105V130C190 138 165 145 135 145C105 145 80 138 80 130V105Z" fill="#CBD5E1" />
    <ellipse cx="135" cy="105" rx="55" ry="14" fill="#FFFFFF" />
    <circle cx="170" cy="122" r="3.5" fill="#0EA5E9" />
    <rect x="98" y="118" width="48" height="5" rx="2.5" fill="#0F172A" />

    <!-- Tier 1 (Top) -->
    <path d="M80 65C80 57 105 50 135 50C165 50 190 57 190 65V90C190 98 165 105 135 105C105 105 80 98 80 90V65Z" fill="#F8FAFC" />
    <ellipse cx="135" cy="65" rx="55" ry="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <circle cx="170" cy="82" r="3.5" fill="url(#cyan-mint)" />
    <rect x="98" y="78" width="55" height="5" rx="2.5" fill="url(#cyan-mint)" />
  </g>

  <!-- Right: Speedometer Gauge -->
  <g filter="url(#shadow-main)">
    <circle cx="265" cy="115" r="58" fill="#FFFFFF" />
    
    <!-- Gauge Outer Track Arc -->
    <path d="M225 140A48 48 0 1 1 305 140" fill="none" stroke="#E2E8F0" stroke-width="10" stroke-linecap="round" />
    <!-- Fast High Speed Zone Arc (Cyan to Mint) -->
    <path d="M265 67A48 48 0 0 1 305 140" fill="none" stroke="url(#cyan-mint)" stroke-width="10" stroke-linecap="round" />

    <!-- Ticks -->
    <circle cx="233" cy="115" r="2.5" fill="#94A3B8" />
    <circle cx="245" cy="85" r="2.5" fill="#94A3B8" />
    <circle cx="265" cy="77" r="3" fill="#0F172A" />
    <circle cx="288" cy="88" r="3" fill="#10B981" />

    <!-- Gauge Center Hub -->
    <circle cx="265" cy="120" r="12" fill="#0F172A" />
    <circle cx="265" cy="120" r="5" fill="#FFFFFF" />

    <!-- Gauge Needle pointing to MAX (Fast) -->
    <line x1="265" y1="120" x2="295" y2="92" stroke="#10B981" stroke-width="4.5" stroke-linecap="round" />

    <!-- Speed Indicator lines -->
    <path d="M312 85L325 80" stroke="#10B981" stroke-width="3" stroke-linecap="round" />
    <path d="M320 102L335 102" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round" />
    <path d="M315 120L328 125" stroke="#0EA5E9" stroke-width="2.5" stroke-linecap="round" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_gcp_migration_v2.webp",
        "title": "古いサーバーをクラウドへ引っ越す",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Migration Rising Arrow from On-Premise to Cloud -->
  <path d="M145 130C165 80 205 75 235 85" stroke="url(#cyan-mint)" stroke-width="5" stroke-linecap="round" stroke-dasharray="8 6" />
  <polygon points="245,88 232,80 236,94" fill="#10B981" />

  <!-- Left Bottom: Legacy Server Box -->
  <g filter="url(#shadow-main)">
    <rect x="70" y="105" width="105" height="95" rx="10" fill="#0F172A" />
    
    <!-- Server Unit 1 -->
    <rect x="78" y="115" width="89" height="22" rx="4" fill="#1E293B" />
    <circle cx="88" cy="126" r="3" fill="#94A3B8" />
    <line x1="97" y1="126" x2="125" y2="126" stroke="#475569" stroke-width="3" stroke-linecap="round" />
    <circle cx="155" cy="126" r="2.5" fill="#0EA5E9" />

    <!-- Server Unit 2 -->
    <rect x="78" y="142" width="89" height="22" rx="4" fill="#1E293B" />
    <circle cx="88" cy="153" r="3" fill="#94A3B8" />
    <line x1="97" y1="153" x2="135" y2="153" stroke="#475569" stroke-width="3" stroke-linecap="round" />
    <circle cx="155" cy="153" r="2.5" fill="#10B981" />

    <!-- Server Unit 3 -->
    <rect x="78" y="169" width="89" height="22" rx="4" fill="#1E293B" />
    <circle cx="88" cy="180" r="3" fill="#94A3B8" />
    <line x1="97" y1="180" x2="115" y2="180" stroke="#475569" stroke-width="3" stroke-linecap="round" />
    <circle cx="155" cy="180" r="2.5" fill="#0EA5E9" />
  </g>

  <!-- Right Top: Modern Cloud -->
  <g filter="url(#shadow-main)">
    <!-- Cloud Silhouette Path -->
    <path d="M255 130H315C328.807 130 340 118.807 340 105C340 92.5 330.5 82.2 318.5 80.4C316.5 61.2 300 46 280 46C262.8 46 248.2 57.5 243.5 73.5C236.5 74.5 230 80.5 230 88C230 96.5 236.5 103.5 245 104.5C245.5 104.5 245.8 104.5 246 104.5C246 118.5 250 130 255 130Z" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2" />
    
    <!-- Cloud Inner Highlights -->
    <circle cx="280" cy="85" r="18" fill="url(#cyan-mint)" opacity="0.15" />
    <path d="M272 85L278 91L292 77" stroke="#10B981" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
  </g>

  <!-- Fast Cloud Speed Stars -->
  <path d="M340 55L342 58L345 59.5L342 61L340 64L338 61L335 59.5L338 58L340 55Z" fill="#0EA5E9" />
  <path d="M225 45L227 48L230 49.5L227 51L225 54L223 51L220 49.5L223 48L225 45Z" fill="#10B981" />
</svg>
"""
    },
    {
        "filename": "illust_case_cloud_security_v2.webp",
        "title": "クラウドの守りをまとめて固める",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Cloud Background Element -->
  <g filter="url(#shadow-card)">
    <path d="M125 125H225C238.807 125 250 113.807 250 100C250 87.5 240.5 77.2 228.5 75.4C226.5 56.2 210 41 190 41C172.8 41 158.2 52.5 153.5 68.5C146.5 69.5 140 75.5 140 83C140 91.5 146.5 98.5 155 99.5C155 113.5 150 125 125 125Z" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="2" />
  </g>

  <!-- Big Security Shield Protecting Cloud -->
  <g filter="url(#shadow-main)">
    <!-- White Shield Base -->
    <path d="M175 185C175 185 225 175 225 130V75L175 58L125 75V130C125 175 175 185 175 185Z" fill="#FFFFFF" />
    <!-- Gradient Shield Inset -->
    <path d="M175 178C175 178 218 168 218 130V81L175 66L132 81V130C132 168 175 178 175 178Z" fill="url(#cyan-mint)" />
    <!-- Keyhole Emblem inside Shield -->
    <circle cx="175" cy="115" r="12" fill="#FFFFFF" />
    <path d="M171 122L168 140H182L179 122" fill="#FFFFFF" />
  </g>

  <!-- Right Checklist Sheet -->
  <g filter="url(#shadow-main)">
    <rect x="250" y="65" width="95" height="120" rx="8" fill="#FFFFFF" />
    <rect x="262" y="78" width="55" height="6" rx="3" fill="#0F172A" />
    
    <!-- Item 1 Check -->
    <circle cx="268" cy="102" r="6" fill="#10B981" />
    <path d="M265 102L267 104L271 99" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
    <rect x="280" y="99" width="50" height="5" rx="2.5" fill="#94A3B8" />

    <!-- Item 2 Check -->
    <circle cx="268" cy="122" r="6" fill="#10B981" />
    <path d="M265 122L267 124L271 119" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
    <rect x="280" y="119" width="45" height="5" rx="2.5" fill="#94A3B8" />

    <!-- Item 3 Check -->
    <circle cx="268" cy="142" r="6" fill="#10B981" />
    <path d="M265 142L267 144L271 139" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
    <rect x="280" y="139" width="55" height="5" rx="2.5" fill="#94A3B8" />

    <!-- Item 4 (Safe seal) -->
    <rect x="262" y="160" width="71" height="12" rx="6" fill="#F1F5F9" />
    <rect x="272" y="164" width="51" height="4" rx="2" fill="#0EA5E9" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_food_recruitment_v2.webp",
        "title": "店舗の採用を一か所で管理する",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Network Connection Lines from Shops to Center Hub -->
  <path d="M100 135C125 105 145 95 170 95" stroke="#0EA5E9" stroke-width="2.5" stroke-dasharray="5 5" opacity="0.6" />
  <path d="M300 135C275 105 255 95 230 95" stroke="#10B981" stroke-width="2.5" stroke-dasharray="5 5" opacity="0.6" />

  <!-- Center: Unified Admin Console Screen -->
  <g filter="url(#shadow-main)">
    <rect x="135" y="35" width="130" height="95" rx="10" fill="#FFFFFF" />
    <!-- Browser/App Header -->
    <rect x="135" y="35" width="130" height="18" rx="6" fill="#F8FAFC" />
    <circle cx="145" cy="44" r="3" fill="#CBD5E1" />
    <circle cx="153" cy="44" r="3" fill="#E2E8F0" />
    
    <!-- Admin Dashboard Content -->
    <rect x="145" y="62" width="50" height="6" rx="3" fill="#0F172A" />
    
    <!-- Candidate row 1 -->
    <rect x="145" y="76" width="110" height="18" rx="4" fill="#F1F5F9" />
    <circle cx="154" cy="85" r="4.5" fill="url(#cyan-mint)" />
    <rect x="165" y="82" width="40" height="4" rx="2" fill="#0F172A" />
    <rect x="235" y="81" width="15" height="8" rx="4" fill="#10B981" />

    <!-- Candidate row 2 -->
    <rect x="145" y="100" width="110" height="18" rx="4" fill="#F1F5F9" />
    <circle cx="154" cy="109" r="4.5" fill="url(#mint-cyan)" />
    <rect x="165" y="106" width="35" height="4" rx="2" fill="#0F172A" />
    <rect x="235" y="105" width="15" height="8" rx="4" fill="#0EA5E9" />
  </g>

  <!-- Left Shop Building 1 -->
  <g filter="url(#shadow-card)">
    <rect x="55" y="125" width="85" height="75" rx="6" fill="#FFFFFF" />
    <!-- Striped Awning (Canopy) -->
    <path d="M52 125H143L138 140H57L52 125Z" fill="#0EA5E9" />
    <path d="M68 125L71 140M86 125L87 140M105 125L104 140M123 125L120 140" stroke="#FFFFFF" stroke-width="3" />
    <!-- Store Door & Window -->
    <rect x="70" y="155" width="22" height="45" rx="3" fill="#F1F5F9" stroke="#E2E8F0" />
    <rect x="102" y="155" width="25" height="25" rx="4" fill="#F8FAFC" stroke="#E2E8F0" />
    <circle cx="114" cy="167" r="5" fill="#10B981" opacity="0.3" />
  </g>

  <!-- Right Shop Building 2 -->
  <g filter="url(#shadow-card)">
    <rect x="260" y="125" width="85" height="75" rx="6" fill="#FFFFFF" />
    <!-- Striped Awning -->
    <path d="M257 125H348L343 140H262L257 125Z" fill="#10B981" />
    <path d="M273 125L276 140M291 125L292 140M310 125L309 140M328 125L325 140" stroke="#FFFFFF" stroke-width="3" />
    <!-- Store Door & Window -->
    <rect x="308" y="155" width="22" height="45" rx="3" fill="#F1F5F9" stroke="#E2E8F0" />
    <rect x="273" y="155" width="25" height="25" rx="4" fill="#F8FAFC" stroke="#E2E8F0" />
    <circle cx="285" cy="167" r="5" fill="#0EA5E9" opacity="0.3" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_expat_matching_v2.webp",
        "title": "言葉の壁をこえて交流できるアプリ",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Global Wireframe Background -->
  <circle cx="200" cy="115" r="70" stroke="#E2E8F0" stroke-width="1.5" stroke-dasharray="4 4" />
  <ellipse cx="200" cy="115" rx="70" ry="25" stroke="#E2E8F0" stroke-width="1.5" />
  <ellipse cx="200" cy="115" rx="25" ry="70" stroke="#E2E8F0" stroke-width="1.5" />

  <!-- Left: English/Latin "A" Chat Bubble -->
  <g filter="url(#shadow-main)">
    <path d="M70 70C70 58.954 78.954 50 90 50H150C161.046 50 170 58.954 170 70V110C170 121.046 161.046 130 150 130H110L85 145V130H90C78.954 130 70 121.046 70 110V70Z" fill="#FFFFFF" />
    <!-- Big Letter 'A' -->
    <text x="120" y="103" font-family="'Noto Sans JP', sans-serif" font-weight="900" font-size="36" fill="#0EA5E9" text-anchor="middle">A</text>
  </g>

  <!-- Right: Japanese "あ" Chat Bubble -->
  <g filter="url(#shadow-main)">
    <path d="M230 70C230 58.954 238.954 50 250 50H310C321.046 50 330 58.954 330 70V110C330 121.046 321.046 130 310 130H270L245 145V130H250C238.954 130 230 121.046 230 110V70Z" fill="#FFFFFF" />
    <!-- Big Letter 'あ' -->
    <text x="280" y="103" font-family="'Noto Sans JP', sans-serif" font-weight="900" font-size="34" fill="#10B981" text-anchor="middle">あ</text>
  </g>

  <!-- Center Dynamic Translation Arrows Loop -->
  <g filter="url(#shadow-card)">
    <!-- Top Arrow (Left to Right, Cyan) -->
    <path d="M178 78C188 68 212 68 222 78" stroke="#0EA5E9" stroke-width="4" stroke-linecap="round" />
    <polygon points="225,82 224,71 214,77" fill="#0EA5E9" />

    <!-- Bottom Arrow (Right to Left, Mint) -->
    <path d="M222 102C212 112 188 112 178 102" stroke="#10B981" stroke-width="4" stroke-linecap="round" />
    <polygon points="175,98 176,109 186,103" fill="#10B981" />
  </g>

  <!-- Cultural Sparkle Dots -->
  <circle cx="190" cy="50" r="4" fill="#10B981" />
  <circle cx="210" cy="135" r="4" fill="#0EA5E9" />
</svg>
"""
    },
    {
        "filename": "illust_case_rental_car_v2.webp",
        "title": "多言語で予約できるサイトをつくる",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Background Calendar Sheet -->
  <g filter="url(#shadow-card)">
    <rect x="75" y="42" width="95" height="95" rx="8" fill="#FFFFFF" />
    <path d="M75 52C75 46.477 79.477 42 85 42H160C165.523 42 170 46.477 170 52V62H75V52Z" fill="#0EA5E9" />
    <circle cx="95" cy="52" r="2.5" fill="#FFFFFF" />
    <circle cx="150" cy="52" r="2.5" fill="#FFFFFF" />
    <!-- Calendar Grid Ticks -->
    <rect x="88" y="74" width="14" height="12" rx="3" fill="#F1F5F9" />
    <rect x="110" y="74" width="14" height="12" rx="3" fill="#F1F5F9" />
    <rect x="132" y="74" width="14" height="12" rx="3" fill="url(#cyan-mint)" />
    <rect x="88" y="94" width="14" height="12" rx="3" fill="#F1F5F9" />
    <rect x="110" y="94" width="14" height="12" rx="3" fill="#10B981" />
    <rect x="132" y="94" width="14" height="12" rx="3" fill="#F1F5F9" />
  </g>

  <!-- Background Global Multilingual Globe -->
  <g filter="url(#shadow-card)">
    <circle cx="280" cy="85" r="42" fill="#FFFFFF" />
    <circle cx="280" cy="85" r="36" stroke="url(#cyan-mint)" stroke-width="2" fill="none" />
    <ellipse cx="280" cy="85" rx="36" ry="14" stroke="#0EA5E9" stroke-width="1.5" fill="none" />
    <ellipse cx="280" cy="85" rx="14" ry="36" stroke="#10B981" stroke-width="1.5" fill="none" />
  </g>

  <!-- Foreground Modern Rental Car Silhouette -->
  <g filter="url(#shadow-main)">
    <!-- Car Body -->
    <path d="M110 160L125 130C130 120 142 115 155 115H235C248 115 260 122 265 133L285 160H295C300.523 160 305 164.477 305 170V180H95V170C95 164.477 99.477 160 105 160H110Z" fill="#FFFFFF" />
    <!-- Car Windows -->
    <path d="M135 132L145 122H190V152H125L135 132Z" fill="#0EA5E9" fill-opacity="0.2" stroke="#0EA5E9" stroke-width="1.5" />
    <path d="M198 122H230C238 122 245 126 248 134L262 152H198V122Z" fill="#0EA5E9" fill-opacity="0.2" stroke="#0EA5E9" stroke-width="1.5" />
    
    <!-- Accent side stripe -->
    <path d="M100 162H300" stroke="url(#cyan-mint)" stroke-width="3" />

    <!-- Front & Rear Wheels -->
    <circle cx="140" cy="180" r="18" fill="#0F172A" />
    <circle cx="140" cy="180" r="8" fill="#FFFFFF" />
    <circle cx="260" cy="180" r="18" fill="#0F172A" />
    <circle cx="260" cy="180" r="8" fill="#FFFFFF" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_sns_app_v2.webp",
        "title": "自分たちのSNSを立ち上げる",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Floating Reaction Badges -->
  <g filter="url(#shadow-card)">
    <circle cx="95" cy="75" r="20" fill="#FFFFFF" />
    <!-- Speech bubble icon -->
    <path d="M87 75C87 70.5 91 67 96 67C101 67 105 70.5 105 75C105 79.5 101 83 96 83H92L87 87V75Z" fill="#0EA5E9" />
  </g>

  <g filter="url(#shadow-card)">
    <circle cx="305" cy="140" r="22" fill="#FFFFFF" />
    <!-- Heart icon -->
    <path d="M305 149C305 149 295 143 295 137C295 133 298 131 301 131C303 131 305 132.5 305 132.5C305 132.5 307 131 309 131C312 131 315 133 315 137C315 143 305 149 305 149Z" fill="#10B981" />
  </g>

  <!-- Center Smartphone with Timeline UI -->
  <g filter="url(#shadow-main)">
    <rect x="135" y="30" width="130" height="185" rx="18" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <rect x="143" y="38" width="114" height="169" rx="12" fill="#F8FAFC" />
    
    <!-- Top Notch -->
    <rect x="175" y="44" width="30" height="3" rx="1.5" fill="#CBD5E1" />

    <!-- Timeline Post 1 -->
    <rect x="149" y="58" width="102" height="42" rx="8" fill="#FFFFFF" />
    <circle cx="162" cy="72" r="6" fill="url(#cyan-mint)" />
    <rect x="174" y="68" width="45" height="5" rx="2.5" fill="#0F172A" />
    <rect x="174" y="76" width="68" height="4" rx="2" fill="#94A3B8" />
    <circle cx="235" cy="90" r="3" fill="#10B981" />
    <circle cx="243" cy="90" r="3" fill="#0EA5E9" />

    <!-- Timeline Post 2 (Featured with image block) -->
    <rect x="149" y="106" width="102" height="52" rx="8" fill="#FFFFFF" />
    <circle cx="162" cy="120" r="6" fill="url(#mint-cyan)" />
    <rect x="174" y="116" width="50" height="5" rx="2.5" fill="#0F172A" />
    <rect x="174" y="124" width="70" height="4" rx="2" fill="#94A3B8" />
    <!-- Mini Media Rectangle -->
    <rect x="174" y="132" width="65" height="18" rx="4" fill="#F1F5F9" />

    <!-- Timeline Post 3 -->
    <rect x="149" y="164" width="102" height="36" rx="8" fill="#FFFFFF" />
    <circle cx="162" cy="178" r="6" fill="#0EA5E9" />
    <rect x="174" y="174" width="40" height="5" rx="2.5" fill="#0F172A" />
    <rect x="174" y="182" width="60" height="4" rx="2" fill="#94A3B8" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_telemedicine_v2.webp",
        "title": "自宅から診察を受けられるアプリ",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Stethoscope Tube wrapping behind phone -->
  <path d="M125 155C90 145 75 110 85 80C95 50 130 45 155 52" stroke="#0F172A" stroke-width="4.5" stroke-linecap="round" fill="none" />
  <path d="M245 52C270 45 305 50 315 80C325 110 310 145 275 155" stroke="#0F172A" stroke-width="4.5" stroke-linecap="round" fill="none" />

  <!-- Medical Cross Badge -->
  <g filter="url(#shadow-card)">
    <circle cx="295" cy="65" r="18" fill="#FFFFFF" />
    <path d="M295 56V74M286 65H304" stroke="#10B981" stroke-width="4" stroke-linecap="round" />
  </g>

  <!-- Center Smartphone with Video Consultation -->
  <g filter="url(#shadow-main)">
    <rect x="140" y="32" width="120" height="176" rx="18" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <rect x="148" y="40" width="104" height="160" rx="12" fill="#0F172A" />
    
    <!-- Video Screen Inner: Doctor Silhouette -->
    <rect x="150" y="42" width="100" height="156" rx="10" fill="#1E293B" />
    <circle cx="200" cy="85" r="18" fill="#FFFFFF" />
    <path d="M178 128C178 112 188 108 200 108C212 108 222 112 222 128" fill="#FFFFFF" />
    <!-- Doctor Stethoscope & tie hint -->
    <path d="M195 108V118L200 122L205 118V108" stroke="#0EA5E9" stroke-width="2" />

    <!-- Patient Picture-in-Picture Mini Wipe -->
    <rect x="210" y="50" width="34" height="42" rx="6" fill="#334155" stroke="#FFFFFF" stroke-width="1.5" />
    <circle cx="227" cy="66" r="6" fill="#94A3B8" />

    <!-- Video Controls: Microphone & Call End -->
    <circle cx="180" cy="170" r="11" fill="#334155" />
    <rect x="178" y="165" width="4" height="7" rx="2" fill="#FFFFFF" />
    <circle cx="210" cy="170" r="11" fill="#10B981" />
    <path d="M205 170L208 173L215 166" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
  </g>

  <!-- Stethoscope Chestpiece in foreground -->
  <g filter="url(#shadow-main)">
    <circle cx="130" cy="170" r="18" fill="#FFFFFF" />
    <circle cx="130" cy="170" r="14" fill="#0EA5E9" />
    <circle cx="130" cy="170" r="7" fill="#FFFFFF" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_pharmacy_inventory_v2.webp",
        "title": "薬の在庫のムダを減らす",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Medicine Shelf Rack in Background -->
  <g filter="url(#shadow-main)">
    <rect x="90" y="42" width="180" height="145" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <!-- Shelf 1 Divider -->
    <line x1="90" y1="95" x2="270" y2="95" stroke="#E2E8F0" stroke-width="3" />
    <!-- Shelf 2 Divider -->
    <line x1="90" y1="145" x2="270" y2="145" stroke="#E2E8F0" stroke-width="3" />

    <!-- Top Shelf Items (Medicine Bottles & Boxes) -->
    <rect x="105" y="60" width="22" height="32" rx="4" fill="#0EA5E9" />
    <rect x="110" y="55" width="12" height="5" rx="2" fill="#FFFFFF" stroke="#0EA5E9" />
    <rect x="135" y="66" width="30" height="26" rx="4" fill="#10B981" />
    <rect x="173" y="58" width="24" height="34" rx="4" fill="#F1F5F9" stroke="#94A3B8" />
    <rect x="205" y="64" width="32" height="28" rx="4" fill="#0F172A" />

    <!-- Middle Shelf Items -->
    <rect x="105" y="112" width="34" height="30" rx="4" fill="#F1F5F9" stroke="#0EA5E9" />
    <rect x="147" y="108" width="25" height="34" rx="4" fill="url(#cyan-mint)" />
    <rect x="180" y="115" width="28" height="27" rx="4" fill="#10B981" />
    <rect x="216" y="110" width="34" height="32" rx="4" fill="#CBD5E1" />

    <!-- Bottom Shelf Base -->
    <rect x="105" y="160" width="150" height="15" rx="4" fill="#F8FAFC" />
  </g>

  <!-- Left: Barcode Scanner Beam Element -->
  <g filter="url(#shadow-card)">
    <rect x="55" y="110" width="60" height="42" rx="6" fill="#FFFFFF" />
    <!-- Barcode Lines -->
    <line x1="65" y1="118" x2="65" y2="142" stroke="#0F172A" stroke-width="3" />
    <line x1="72" y1="118" x2="72" y2="142" stroke="#0F172A" stroke-width="1.5" />
    <line x1="77" y1="118" x2="77" y2="142" stroke="#0F172A" stroke-width="4" />
    <line x1="85" y1="118" x2="85" y2="142" stroke="#0F172A" stroke-width="2" />
    <line x1="92" y1="118" x2="92" y2="142" stroke="#0F172A" stroke-width="3" />
    <line x1="100" y1="118" x2="100" y2="142" stroke="#0F172A" stroke-width="1.5" />
    <!-- Red/Cyan Laser Scan Line across -->
    <line x1="50" y1="130" x2="120" y2="130" stroke="#0EA5E9" stroke-width="2.5" />
  </g>

  <!-- Right: Alert Notification Bell (Prevention of Waste/Shortage) -->
  <g filter="url(#shadow-main)">
    <circle cx="285" cy="115" r="30" fill="#FFFFFF" />
    <!-- Bell Icon -->
    <path d="M285 96C282.5 96 280.5 98 280.5 100.5V102C275 104 271 109 271 116V124L267 128V130H303V128L299 124V116C299 109 295 104 289.5 102V100.5C289.5 98 287.5 96 285 96Z" fill="#10B981" />
    <circle cx="285" cy="134" r="3.5" fill="#10B981" />
    
    <!-- Sound Wave Ring -->
    <path d="M305 110C307 113 307 117 305 120" stroke="#0EA5E9" stroke-width="2.5" stroke-linecap="round" />
  </g>
</svg>
"""
    },
    {
        "filename": "illust_case_delivery_lp_v2.webp",
        "title": "デリバリーの利点がひと目で伝わる",
        "multiline": False,
        "svg_content": f"""
<svg width="400" height="240" viewBox="0 0 400 240" fill="none" xmlns="http://www.w3.org/2000/svg">
{SVG_DEFS}
  <!-- Left: Takeout / Delivery Paper Bag -->
  <g filter="url(#shadow-main)">
    <!-- Bag Body -->
    <path d="M75 80L90 65H180L195 80L185 185H85L75 80Z" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <!-- Bag Handle Cutout -->
    <rect x="115" y="75" width="40" height="12" rx="6" fill="#F1F5F9" stroke="#E2E8F0" />
    
    <!-- Emblem / Cutlery Icon on Bag -->
    <circle cx="135" cy="125" r="24" fill="url(#cyan-mint)" opacity="0.12" />
    <!-- Fork & Spoon -->
    <path d="M128 114V136M124 114V122C124 124 126 126 128 126C130 126 132 124 132 122V114" stroke="#10B981" stroke-width="2.5" stroke-linecap="round" />
    <path d="M142 114C138 114 136 118 136 122C136 125 138 127 141 127V136" stroke="#0EA5E9" stroke-width="2.5" stroke-linecap="round" />
    
    <!-- Quality Check Ribbon -->
    <rect x="110" y="152" width="50" height="6" rx="3" fill="#0F172A" />
  </g>

  <!-- Right: Landing Page Smartphone Screen -->
  <g filter="url(#shadow-main)">
    <rect x="195" y="32" width="125" height="176" rx="18" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
    <rect x="203" y="40" width="109" height="160" rx="12" fill="#F8FAFC" />
    
    <!-- Top Speaker -->
    <rect x="238" y="46" width="30" height="3" rx="1.5" fill="#CBD5E1" />

    <!-- LP Hero Banner on Phone -->
    <rect x="210" y="56" width="95" height="48" rx="8" fill="url(#cyan-mint)" />
    <!-- Hero content lines -->
    <rect x="218" y="66" width="60" height="7" rx="3.5" fill="#FFFFFF" />
    <rect x="218" y="77" width="45" height="5" rx="2.5" fill="#FFFFFF" opacity="0.8" />

    <!-- LP Benefit 3 Points (Checkmarks) -->
    <circle cx="218" cy="116" r="3.5" fill="#10B981" />
    <rect x="226" y="114" width="68" height="4" rx="2" fill="#0F172A" />
    <circle cx="218" cy="128" r="3.5" fill="#10B981" />
    <rect x="226" y="126" width="58" height="4" rx="2" fill="#0F172A" />
    <circle cx="218" cy="140" r="3.5" fill="#10B981" />
    <rect x="226" y="138" width="62" height="4" rx="2" fill="#0F172A" />

    <!-- High CVR CTA Button -->
    <rect x="210" y="156" width="95" height="22" rx="11" fill="url(#mint-cyan)" />
    <rect x="228" y="164" width="58" height="6" rx="3" fill="#FFFFFF" />
  </g>
</svg>
"""
    }
]

def generate_banner_html(case):
    multiline = case.get("multiline", False)
    title_html = case["title"]
    font_size = "40px" if multiline else "46px"
    line_height = "1.3" if multiline else "1.35"
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@800;900&display=swap');

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  background: linear-gradient(135deg, #F1F5F9 0%, #CBD5E1 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', sans-serif;
  -webkit-font-smoothing: antialiased;
}}

.container {{
  width: 100%;
  max-width: 1040px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}

.illustration-area {{
  width: 100%;
  height: 240px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 38px;
}}

.title {{
  font-size: {font_size};
  font-weight: 800;
  line-height: {line_height};
  text-align: center;
  letter-spacing: -0.01em;
  background: linear-gradient(90deg, #0EA5E9 0%, #10B981 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  padding: 0 40px;
  white-space: {'normal' if multiline else 'nowrap'};
}}
</style>
</head>
<body>
  <div class="container">
    <div class="illustration-area">
      {case["svg_content"]}
    </div>
    <h1 class="title">{title_html}</h1>
  </div>
</body>
</html>
"""
    return html

def main():
    print(f"Generating all {len(CASES_DATA)} case banners...")
    
    for idx, case in enumerate(CASES_DATA, start=1):
        filename = case["filename"]
        print(f"[{idx}/{len(CASES_DATA)}] Processing {filename}...")
        
        html_content = generate_banner_html(case)
        base_name = os.path.splitext(filename)[0]
        html_file = os.path.join(TEMP_DIR, f"{base_name}.html")
        png_file = os.path.join(TEMP_DIR, f"{base_name}.png")
        final_webp_file = os.path.join(OUTPUT_DIR, filename)

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Run headless chrome to take screenshot
        cmd = [
            CHROME_PATH,
            "--headless",
            "--disable-gpu",
            "--window-size=1200,675",
            f"--screenshot={png_file}",
            html_file
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error capturing {filename}: {res.stderr}")
            continue

        # Convert to WebP using Pillow
        im = Image.open(png_file)
        im.save(final_webp_file, "WEBP", quality=95)
        print(f"  ✓ Saved {final_webp_file} ({im.size[0]}x{im.size[1]})")

    print("\nAll 18 banners generated successfully!")

if __name__ == "__main__":
    main()
