#!/usr/bin/env python3
"""Generate multipage EN/ZH academic homepage."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CSS = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+3:wght@400;600;700&display=swap"

RESEARCH_EN = """
      <h2 id="research" class="section-title">🔬 Research Interests</h2>
      <p class="section-note">
        I study how multimodal foundation models can perceive, reason about, and act upon complex visual worlds—across general, medical, industrial, and sports settings.
      </p>
      <div class="research">
        <article class="research-theme">
          <h3 class="research-theme__title">1. Multimodal Large Language Models: Design and Applications</h3>
          <p class="research-theme__lead">
            Designing multimodal LLMs that ground language in visual and temporal signals, and transferring these models to high-stakes application domains with reliable understanding and localization.
          </p>
          <h4 class="research-subhead">General vision–language understanding</h4>
          <ul class="plain-list">
            <li>Video understanding and temporal reasoning</li>
            <li>Video question answering</li>
            <li>Visual grounding and temporal localization</li>
          </ul>
          <h4 class="research-subhead">Medical imaging and surgical intelligence</h4>
          <ul class="plain-list">
            <li>Whole-slide image (WSI) analysis</li>
            <li>CT analysis and medical image segmentation</li>
            <li>Surgical video understanding and skill assessment</li>
          </ul>
          <h4 class="research-subhead">Industrial perception</h4>
          <ul class="plain-list">
            <li>Intelligent visual inspection</li>
            <li>Anomalous event monitoring</li>
          </ul>
          <h4 class="research-subhead">Sports analytics</h4>
          <ul class="plain-list">
            <li>Athlete action quality assessment</li>
          </ul>
        </article>
        <article class="research-theme">
          <h3 class="research-theme__title">2. World Models</h3>
          <p class="research-theme__lead">
            Learning predictive models of environmental dynamics to support temporal foresight, planning, and decision-making in multimodal settings.
          </p>
        </article>
        <article class="research-theme">
          <h3 class="research-theme__title">3. Multi-Agent Systems</h3>
          <p class="research-theme__lead">
            Coordinating multiple agents for collaborative perception, reasoning, and task execution in complex environments.
          </p>
        </article>
      </div>
""".strip()

RESEARCH_ZH = """
      <h2 id="research" class="section-title">🔬 研究方向</h2>
      <p class="section-note">
        关注多模态基础模型如何感知、理解并作用于复杂视觉世界，覆盖通用、医学、工业与体育等场景。
      </p>
      <div class="research">
        <article class="research-theme">
          <h3 class="research-theme__title">1. 多模态大语言模型：方法设计与应用</h3>
          <p class="research-theme__lead">
            研究将语言与视觉、时序信号对齐的多模态大语言模型，并面向高可靠性理解与定位需求，推进模型在关键领域的迁移与落地。
          </p>
          <h4 class="research-subhead">通用视觉—语言理解</h4>
          <ul class="plain-list">
            <li>视频理解与时序推理</li>
            <li>视频问答（Video QA）</li>
            <li>视觉定位与时序定位（grounding / localization）</li>
          </ul>
          <h4 class="research-subhead">医学影像与手术智能</h4>
          <ul class="plain-list">
            <li>全切片病理图像（WSI）分析</li>
            <li>CT 分析与医学图像分割</li>
            <li>手术视频理解与技能评估</li>
          </ul>
          <h4 class="research-subhead">工业视觉感知</h4>
          <ul class="plain-list">
            <li>智能视觉检测</li>
            <li>异常事件监测</li>
          </ul>
          <h4 class="research-subhead">体育分析</h4>
          <ul class="plain-list">
            <li>运动员动作质量评估</li>
          </ul>
        </article>
        <article class="research-theme">
          <h3 class="research-theme__title">2. 世界模型</h3>
          <p class="research-theme__lead">
            学习环境动态的预测模型，以支撑多模态场景中的时序预见、规划与决策。
          </p>
        </article>
        <article class="research-theme">
          <h3 class="research-theme__title">3. 多智能体系统</h3>
          <p class="research-theme__lead">
            研究多智能体协同感知、推理与任务执行，提升复杂环境下的协作能力。
          </p>
        </article>
      </div>
