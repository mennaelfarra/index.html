<button id="chatToggle" style="
position: fixed;
bottom: 20px;
right: 20px;
background: #2563eb;
color: white;
border-radius: 999px;
padding: 14px;
border:none;
cursor:pointer;
z-index:9999;
">💬</button>

<div id="chatBox" style="
display:none;
position:fixed;
bottom:80px;
right:20px;
width:300px;
background:white;
border-radius:12px;
box-shadow:0 0 20px rgba(0,0,0,0.3);
z-index:9999;
">
<div style="padding:10px;background:#2563eb;color:white;">
AI Chat
</div>

<div id="messages" style="height:250px;overflow:auto;padding:10px;"></div>

<input id="input" style="width:70%;padding:10px;">
<button onclick="send()">Send</button>
</div>

<script>
const box = document.getElementById("chatBox");

document.getElementById("chatToggle").onclick = () => {
  box.style.display = box.style.display === "none" ? "block" : "none";
};

async function send() {
  const input = document.getElementById("input");
  const msg = input.value;

  document.getElementById("messages").innerHTML += "<div>👤 " + msg + "</div>";

  const res = await fetch("/api/chat", {
    method: "POST",
    body: JSON.stringify({ message: msg })
  });

  const data = await res.json();

  document.getElementById("messages").innerHTML += "<div>🤖 " + data.reply + "</div>";
  input.value = "";
}
</script>