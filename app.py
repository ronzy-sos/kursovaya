from flask import Flask, render_template_string, abort

app = Flask(__name__)

MAP_ORDER = ["mirage", "dust2", "inferno"]

SITE_DATA = {
    "mirage": {
        "title": "Mirage",
        "short_text": "Mirage — одна из самых популярных карт современного Counter-Strike. Здесь особенно важны контроль мида, координация и точные тайминги раскидок.",
        "image": "/static/images/mirage.jpg",
        "in_development": False,
        "theme": {
            "accent": "#ffcc70",
            "accent_soft": "rgba(255, 204, 112, 0.10)"
        },
        "grenades": {
            "smokes": {
                "title": "Смоки",
                "icon": "☁",
                "purpose": "Смоки на Mirage особенно важны для выхода на A, контроля мида и ограничения обзора защитников.",
                "lineups": [
                    {
                        "side": "T",
                        "name": "Smoke на Start Mid",
                        "preview_image": "/static/images/mirage/smoke-start-mid-preview.png",
                        "description": "Это раскид смока на Start Mid для карты Mirage. Ниже показаны оба ракурса и пошаговое выполнение данного смока.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от T стороны",
                                "text": "Игрок с T стороны встаёт в нужную стартовую позицию на миде, наводится в правильную точку и выполняет бросок смока с ЛКМ.",
                                "file": "/static/videos/mirage/smokes/smoke-start-mid-t.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны CT",
                                "text": "На этом видео показано, как смок приземляется со стороны защиты. Такой ракурс помогает понять точность раскида и итоговую зону перекрытия обзора.",
                                "file": "/static/videos/mirage/smokes/smoke-start-mid-ct.mp4"
                            }
                        ],
                        "benefit": "Данный смок дает игрокам T стороны возможность безопасно выйти на мид."
                    },
                    {
                        "side": "T",
                        "name": "Smoke на Connector",
                        "preview_image": "/static/images/mirage/smoke-connector-preview.png",
                        "description": "Это раскид смока на Connector для карты Mirage. Ниже показаны оба ракурса и пошаговое выполнение данного смока.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от T стороны",
                                "text": "Игрок с T стороны занимает указанную позицию, наводится в нужную точку и выполняет бросок смока на Connector с прыжком и ЛКМ.",
                                "file": "/static/videos/mirage/smokes/smoke-connector-t.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны CT",
                                "text": "На этом видео показано, как смок ложится со стороны защиты. Такой ракурс помогает понять точность раскида и то, как именно перекрывается Connector.",
                                "file": "/static/videos/mirage/smokes/smoke-connector-ct.mp4"
                            }
                        ],
                        "benefit": "Данный смок позволяет игрокам T стороны безопаснее выходить в зону мида и ограничивать обзор защитников с Connector`a."
                    }
                ]
            },
            "flashes": {
                "title": "Флешки",
                "icon": "✦",
                "purpose": "Флешки помогают ослеплять защитников перед выходом и создавать удобный момент для врыва в определенную позицию.",
                "lineups": [
                    {
                        "side": "CT",
                        "name": "Flash за CT против push`a с ямы",
                        "preview_image": "/static/images/mirage/flash-ct-anti-push-pit-preview.png",
                        "description": "Это флешка за CT сторону на карте Mirage против агрессивного push`a со стороны T с ямы. Ниже показаны оба ракурса и пошаговое выполнение данного раскида.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от CT стороны",
                                "text": "Игрок со стороны защиты упиратеся в угол под паласами, наводит прицел как показно на видео, после чего кидает флешку с прыжком и ЛКМ, чтобы остановить или замедлить агрессивный выход соперников с ямы.",
                                "file": "/static/videos/mirage/flashes/flash-ct-anti-push-pit-ct.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны T",
                                "text": "На этом видео показано, как флешка срабатывает со стороны атаки. Такой ракурс помогает понять, насколько эффективно она останавливает push с ямы.",
                                "file": "/static/videos/mirage/flashes/flash-ct-anti-push-pit-t.mp4"
                            }
                        ],
                        "benefit": "Флеш помогает игрокам CT стороны сдержать агрессивный push соперников с ямы и выиграть время для защиты позиции."
                    },
                    {
                        "side": "T",
                        "name": "Flash для выхода с ямы",
                        "preview_image": "/static/images/mirage/flash-pit-exit-preview.png",
                        "description": "Это флешка для выхода с ямы на карте Mirage за T сторону. Ниже показаны оба ракурса и пошаговое выполнение данного раскида.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от T стороны",
                                "text": "Игрок со стороны атаки встает как показано на видео, после чего целиться и кидает флешку ЛКМ, чтобы безопаснее выйти на A site и ослепить игроков защиты на ближайших позициях.",
                                "file": "/static/videos/mirage/flashes/flash-pit-exit-t.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны CT",
                                "text": "На этом видео показано, как флешка выглядит со стороны защиты. Такой ракурс помогает понять, какие позиции на A site она перекрывает и насколько удобен выход после неё.",
                                "file": "/static/videos/mirage/flashes/flash-pit-exit-ct.mp4"
                            }
                        ],
                        "benefit": "Флеш помогает игрокам T стороны безопаснее выйти с ямы на A site, ослепить защитников и создать удобный момент для врыва."
                    }
                ]
            },
            "molotovs": {
                "title": "Молотовы",
                "icon": "🔥",
                "purpose": "Молотовы нужны для выжигания сильных позиций и замедления соперника при выходе на плент.",
                "lineups": [
                    {
                        "side": "T",
                        "name": "Molotov под Palace",
                        "preview_image": "/static/images/mirage/molotov-palace-preview.png",
                        "description": "Это раскид молотова под Palace на карте Mirage за T сторону. Ниже показаны оба ракурса и пошаговое выполнение данного раскида.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от T стороны",
                                "text": "Игрок со стороны атаки занимает указанную позицию, наводится в правильную точку, набирает немного скорость и выполняет бросок молотова под Palace с ЛКМ.",
                                "file": "/static/videos/mirage/molotovs/molotov-palace-t.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны CT",
                                "text": "На этом видео показано, как молотов ложится со стороны защиты. Такой ракурс помогает понять точность раскида и площадь выжигания позиции под Palace.",
                                "file": "/static/videos/mirage/molotovs/molotov-palace-ct.mp4"
                            }
                        ],
                        "benefit": "Молотов помогает игрокам T стороны выбить соперника из позиции под Palace и безопаснее развивать выход на A."
                    },
                    {
                        "side": "CT",
                        "name": "Molotov на A site",
                        "preview_image": "/static/images/mirage/molotov-a-site-preview.png",
                        "description": "Это раскид молотова на A site на карте Mirage за CT сторону. Ниже показаны оба ракурса и пошаговое выполнение данного раскида.",
                        "videos": [
                            {
                                "step": "Шаг 1",
                                "title": "Вид от CT стороны",
                                "text": "Игрок со стороны защиты занимает позицию на A site, наводится в нужную точку и выполняет бросок молотова с ЛКМ для контроля выхода соперников.",
                                "file": "/static/videos/mirage/molotovs/molotov-a-site-ct.mp4"
                            },
                            {
                                "step": "Шаг 2",
                                "title": "Вид со стороны T",
                                "text": "На этом видео показано, как молотов выглядит со стороны атаки. Такой ракурс помогает понять, какую часть A site и ближайших подходов перекрывает огонь.",
                                "file": "/static/videos/mirage/molotovs/molotov-a-site-t.mp4"
                            }
                        ],
                        "benefit": "Молотов помогает игрокам CT стороны замедлить выход соперников на A site, выиграть время и осложнить занятие плента."
                    }
                ]
            }
        }
    },
    "dust2": {
        "title": "Dust 2",
        "short_text": "Dust 2 — одна из самых известных карт в Counter-Strike. Раздел по этой карте сейчас находится в разработке.",
        "image": "/static/images/dust2.jpg",
        "in_development": True,
        "theme": {
            "accent": "#58e6ff",
            "accent_soft": "rgba(88, 230, 255, 0.10)"
        },
        "grenades": {}
    },
    "inferno": {
        "title": "Inferno",
        "short_text": "Inferno — классическая тактическая карта серии Counter-Strike. Раздел по этой карте сейчас находится в разработке.",
        "image": "/static/images/inferno.jpg",
        "in_development": True,
        "theme": {
            "accent": "#ff7a59",
            "accent_soft": "rgba(255, 122, 89, 0.10)"
        },
        "grenades": {}
    }
}