""".strip()

NEWS_ITEMS_EN = [
    '2026/01: New Paper “Multiple myeloma cell segmentation based on position prior information guidance in medical imaging” is accepted by <strong>Pattern Recognition</strong>.',
    '2025/12: New Paper “视觉语言大模型的幻觉综述：成因、评估与治理” is accepted by <strong>计算机研究与发展</strong>.',
    '2025/11: New Paper “Instruction-guided fusion of multi-layer visual features in Large Vision-Language Models” is accepted by <strong>Pattern Recognition</strong>.',
    '2025/08: New Paper “Adapting Multimodal Large Language Models for Video Question Answering by Capturing Question-Critical and Coherent Moments” is accepted by <strong><em>IEEE</em> Transactions on Multimedia</strong>.',
    '2025/08: New Paper “Cross-Modal Complementary Learning and Template-Based Reasoning Chains for Future Event Prediction in Videos” is accepted by <strong><em>IEEE</em> Transactions on Multimedia</strong>.',
    '2025/05: New Paper “VFE: A large-scale video future event description dataset for evaluating video temporal prediction” is accepted by <strong>Applied Intelligence</strong>.',
    '2025/02: New Paper “MKER: Multi-Modal Knowledge Extraction and Reasoning for Future Event Prediction” is accepted by <strong>Complex &amp; Intelligent Systems</strong>.',
    '2024/08: New Paper “Object-Centric Cross-Modal Knowledge Reasoning for Future Event Prediction in Videos” is accepted by <strong><em>IEEE</em> TCSVT</strong>.',
]

NEWS_ITEMS_ZH = [
    '2026/01：论文“Multiple myeloma cell segmentation based on position prior information guidance in medical imaging”被 <strong>Pattern Recognition</strong> 接收。',
    '2025/12：论文“视觉语言大模型的幻觉综述：成因、评估与治理”被 <strong>计算机研究与发展</strong> 接收。',
    '2025/11：论文“Instruction-guided fusion of multi-layer visual features in Large Vision-Language Models”被 <strong>Pattern Recognition</strong> 接收。',
    '2025/08：论文“Adapting Multimodal Large Language Models for Video Question Answering by Capturing Question-Critical and Coherent Moments”被 <strong><em>IEEE</em> Transactions on Multimedia</strong> 接收。',
    '2025/08：论文“Cross-Modal Complementary Learning and Template-Based Reasoning Chains for Future Event Prediction in Videos”被 <strong><em>IEEE</em> Transactions on Multimedia</strong> 接收。',
    '2025/05：论文“VFE: A large-scale video future event description dataset for evaluating video temporal prediction”被 <strong>Applied Intelligence</strong> 接收。',
    '2025/02：论文“MKER: Multi-Modal Knowledge Extraction and Reasoning for Future Event Prediction”被 <strong>Complex &amp; Intelligent Systems</strong> 接收。',
    '2024/08：论文“Object-Centric Cross-Modal Knowledge Reasoning for Future Event Prediction in Videos”被 <strong><em>IEEE</em> TCSVT</strong> 接收。',
]

PUBS = [
    {
        "title": "Instruction-guided fusion of multi-layer visual features in Large Vision-Language Models",
        "authors": "X Li, Y Zheng, H Chen, X Chen, Y Liang, <strong>C Lai</strong>, B Li, X Xue",
        "venue": "Pattern Recognition, Vol. 170, Article 111932, 2026",
    },
    {
        "title": "Multiple myeloma cell segmentation based on position prior information guidance in medical imaging",
        "authors": "D Li, J Zhang, Y Li, Q Wang, H Shen, <strong>C Lai</strong>, Y Tan, F Zhou",
        "venue": "Pattern Recognition, Vol. 179, Article 113744, 2026",
    },
    {
        "title": "Adapting Multimodal Large Language Models for Video Question Answering by Capturing Question-Critical and Coherent Moments",
        "authors": "H Wang, <strong>C Lai</strong>, W Ge",
        "venue": "IEEE Transactions on Multimedia, Vol. 27, pp. 8737-8747, 2025",
    },
    {
        "title": "Cross-Modal Complementary Learning and Template-Based Reasoning Chains for Future Event Prediction in Videos",
        "authors": "<strong>C Lai</strong>, W Ge, X Xue",
        "venue": "IEEE Transactions on Multimedia, Vol. 27, pp. 7497-7509, 2025",
    },
    {
        "title": "VFE: A large-scale video future event description dataset for evaluating video temporal prediction",
        "authors": "<strong>C Lai</strong>, H Wang",
        "venue": "Applied Intelligence, Vol. 55, Article 713, 2025",
    },
    {
        "title": "MKER: Multi-Modal Knowledge Extraction and Reasoning for Future Event Prediction",
        "authors": "<strong>C Lai</strong>, S Qiu",
        "venue": "Complex &amp; Intelligent Systems, Vol. 11(2), 2025",
    },
    {
        "title": "视觉语言大模型的幻觉综述：成因、评估与治理",
        "authors": "李煦, 朱睿, 陈小磊, 伍瑾轩, 郑毅, <strong>赖承杭</strong>, 梁宇轩, 李斌, 薛向阳",
        "venue": "计算机研究与发展, 2025年第12期",
    },
    {
        "title": "Object-Centric Cross-Modal Knowledge Reasoning for Future Event Prediction in Videos",
        "authors": "<strong>C Lai</strong>, H Wang, W Ge, X Xue",
        "venue": "IEEE Transactions on Circuits and Systems for Video Technology, Vol. 34, Issue 12, 2024",
    },
    {
        "title": "Weakly Supervised Gaussian Contrastive Grounding with Large Multimodal Models for Video Question Answering",
        "authors": "H Wang, <strong>C Lai</strong>, Y Sun, W Ge",
        "venue": "ACMMM, 2024",
    },
    {
        "title": "Leveraging Smooth Deformation Augmentation for LiDAR Point Cloud Semantic Segmentation",
        "authors": "S Qiu, J Chen, <strong>C Lai</strong>, H Lu, X Xue, J Pu",
        "venue": "IEEE Transactions on Intelligent Vehicles, Vol. 9(2), pp. 3316-3329, 2024",
    },
    {
        "title": "DADL: Double Asymmetric Distribution Learning for head pose estimation in wisdom museum",
        "authors": "W Zhao, S Wang, X Wang, D Li, J Wang, <strong>C Lai</strong>, X Li",
        "venue": "Journal of King Saud University-Computer and Information Sciences, Vol. 36(1), Article 101869, 2024",
    },
    {
        "title": "Weakly Supervised Learning of Semantic Correspondence through Cascaded Online Correspondence Refinement",
        "authors": "Y Huang, Y Sun, <strong>C Lai</strong>, Q Xu, X Wang, X Shen, W Ge",
        "venue": "Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023",
    },
    {
        "title": "GCANet: Geometry cues-aware facial expression recognition based on graph convolutional networks",
        "authors": "S Wang, A Zhao, <strong>C Lai</strong>, Q Zhang, D Li, Y Gao, L Dong, X Wang",
        "venue": "Journal of King Saud University-Computer and Information Sciences, Vol. 35(7), Article 101605, 2023",
    },
    {
        "title": "Infrared facial expression recognition via Gaussian-based label distribution learning in the dark illumination environment for human emotion detection",
        "authors": "Z Zhang, <strong>C Lai</strong>, H Liu, YF Li",
        "venue": "Neurocomputing, Vol. 409, pp. 341-350, 2020",
    },
]


def pubs_html() -> str:
    blocks = []
    for i, p in enumerate(PUBS, start=1):
        blocks.append(
            "        <li>\n"
            f'          <div class="pub-head"><span class="pub-num">[{i}]</span> <span class="title">{p["title"]}</span></div>\n'
            f'          <div class="meta"><span class="authors">{p["authors"]}</span><span class="venue-sep">. </span><span class="venue">{p["venue"]}</span></div>\n'
            "        </li>"
        )
    return "\n".join(blocks)

NAV_EN = [
    ("", "Home"),
    ("publications/", "Publications"),
    ("teaching/", "Teaching"),
    ("students/", "Students"),
]
NAV_ZH = [
    ("", "首页"),
    ("publications/", "论文"),
    ("teaching/", "教学"),
    ("students/", "学生"),
]


def rel_prefix(depth: int) -> str:
    return "" if depth == 0 else "../" * depth


def page(
    *,
    lang: str,
    depth: int,
    slug: str,
    title: str,
    description: str,
    active: str,
    main_html: str,
    show_sidebar: bool = True,
) -> str:
    prefix = rel_prefix(depth)
    home_href = f"{prefix}" if prefix else "./"
    is_zh = lang == "zh"
    # For ZH pages, site assets sit above /zh/
    asset_prefix = prefix if not is_zh else rel_prefix(depth + 1)
    # Language alternate
    if is_zh:
        # current under /zh/... ; EN counterpart is up out of zh then into slug
        en_href = f"{rel_prefix(depth + 1)}{slug}" if slug else rel_prefix(depth + 1) or "../"
        lang_switch = f'<a class="lang-switch" href="{en_href}" hreflang="en" lang="en">English</a>'
        brand = "赖承杭 / 个人主页"
        brand_href = home_href
        home_url = "https://chlai1111.github.io/zh/" + slug
        en_url = "https://chlai1111.github.io/" + slug
        zh_url = home_url
        html_lang = "zh-Hans"
        footer = '© <span id="y"></span> 赖承杭. 托管于 GitHub Pages · <a href="https://github.com/chlai1111/chlai1111.github.io">源代码</a>'
        nav = NAV_ZH
        author_name = "赖承杭（Chenghang Lai）"
        author_bio = "温州大学"
        author_lab = "灵境智能研究组负责人"
        meta_loc = "中国 · 温州"
        label_email = "邮箱"
        aria_nav = "主导航"
        avatar_alt = "赖承杭照片"
    else:
        zh_href = f"{prefix}zh/{slug}"
        lang_switch = f'<a class="lang-switch" href="{zh_href}" hreflang="zh-Hans" lang="zh-Hans">中文</a>'
        brand = "Chenghang Lai / Personal Homepage"
        brand_href = home_href
        home_url = "https://chlai1111.github.io/" + slug
        en_url = home_url
        zh_url = "https://chlai1111.github.io/zh/" + slug
        html_lang = "en"
        footer = '© <span id="y"></span> Chenghang Lai. Hosted on GitHub Pages · <a href="https://github.com/chlai1111/chlai1111.github.io">Source</a>'
        nav = NAV_EN
        author_name = "Chenghang Lai (赖承杭)"
        author_bio = "Wenzhou University"
        author_lab = "Director, LingVision Lab"
        meta_loc = "Wenzhou, China"
        label_email = "Email"
        aria_nav = "Primary"
        avatar_alt = "Portrait of Chenghang Lai"
        asset_prefix = prefix

    active_key = active.rstrip("/")
    nav_html = []
    for href, label in nav:
        href_key = href.rstrip("/")
        cls = ' class="is-active"' if href_key == active_key else ""
        link = home_href if href == "" else f"{prefix}{href}"
        nav_html.append(f'<a href="{link}"{cls}>{label}</a>')

    sidebar = ""
    if show_sidebar:
        sidebar = f"""
    <aside class="sidebar">
      <img class="avatar" src="{asset_prefix}images/profile.jpg?v=3" alt="{avatar_alt}">
      <h1 class="author-name">{author_name}</h1>
      <p class="author-bio">{author_bio}</p>
      <p class="author-lab">{author_lab}</p>
      <ul class="author-meta">
        <li><span class="label">📍</span> {meta_loc}</li>
        <li><span class="label">{label_email}</span> <a href="mailto:chlai21@m.fudan.edu.cn">chlai21@m.fudan.edu.cn</a></li>
        <li><span class="label">Scholar</span> <a href="https://scholar.google.com.hk/citations?hl=zh-CN&amp;user=WxUuGCAAAAAJ">Google Scholar</a></li>
        <li><span class="label">GitHub</span> <a href="https://github.com/chlai1111">chlai1111</a></li>
      </ul>
    </aside>"""

    layout_class = "layout" if show_sidebar else "layout layout--wide"

    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{home_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="zh-Hans" href="{zh_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url if not is_zh else 'https://chlai1111.github.io/'}">
  <link rel="icon" href="{asset_prefix}images/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{CSS}" rel="stylesheet">
  <link rel="stylesheet" href="{asset_prefix}assets/css/main.css">
</head>
<body>
  <header class="masthead">
    <div class="masthead__inner">
      <a class="site-title" href="{brand_href}">{brand}</a>
      <div class="masthead__right">
        <nav class="nav" aria-label="{aria_nav}">
          {''.join(nav_html)}
        </nav>
        {lang_switch}
      </div>
    </div>
  </header>

  <div class="{layout_class}">
{sidebar}

    <main class="main">
{main_html}
    </main>
  </div>

  <footer class="footer">
    {footer}
  </footer>
  <script>document.getElementById('y').textContent = new Date().getFullYear();</script>
</body>
</html>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def news_list(items):
    return "<ul class=\"news\">\n" + "\n".join(f"        <li>{x}</li>" for x in items) + "\n      </ul>"


def main():
    # EN home
    en_home = f"""
      <h1 id="biography" class="page-title">Biography</h1>
      <div class="bio">
        <p>
          I am a <strong>lecturer at <a href="https://www.wzu.edu.cn/">Wenzhou University (温州大学)</a></strong>
          and the <strong>director of LingVision Lab (灵境智能研究组)</strong>.
          I received my Ph.D. from the <a href="https://cs.fudan.edu.cn/">School of Computer Science</a>,
          <a href="https://fudan.edu.cn/">Fudan University</a> (2021.9–2025.6).
          <strong>My research focuses on multimodal large language models, world models, and multi-agent systems, with applications in general video understanding, medical imaging, industrial inspection, and sports analytics.</strong>
          During my doctoral studies, I was guided by Academician
          <a href="https://ysg.ckcest.cn/html/details/8058/index.html">Qionghai Dai</a> from Tsinghua University
          and Professor <a href="https://cs.fudan.edu.cn/3f/8a/c25907a278410/page.htm">Xiangyang Xue</a> from Fudan University.
        </p>
        <p>
          <a href="mailto:chlai21@m.fudan.edu.cn">Email</a> /
          <a href="https://github.com/chlai1111">GitHub</a>
        </p>
        <p class="recruit-note">
          LingVision Lab admits a limited number of students each year. Outstanding master’s and undergraduate students who are interested in our research are welcome to apply to join the lab.
        </p>
      </div>

