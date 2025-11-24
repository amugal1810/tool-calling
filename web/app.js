async function ask() {
  const q = document.getElementById("q").value;
  const res = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ question: q })
  });
  const data = await res.json();
  document.getElementById("output").textContent = data.answer;
}