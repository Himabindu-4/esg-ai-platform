import { useState } from "react";
import API from "../services/api";

function ESGScreener() {

  const [minESG, setMinESG] = useState(0);
  const [minEnv, setMinEnv] = useState(0);
  const [minSoc, setMinSoc] = useState(0);
  const [minGov, setMinGov] = useState(0);

  const [results, setResults] = useState([]);


  const runScreener = async () => {

    try {

      const res = await API.get("/screener", {
        params: {
          min_esg: minESG,
          min_env: minEnv,
          min_soc: minSoc,
          min_gov: minGov
        }
      });

      setResults(res.data);

    } catch (err) {
      console.error(err);
    }
  };


  return (
    <div style={{
      marginTop: "50px",
      background: "#1e293b",
      padding: "25px",
      borderRadius: "16px"
    }}>

      <h2 style={{ color: "white", textAlign: "center" }}>
        ESG Screener
      </h2>

      <div style={{
        display: "flex",
        gap: "10px",
        justifyContent: "center",
        marginTop: "20px",
        flexWrap: "wrap"
      }}>

        <input
          type="number"
          placeholder="Min ESG"
          value={minESG}
          onChange={(e) => setMinESG(e.target.value)}
        />

        <input
          type="number"
          placeholder="Min Env"
          value={minEnv}
          onChange={(e) => setMinEnv(e.target.value)}
        />

        <input
          type="number"
          placeholder="Min Social"
          value={minSoc}
          onChange={(e) => setMinSoc(e.target.value)}
        />

        <input
          type="number"
          placeholder="Min Governance"
          value={minGov}
          onChange={(e) => setMinGov(e.target.value)}
        />

        <button onClick={runScreener}>
          Filter
        </button>

      </div>


      {/* RESULTS */}
      <div style={{ marginTop: "30px" }}>

        {results.length === 0 ? (
          <p style={{ color: "#94a3b8", textAlign: "center" }}>
            No results found
          </p>
        ) : (

          results.map((c, i) => (
            <div key={i} style={{
              padding: "10px",
              borderBottom: "1px solid #334155",
              color: "white"
            }}>
              {c.ticker} | ESG: {c.total}
            </div>
          ))
        )}

      </div>

    </div>
  );
}

export default ESGScreener;