{RESEARCH_EN}
""".strip()
    write(ROOT / "index.html", page(
        lang="en", depth=0, slug="", title="Chenghang Lai (赖承杭) — Personal Homepage",
        description="Academic homepage of Chenghang Lai, lecturer at Wenzhou University and director of LingVision Lab. Research interests: multimodal large language models, world models, and multi-agent systems.",
        active="", main_html=en_home, show_sidebar=True,
    ))

    pubs_en = f"""
      <h1 class="page-title">📎 Publications</h1>
      <h2 id="news" class="section-title">🔥 Recent Acceptances</h2>
      {news_list(NEWS_ITEMS_EN)}
      <h2 id="papers" class="section-title">Selected Papers</h2>
      <ul class="pubs">
{pubs_html()}
      </ul>
""".strip()
    write(ROOT / "publications" / "index.html", page(
        lang="en", depth=1, slug="publications/", title="Publications — Chenghang Lai",
        description="Selected publications and recent acceptances of Chenghang Lai.",
        active="publications",
        main_html=pubs_en,
        show_sidebar=False,
    ))

    teaching_en = """
      <h1 class="page-title">📚 Teaching</h1>
      <p class="section-note">Academic year 2026–2027</p>
      <h3 class="subhead">Undergraduate</h3>
      <ul class="plain-list">
        <li>Design and Analysis of Computer Algorithms — 2026–2027 Fall</li>
        <li>Applications of Computer Vision — 2026–2027 Spring</li>
      </ul>
      <h3 class="subhead">Graduate</h3>
      <ul class="plain-list">
        <li>Computer System Architecture — 2026–2027 Fall</li>
      </ul>
