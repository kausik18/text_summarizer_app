document.getElementById("processBtn").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value;

  const response = await fetch("http://127.0.0.1:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  const data = await response.json();

  document.getElementById("summary").innerText = data.summary;

  const keywordList = document.getElementById("keywords");
  keywordList.innerHTML = "";
  data.keywords.forEach((kw) => {
    const li = document.createElement("li");
    li.textContent = kw;
    keywordList.appendChild(li);
  });
});
