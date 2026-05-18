(function(){
  const widget = document.createElement('div');
  widget.innerHTML = `
    <div id="amandarina-chat-btn" style="position:fixed;bottom:20px;right:20px;background:#ff6b35;color:white;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:9999;font-size:24px;box-shadow:0 4px 12px rgba(0,0,0,0.2);">💬</div>
    <div id="amandarina-chat-box" style="position:fixed;bottom:90px;right:20px;width:340px;height:450px;background:white;border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,0.15);display:none;flex-direction:column;z-index:9999;overflow:hidden;">
      <div style="padding:14px;background:linear-gradient(135deg,#ff6b35,#f7931e);color:white;font-weight:600;">🤖 Amandarina AI</div>
      <div id="amandarina-chat-log" style="flex:1;overflow-y:auto;padding:14px;font-size:14px;line-height:1.5;"></div>
      <div style="padding:12px;border-top:1px solid #eee;display:flex;gap:8px;">
        <input id="amandarina-chat-input" style="flex:1;padding:10px;border:1px solid #ddd;border-radius:8px;outline:none;font-size:14px;" placeholder="¿En qué te ayudo?">
        <button id="amandarina-chat-send" style="padding:10px 16px;background:#ff6b35;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:600;">Enviar</button>
      </div>
    </div>
  `;
  document.body.appendChild(widget);

  const btn = document.getElementById('amandarina-chat-btn');
  const box = document.getElementById('amandarina-chat-box');
  const log = document.getElementById('amandarina-chat-log');
  const input = document.getElementById('amandarina-chat-input');
  const send = document.getElementById('amandarina-chat-send');

  btn.onclick = () => box.style.display = box.style.display === 'none'? 'flex' : 'none';

  async function sendMessage(){
    const msg = input.value.trim();
    if(!msg) return;
    
    // Mostrar mensaje del usuario
    log.innerHTML += `<div style="margin:10px 0;text-align:right;"><div style="display:inline-block;background:#f1f1f1;padding:8px 12px;border-radius:12px;">${msg}</div></div>`;
    input.value = '';

    // Mostrar indicador de escritura
    log.innerHTML += `<div id="typing" style="margin:10px 0;color:#888;">✍️ Escribiendo...</div>`;
    log.scrollTop = log.scrollHeight;

    try{
      // CAMBIAR ESTA URL POR LA DE RENDER
      const res = await fetch('https://TU-APP-RENDER.onrender.com/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text: msg})
      });
      const data = await res.json();
      document.getElementById('typing').remove();
      log.innerHTML += `<div style="margin:10px 0;"><div style="display:inline-block;background:#ff6b35;color:white;padding:8px 12px;border-radius:12px;">${data.reply}</div></div>`;
      log.scrollTop = log.scrollHeight;
    }catch(e){
      document.getElementById('typing').remove();
      log.innerHTML += `<div style="margin:10px 0;color:red;">❌ Error. Intenta de nuevo.</div>`;
    }
  }

  send.onclick = sendMessage;
  input.addEventListener('keypress', e => {if(e.key==='Enter') sendMessage()});
})();