""".strip()
    write(ROOT / "teaching" / "index.html", page(
        lang="en", depth=1, slug="teaching/", title="Teaching — Chenghang Lai",
        description="Teaching courses by Chenghang Lai.",
        active="teaching", main_html=teaching_en, show_sidebar=False,
    ))

    students_en = """
      <h1 class="page-title">👥 Students</h1>
      <h3 class="subhead">Master’s Students · Class of 2025</h3>
      <ul class="plain-list">
        <li>Xue Zekun (薛泽坤) · Wenzhou University</li>
        <li>Chen Jiong (陈炅) · Wenzhou University</li>
        <li>Wu Boxuan (吴波炫) · Wenzhou University</li>
      </ul>
      <h3 class="subhead">Master’s Students · Class of 2026</h3>
      <ul class="plain-list">
        <li>Xie Yi (谢益) · Wenzhou University</li>
        <li>Lu Jiaming (陆佳明) · Wenzhou University</li>
        <li>Chen Yuxuan (陈雨轩) · Wenzhou University</li>
        <li>Zhang Yangliu (张杨柳) · Wenzhou University</li>
        <li>Xu Junchang (许俊昌) · Wenzhou University</li>
      </ul>
      <h3 class="subhead">Undergraduate Students · Class of 2025</h3>
      <ul class="plain-list">
        <li>Huang Xiaorui (黄小芮) · Wenzhou University</li>
        <li>Ye Mengya (叶梦雅) · Wenzhou University</li>
        <li>Lü Dingtian (吕鼎天) · Wenzhou University</li>
      </ul>
      <h3 class="subhead">Undergraduate Students · Class of 2026</h3>
      <ul class="plain-list">
        <li>Guo Qiming (郭骐铭) · Wenzhou University</li>
      </ul>
