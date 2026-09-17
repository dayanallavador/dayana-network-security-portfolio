from pathlib import Path

maintenance_page = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Dayana Llavador — portfolio temporarily under maintenance" />
  <title>Maintenance — Dayana Llavador</title>
  <style>
    :root{
      --bg:#08131f;
      --surface:#0f1b2b;
      --text:#f4f7fb;
      --muted:#aab7c9;
      --line:rgba(255,255,255,.12);
      --blue:#5c7cff;
    }
    *{box-sizing:border-box}
    html,body{margin:0;min-height:100%;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
    body{
      min-height:100vh;
      display:grid;
      place-items:center;
      padding:24px;
      color:var(--text);
      background:
        radial-gradient(circle at 75% 30%,rgba(47,109,246,.18),transparent 28%),
        linear-gradient(180deg,#0d1d30,var(--bg));
    }
    main{
      width:min(680px,100%);
      padding:42px;
      border:1px solid var(--line);
      border-radius:14px;
      background:rgba(15,27,43,.72);
      box-shadow:0 24px 70px rgba(0,0,0,.28);
      backdrop-filter:blur(14px);
    }
    .eyebrow{
      display:block;
      margin-bottom:16px;
      color:#aebee0;
      font-size:12px;
      font-weight:800;
      letter-spacing:.14em;
    }
    h1{
      margin:0 0 16px;
      font-size:clamp(38px,8vw,64px);
      line-height:1;
      letter-spacing:-.045em;
    }
    p{
      margin:0;
      max-width:560px;
      color:var(--muted);
      font-size:17px;
      line-height:1.65;
    }
    .status{
      display:inline-flex;
      align-items:center;
      gap:8px;
      margin-top:28px;
      padding:9px 12px;
      border:1px solid var(--line);
      border-radius:999px;
      color:#dce5f2;
      font-size:13px;
    }
    .dot{
      width:8px;
      height:8px;
      border-radius:50%;
      background:var(--blue);
      box-shadow:0 0 0 5px rgba(92,124,255,.12);
    }
    @media(max-width:640px){
      main{padding:30px 24px}
      p{font-size:16px}
    }
  </style>
</head>
<body>
  <main>
    <span class="eyebrow">DAYANA LLAVADOR · NETWORK SECURITY</span>
    <h1>Website under maintenance.</h1>
    <p>I'm making some updates to the portfolio. It will be back online soon.</p>
    <div class="status"><span class="dot"></span> Maintenance in progress</div>
  </main>
</body>
</html>
'''

Path("index.html").write_text(maintenance_page, encoding="utf-8")
