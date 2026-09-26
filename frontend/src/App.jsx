import { useState } from "react";

function App() {

  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  async function handleSearch() {

    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: query
      })
    });

    const data = await response.json();

    setAnswer(data.answer);
  }

  return (
    <div>
      <h1>Semantic Video Search</h1>

      <input
        type="text"
        placeholder="Ask something about the video..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSearch}>
        Search
      </button>

      {answer && (
        <div>
          <h2>Answer</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;