""".strip()
    write(ROOT / "students" / "index.html", page(
        lang="en", depth=1, slug="students/", title="Students — Chenghang Lai",
        description="Students advised by Chenghang Lai.",
        active="students", main_html=students_en, show_sidebar=False,
    ))

    # ZH home
    zh_home = f"""
      <h1 id="biography" class="page-title">个人简介</h1>
      <div class="bio">
        <p>
          我是<strong><a href="https://www.wzu.edu.cn/">温州大学</a>讲师</strong>，
          <strong>灵境智能研究组（LingVision Lab）负责人</strong>。
          博士毕业于<a href="https://fudan.edu.cn/">复旦大学</a>
          <a href="https://cs.fudan.edu.cn/">计算机科学技术学院</a>（2021.9–2025.6）。
          <strong>主要研究多模态大语言模型、世界模型与多智能体系统，并面向通用视频理解、医学影像、工业检测与体育分析等场景开展应用研究。</strong>
          博士期间得到清华大学戴琼海院士与复旦大学薛向阳教授指导。
        </p>
        <p>
          <a href="mailto:chlai21@m.fudan.edu.cn">邮箱</a> /
          <a href="https://github.com/chlai1111">GitHub</a>
        </p>
        <p class="recruit-note">
          灵境智能研究组每年招生名额有限，欢迎对相关研究方向感兴趣、基础扎实的优秀硕士生与本科生联系加入。
        </p>
      </div>