def slugify_name(name: str) -> str:
    return (
        name.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("→", "")
        .replace(".", "")
    )


def render_page(content, title="CS2 Tactical"):
    html = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #07111f;
            --panel: rgba(15, 26, 43, 0.74);
            --border: rgba(115, 173, 255, 0.18);
            --text: #ecf5ff;
            --muted: #9eb6d3;
            --cyan: #58e6ff;
            --cyan-soft: rgba(88, 230, 255, 0.08);
            --radius: 24px;
            --glow: 0 0 25px rgba(88, 230, 255, 0.22);
            --shadow: 0 18px 40px rgba(0, 0, 0, 0.25);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.12), transparent 28%),
                radial-gradient(circle at top right, rgba(79, 124, 255, 0.14), transparent 24%),
                linear-gradient(180deg, #060d18 0%, #091221 45%, #07111f 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 38px 38px;
            pointer-events: none;
            z-index: 0;
        }

        header {
            position: sticky;
            top: 0;
            z-index: 50;
            backdrop-filter: blur(16px);
            background: rgba(6, 13, 24, 0.62);
            border-bottom: 1px solid rgba(115, 173, 255, 0.12);
        }

        .nav {
            width: min(1180px, calc(100% - 32px));
            margin: 0 auto;
            padding: 18px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
        }

        .logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 1px;
            color: white;
            text-decoration: none;
        }

        .logo span {
            color: var(--cyan);
            text-shadow: 0 0 14px rgba(88, 230, 255, 0.35);
        }

        .nav-links {
            display: flex;
            gap: 22px;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: var(--muted);
            text-decoration: none;
            font-weight: 600;
            transition: 0.25s ease;
        }

        .nav-links a:hover {
            color: white;
            text-shadow: 0 0 10px rgba(88, 230, 255, 0.28);
        }

        .container {
            position: relative;
            z-index: 1;
            width: min(1180px, calc(100% - 32px));
            margin: 0 auto;
        }

        .hero {
            position: relative;
            min-height: calc(100vh - 78px);
            width: 100%;
            overflow: hidden;
            margin-top: 0;
            border-radius: 0;
            box-shadow: none;
            border: none;
        }

        .hero-video {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hero-overlay {
            position: absolute;
            inset: 0;
            background:
                linear-gradient(90deg, rgba(4, 10, 20, 0.90) 0%, rgba(4, 10, 20, 0.74) 38%, rgba(4, 10, 20, 0.58) 100%),
                linear-gradient(180deg, rgba(4, 10, 20, 0.35) 0%, rgba(4, 10, 20, 0.58) 100%);
            z-index: 1;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            min-height: calc(100vh - 78px);
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 28px;
            align-items: center;
            width: min(1180px, calc(100% - 32px));
            margin: 0 auto;
            padding: 50px 0;
        }

        .eyebrow {
            display: inline-block;
            margin-bottom: 18px;
            padding: 8px 14px;
            border: 1px solid var(--accent, rgba(88, 230, 255, 0.22));
            border-radius: 999px;
            background: var(--accent_soft, rgba(88, 230, 255, 0.08));
            color: var(--accent, #58e6ff);
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            box-shadow: 0 0 24px var(--accent_soft, rgba(88, 230, 255, 0.10));
        }

        .hero h1, .page-title {
            font-family: 'Orbitron', sans-serif;
            line-height: 1.04;
            letter-spacing: 0.5px;
        }

        .hero h1 {
            font-size: clamp(38px, 6vw, 72px);
            margin-bottom: 18px;
        }

        .hero h1 span {
            color: var(--cyan);
            text-shadow: 0 0 18px rgba(88, 230, 255, 0.35);
        }

        .hero p, .page-subtitle {
            color: var(--muted);
            line-height: 1.8;
            font-size: 18px;
        }

        .hero p {
            max-width: 720px;
            margin-bottom: 28px;
        }

        .hero-actions {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 180px;
            padding: 15px 24px;
            border-radius: 14px;
            text-decoration: none;
            font-weight: 700;
            transition: 0.25s ease;
        }

        .btn-primary {
            color: #04101b;
            background: linear-gradient(135deg, var(--cyan), #8ff3ff);
            box-shadow: 0 12px 30px rgba(34, 211, 238, 0.22);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 18px 34px rgba(34, 211, 238, 0.3);
        }

        .btn-secondary {
            color: white;
            border: 1px solid rgba(115, 173, 255, 0.2);
            background: rgba(255,255,255,0.03);
        }

        .btn-secondary:hover {
            transform: translateY(-3px);
            border-color: rgba(88, 230, 255, 0.4);
            box-shadow: var(--glow);
        }

        .glass-card {
            position: relative;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 26px;
            padding: 24px;
            backdrop-filter: blur(14px);
            box-shadow: var(--shadow);
            overflow: hidden;
        }

        .glass-card::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, var(--accent_soft, rgba(88,230,255,0.08)), transparent 40%, rgba(79,124,255,0.08));
            pointer-events: none;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
        }

        .stat-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(115, 173, 255, 0.12);
            border-radius: 18px;
            padding: 18px;
        }

        .stat-number {
            font-family: 'Orbitron', sans-serif;
            color: var(--cyan);
            font-size: 28px;
            margin-bottom: 8px;
        }

        .stat-label {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.5;
        }

        .section {
            padding: 70px 0;
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: end;
            gap: 20px;
            margin-bottom: 28px;
            flex-wrap: wrap;
        }

        .section-head h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(28px, 4vw, 42px);
        }

        .section-head p {
            max-width: 620px;
            color: var(--muted);
            line-height: 1.7;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 22px;
        }

        .card {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
            backdrop-filter: blur(14px);
            transition: 0.28s ease;
            box-shadow: 0 12px 32px rgba(0,0,0,0.18);
        }

        .card:hover {
            transform: translateY(-7px);
            border-color: var(--accent, rgba(88, 230, 255, 0.35));
            box-shadow: 0 16px 36px rgba(8, 21, 37, 0.45), 0 0 24px var(--accent_soft, rgba(88, 230, 255, 0.10));
        }

        .card.dev-card {
            opacity: 0.92;
            cursor: default;
        }

        .map-link, .grenade-link, .lineup-link {
            text-decoration: none;
            color: inherit;
        }

        .map-image {
            height: 220px;
            background-size: cover;
            background-position: center;
            position: relative;
        }

        .map-image::after {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(5,12,22,0.95), rgba(5,12,22,0.2));
        }

        .dev-badge {
            position: absolute;
            top: 14px;
            right: 14px;
            z-index: 3;
            padding: 8px 12px;
            border-radius: 999px;
            background: rgba(255, 122, 89, 0.92);
            color: white;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            box-shadow: 0 10px 24px rgba(255, 122, 89, 0.25);
        }

        .card-content {
            padding: 22px;
        }

        .card h3 {
            font-size: 22px;
            margin-bottom: 10px;
        }

        .map-title, .grenade-title, .lineup-title {
            font-family: 'Orbitron', sans-serif;
        }

        .card p {
            color: var(--muted);
            line-height: 1.7;
            font-size: 15px;
        }

        .map-tag, .grenade-tag, .lineup-tag {
            display: inline-block;
            margin-top: 14px;
            color: var(--accent, var(--cyan));
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .page-wrap {
            padding: 56px 0 46px;
        }

        .page-top {
            margin-bottom: 28px;
        }

        .page-top-card {
            display: grid;
            grid-template-columns: 1fr;
            gap: 18px;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 34px;
            backdrop-filter: blur(14px);
            box-shadow: var(--shadow);
        }

        .page-title {
            font-size: clamp(34px, 6vw, 60px);
        }

        .grenade-card {
            padding: 26px;
            min-height: 250px;
        }

        .grenade-icon {
            width: 58px;
            height: 58px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            background: var(--accent_soft, rgba(88, 230, 255, 0.10));
            color: var(--accent, var(--cyan));
            border: 1px solid var(--accent_soft, rgba(88, 230, 255, 0.10));
            margin-bottom: 16px;
        }

        .purpose-box, .media-box, .lineups-box, .benefit-box, .dev-box {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 28px;
            backdrop-filter: blur(14px);
            box-shadow: var(--shadow);
            margin-bottom: 22px;
        }

        .box-title {
            font-family: 'Orbitron', sans-serif;
            color: var(--accent, var(--cyan));
            font-size: 24px;
            margin-bottom: 12px;
        }

        .purpose-box p,
        .media-box p,
        .lineups-box p,
        .benefit-box p,
        .dev-box p {
            color: var(--muted);
            line-height: 1.8;
            font-size: 17px;
        }

        .lineup-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 18px;
            margin-top: 16px;
        }

        .lineup-card {
            padding: 22px;
            border-radius: 20px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(115, 173, 255, 0.14);
            transition: 0.25s ease;
        }

        .lineup-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent, rgba(88, 230, 255, 0.30));
            box-shadow: 0 0 20px var(--accent_soft, rgba(88, 230, 255, 0.10));
        }

        .side-badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            background: var(--accent_soft, rgba(88, 230, 255, 0.10));
            color: var(--accent, var(--cyan));
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .lineup-preview {
            width: 100%;
            height: 170px;
            object-fit: cover;
            border-radius: 14px;
            display: block;
            margin: 12px 0 6px;
            border: 1px solid rgba(115, 173, 255, 0.16);
        }

        .video-stack {
            display: flex;
            flex-direction: column;
            gap: 22px;
            margin-top: 16px;
        }

        .video-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(115, 173, 255, 0.14);
            border-radius: 20px;
            padding: 20px;
        }

        .step-badge {
            display: inline-block;
            padding: 8px 14px;
            margin-bottom: 14px;
            border-radius: 999px;
            background: var(--accent_soft, rgba(88, 230, 255, 0.10));
            color: var(--accent, var(--cyan));
            border: 1px solid var(--accent, var(--cyan));
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            box-shadow: 0 0 18px var(--accent_soft, rgba(88, 230, 255, 0.10));
        }

        .video-card h3 {
            font-size: 20px;
            margin-bottom: 10px;
            color: var(--accent, var(--cyan));
            font-family: 'Orbitron', sans-serif;
        }

        .video-card p {
            color: var(--muted);
            line-height: 1.7;
            margin-bottom: 14px;
        }

        .lineup-video {
            width: 100%;
            border-radius: 14px;
            display: block;
            background: #000;
        }

        footer {
            width: min(1180px, calc(100% - 32px));
            margin: 20px auto 26px;
            padding: 22px 26px;
            text-align: center;
            color: var(--muted);
            border: 1px solid rgba(115, 173, 255, 0.12);
            border-radius: 18px;
            background: rgba(255,255,255,0.02);
            position: relative;
            z-index: 1;
        }

        @media (max-width: 1024px) {
            .hero-content,
            .grid-3,
            .grid-2,
            .lineup-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                min-height: auto;
            }

            .hero-content {
                min-height: auto;
                padding: 36px 0;
            }
        }

        @media (max-width: 720px) {
            .nav {
                flex-direction: column;
                gap: 14px;
            }

            .stats {
                grid-template-columns: 1fr;
            }

            .hero p,
            .page-subtitle,
            .purpose-box p,
            .media-box p,
            .lineups-box p,
            .benefit-box p,
            .dev-box p {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    __CONTENT__
</body>
</html>
"""
    html = html.replace("__TITLE__", title)
    html = html.replace("__CONTENT__", content)
    return render_template_string(html)


@app.route("/")
def home():
    content = """
    <header>
        <div class="nav">
            <a href="/" class="logo">CS2 <span>TACTICAL</span></a>
            <div class="nav-links">
                <a href="/">Главная</a>
                <a href="#about">О сайте</a>
                <a href="#maps">Карты</a>
            </div>
        </div>
    </header>

    <section class="hero">
        <video class="hero-video" autoplay muted loop playsinline>
            <source src="/static/videos/cs2-montage.mp4" type="video/mp4">
        </video>
        <div class="hero-overlay"></div>

        <div class="hero-content">
            <div>
                <div class="eyebrow">Grenade Training Platform</div>
                <h1>Изучай <span>раскидки гранат</span> в CS2 стильно и удобно</h1>
                <p>
                    Это сайт для тренировки и изучения базовых раскидов на популярных картах.
                    Сейчас основное внимание уделено Mirage, а разделы Dust 2 и Inferno находятся в разработке.
                </p>

                <div class="hero-actions">
                    <a href="#maps" class="btn btn-primary">Открыть карты</a>
                    <a href="#about" class="btn btn-secondary">Узнать о сайте</a>
                </div>
            </div>

            <div class="glass-card">
                <div class="eyebrow">О проекте</div>
                <h2 style="font-family: 'Orbitron', sans-serif; font-size: 34px; margin-bottom: 12px;">
                    Быстрый доступ к раскидам
                </h2>
                <p style="color: var(--muted); line-height: 1.8; margin-bottom: 18px;">
                    Сайт подойдёт новичкам и игрокам, которые хотят лучше понимать позиции
                    и практическое применение смоков, флешек и молотовых.
                </p>

                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">3</div>
                        <div class="stat-label">Типа гранат на основной карте</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">2</div>
                        <div class="stat-label">Раскида в каждом разделе</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">Mirage</div>
                        <div class="stat-label">Карта уже активно наполнена контентом</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">Guide</div>
                        <div class="stat-label">Удобная структура для изучения по шагам</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="container">
        <section class="section" id="about">
            <div class="section-head">
                <h2>О чём этот сайт</h2>
                <p>
                    Пользователь выбирает карту, затем тип гранаты, после чего видит нужные раскиды для выбранного раздела.
                </p>
            </div>

            <div class="grid-3">
                <div class="card">
                    <div class="card-content">
                        <h3>Просто</h3>
                        <p>На каждой странице нет лишней информации: только нужные типы гранат и только нужные раскиды.</p>
                    </div>
                </div>

                <div class="card">
                    <div class="card-content">
                        <h3>Понятно</h3>
                        <p>У раскидов есть названия, сторона, картинка позиции, описание и пошаговые видео с двух ракурсов.</p>
                    </div>
                </div>

                <div class="card">
                    <div class="card-content">
                        <h3>Удобно</h3>
                        <p>Сайт помогает быстро открыть конкретный раскид без лишних карточек и длинных списков.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section" id="maps">
            <div class="section-head">
                <h2>Карты</h2>
            </div>

            <div class="grid-3">
    """

    for map_slug in MAP_ORDER:
        map_data = SITE_DATA[map_slug]
        accent = map_data["theme"]["accent"]
        accent_soft = map_data["theme"]["accent_soft"]
        dev_badge = '<div class="dev-badge">В разработке</div>' if map_data.get("in_development") else ""
        tag_text = "Открыть карту →" if not map_data.get("in_development") else "Раздел в разработке"
        dev_class = "dev-card" if map_data.get("in_development") else ""

        card_html = f"""
            <div class="card {dev_class}" style="--accent:{accent}; --accent_soft:{accent_soft};">
                <div class="map-image" style="background-image: url('{map_data["image"]}');">
                    {dev_badge}
                </div>
                <div class="card-content">
                    <h3 class="map-title">{map_data["title"]}</h3>
                    <p>{map_data["short_text"]}</p>
                    <div class="map-tag">{tag_text}</div>
                </div>
            </div>
        """

        if map_data.get("in_development"):
            content += card_html
        else:
            content += f"""
                <a href="/map/{map_slug}" class="map-link">
                    {card_html}
                </a>
            """

    content += """
            </div>
        </section>
    </div>

    <footer>
        © 2026 CS2 Tactical
    </footer>
    """
    return render_page(content, "CS2 Tactical")


@app.route("/map/<map_slug>")
def map_detail(map_slug):
    map_data = SITE_DATA.get(map_slug)
    if not map_data or map_data.get("in_development"):
        abort(404)

    accent = map_data["theme"]["accent"]
    accent_soft = map_data["theme"]["accent_soft"]

    content = f"""
    <header>
        <div class="nav">
            <a href="/" class="logo">CS2 <span>TACTICAL</span></a>
            <div class="nav-links">
                <a href="/">Главная</a>
                <a href="#grenades">Гранаты</a>
            </div>
        </div>
    </header>

    <div class="container page-wrap" style="--accent:{accent}; --accent_soft:{accent_soft};">
        <div class="page-top">
            <div class="page-top-card">
                <div class="eyebrow">Map Overview</div>
                <h1 class="page-title">{map_data["title"]}</h1>
                <p class="page-subtitle">{map_data["short_text"]}</p>
            </div>
        </div>

        <section id="grenades">
            <div class="section-head">
                <h2>Типы гранат</h2>
                <p>
                    На карте доступны только три основных типа гранат. В каждом разделе находится по два конкретных раскида.
                </p>
            </div>

            <div class="grid-2">
    """

    for grenade_slug, grenade_data in map_data["grenades"].items():
        content += f"""
            <a href="/map/{map_slug}/grenade/{grenade_slug}" class="grenade-link">
                <div class="card grenade-card">
                    <div class="grenade-icon">{grenade_data["icon"]}</div>
                    <h3 class="grenade-title">{grenade_data["title"]}</h3>
                    <p>{grenade_data["purpose"]}</p>
                    <div class="grenade-tag">Открыть раздел →</div>
                </div>
            </a>
        """

    content += """
            </div>

            <div style="margin-top: 32px;">
                <a href="/" class="btn btn-primary">← Назад на главную</a>
            </div>
        </section>
    </div>

    <footer>
        © 2026 CS2 Tactical
    </footer>
    """
    return render_page(content, f'{map_data["title"]} — CS2 Tactical')


@app.route("/map/<map_slug>/grenade/<grenade_slug>")
def grenade_detail(map_slug, grenade_slug):
    map_data = SITE_DATA.get(map_slug)
    if not map_data or map_data.get("in_development"):
        abort(404)

    grenade_data = map_data["grenades"].get(grenade_slug)
    if not grenade_data:
        abort(404)

    accent = map_data["theme"]["accent"]
    accent_soft = map_data["theme"]["accent_soft"]

    lineups_html = ""
    for lineup in grenade_data["lineups"]:
        lineup_slug = slugify_name(lineup["name"])
        preview_html = ""
        if lineup.get("preview_image"):
            preview_html = f'<img src="{lineup["preview_image"]}" alt="{lineup["name"]}" class="lineup-preview">'

        lineups_html += f"""
        <a href="/map/{map_slug}/grenade/{grenade_slug}/lineup/{lineup_slug}" class="lineup-link">
            <div class="lineup-card">
                <div class="side-badge">{lineup["side"]}</div>
                <h3 class="lineup-title">{lineup["name"]}</h3>
                {preview_html}
                <div class="lineup-tag">Открыть раскид →</div>
            </div>
        </a>
        """

    content = f"""
    <header>
        <div class="nav">
            <a href="/" class="logo">CS2 <span>TACTICAL</span></a>
            <div class="nav-links">
                <a href="/">Главная</a>
                <a href="/map/{map_slug}">{map_data["title"]}</a>
            </div>
        </div>
    </header>

    <div class="container page-wrap" style="--accent:{accent}; --accent_soft:{accent_soft};">
        <div class="page-top">
            <div class="page-top-card">
                <div class="eyebrow">{map_data["title"]}</div>
                <h1 class="page-title">{grenade_data["icon"]} {grenade_data["title"]}</h1>
                <p class="page-subtitle">{grenade_data["purpose"]}</p>
            </div>
        </div>

        
        <div class="lineups-box">
            <div class="box-title">Доступные раскиды</div>
            <p>В этом разделе представлены два основных раскида.</p>

            <div class="lineup-grid">
                {lineups_html}
            </div>
        </div>

        <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px;">
            <a href="/map/{map_slug}" class="btn btn-primary">← Назад к карте</a>
            <a href="/" class="btn btn-secondary">На главную</a>
        </div>
    </div>

    <footer>
        © 2026 CS2 Tactical
    </footer>
    """
    return render_page(content, f'{grenade_data["title"]} — {map_data["title"]}')


@app.route("/map/<map_slug>/grenade/<grenade_slug>/lineup/<lineup_slug>")
def lineup_detail(map_slug, grenade_slug, lineup_slug):
    map_data = SITE_DATA.get(map_slug)
    if not map_data or map_data.get("in_development"):
        abort(404)

    grenade_data = map_data["grenades"].get(grenade_slug)
    if not grenade_data:
        abort(404)

    lineup_data = None
    for lineup in grenade_data["lineups"]:
        if slugify_name(lineup["name"]) == lineup_slug:
            lineup_data = lineup
            break

    if not lineup_data:
        abort(404)

    accent = map_data["theme"]["accent"]
    accent_soft = map_data["theme"]["accent_soft"]

    description = lineup_data.get(
        "description",
        f"Это отдельная страница для конкретного раскида {lineup_data['name']} на карте {map_data['title']}."
    )

    videos = lineup_data.get("videos", [])
    benefit = lineup_data.get("benefit", "")

    if videos:
        videos_html = '<div class="video-stack">'
        for video in videos:
            videos_html += f"""
            <div class="video-card">
                <div class="step-badge">{video.get("step", "Шаг")}</div>
                <h3>{video["title"]}</h3>
                <p>{video.get("text", "")}</p>
                <video class="lineup-video" autoplay muted loop playsinline>
                    <source src="{video["file"]}" type="video/mp4">
                </video>
            </div>
            """
        videos_html += "</div>"
    else:
        videos_html = """
        <div class="video-card">
            <div class="step-badge">Скоро</div>
            <h3>Видео будет добавлено позже</h3>
            <p>Для этого раскида пока нет прикреплённого видео.</p>
        </div>
        """

    benefit_html = ""
    if benefit:
        benefit_html = f"""
        <div class="benefit-box">
            <div class="box-title">Плюс данного раскида</div>
            <p>{benefit}</p>
        </div>
        """

    content = f"""
    <header>
        <div class="nav">
            <a href="/" class="logo">CS2 <span>TACTICAL</span></a>
            <div class="nav-links">
                <a href="/">Главная</a>
                <a href="/map/{map_slug}">{map_data["title"]}</a>
                <a href="/map/{map_slug}/grenade/{grenade_slug}">{grenade_data["title"]}</a>
            </div>
        </div>
    </header>

    <div class="container page-wrap" style="--accent:{accent}; --accent_soft:{accent_soft};">
        <div class="page-top">
            <div class="page-top-card">
                <div class="eyebrow">{map_data["title"]} / {grenade_data["title"]}</div>
                <h1 class="page-title">{lineup_data["name"]}</h1>
                <p class="page-subtitle">
                    Сторона: <strong>{lineup_data["side"]}</strong>. На этой странице показан конкретный раскид с пошаговым разбором.
                </p>
            </div>
        </div>

        <div class="purpose-box">
            <div class="box-title">Информация о раскиде</div>
            <p>{description}</p>
        </div>

        <div class="media-box">
            <div class="box-title">Пошаговое выполнение</div>
            <p>
                Ниже показаны два видео данного раскида. Они запускаются автоматически, без звука и без элементов управления.
            </p>
            {videos_html}
        </div>

        {benefit_html}

        <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px;">
            <a href="/map/{map_slug}/grenade/{grenade_slug}" class="btn btn-primary">← Назад к типу гранаты</a>
            <a href="/map/{map_slug}" class="btn btn-secondary">К карте</a>
        </div>
    </div>

    <footer>
        © 2026 CS2 Tactical
    </footer>
    """
    return render_page(content, f'{lineup_data["name"]} — {map_data["title"]}')


if __name__ == "__main__":
    app.run(debug=True)