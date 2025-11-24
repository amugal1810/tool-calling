async function ask() {
    const q = document.getElementById("q").value;
    const output = document.getElementById("output");
    const loader = document.getElementById("loader");

    loader.style.display = "block";
    output.textContent = "";

    const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: q })
    });

    const data = await res.json();
    loader.style.display = "none";
    output.textContent = data.answer;
}