{RESEARCH_ZH}
""".strip()
    write(ROOT / "zh" / "index.html", page(
        lang="zh", depth=0, slug="", title="赖承杭（Chenghang Lai）— 个人主页",
        description="温州大学讲师、灵境智能研究组（LingVision Lab）负责人赖承杭的学术主页。研究方向：多模态大语言模型、世界模型与多智能体系统。",
        active="", main_html=zh_home, show_sidebar=True,
    ))

    pubs_zh = f"""
      <h1 class="page-title">📎 论文</h1>
      <h2 id="news" class="section-title">🔥 近期录用</h2>
      {news_list(NEWS_ITEMS_ZH)}
      <h2 id="papers" class="section-title">代表性论文</h2>
      <ul class="pubs">
{pubs_html()}
      </ul>
""".strip()
    write(ROOT / "zh" / "publications" / "index.html", page(
        lang="zh", depth=1, slug="publications/", title="论文 — 赖承杭",
        description="赖承杭的论文列表与近期录用动态。",
        active="publications",
        main_html=pubs_zh,
        show_sidebar=False,
    ))

    teaching_zh = """
      <h1 class="page-title">📚 教学</h1>
      <p class="section-note">2026–2027 学年</p>
      <h3 class="subhead">本科</h3>
      <ul class="plain-list">
        <li>计算机算法设计与分析 — 2026–2027 第一学期</li>
        <li>计算机视觉应用 — 2026–2027 第二学期</li>
      </ul>
      <h3 class="subhead">研究生</h3>
      <ul class="plain-list">
        <li>计算机系统结构教程 — 2026–2027 第一学期</li>
      </ul>
""".strip()
    write(ROOT / "zh" / "teaching" / "index.html", page(
        lang="zh", depth=1, slug="teaching/", title="教学 — 赖承杭",
        description="赖承杭的教学课程。",
        active="teaching", main_html=teaching_zh, show_sidebar=False,
    ))

    students_zh = """
      <h1 class="page-title">👥 学生</h1>
      <h3 class="subhead">硕士研究生 · 25级</h3>
      <ul class="plain-list">
        <li>薛泽坤（Xue Zekun）· 温州大学</li>
        <li>陈炅（Chen Jiong）· 温州大学</li>
        <li>吴波炫（Wu Boxuan）· 温州大学</li>
      </ul>
      <h3 class="subhead">硕士研究生 · 26级</h3>
      <ul class="plain-list">
        <li>谢益（Xie Yi）· 温州大学</li>
        <li>陆佳明（Lu Jiaming）· 温州大学</li>
        <li>陈雨轩（Chen Yuxuan）· 温州大学</li>
        <li>张杨柳（Zhang Yangliu）· 温州大学</li>
        <li>许俊昌（Xu Junchang）· 温州大学</li>
      </ul>
      <h3 class="subhead">本科生 · 25级</h3>
      <ul class="plain-list">
        <li>黄小芮（Huang Xiaorui）· 温州大学</li>
        <li>叶梦雅（Ye Mengya）· 温州大学</li>
        <li>吕鼎天（Lü Dingtian）· 温州大学</li>
      </ul>
      <h3 class="subhead">本科生 · 26级</h3>
      <ul class="plain-list">
        <li>郭骐铭（Guo Qiming）· 温州大学</li>
      </ul>
""".strip()
    write(ROOT / "zh" / "students" / "index.html", page(
        lang="zh", depth=1, slug="students/", title="学生 — 赖承杭",
        description="赖承杭指导的学生。",
        active="students", main_html=students_zh, show_sidebar=False,
    ))


if __name__ == "__main__":
    main()
