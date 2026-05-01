import { useState } from "react";
import API from "../services/api";

function PortfolioAnalyzer() {

  const [result, setResult] = useState(null);
  const [file, setFile] = useState(null);


  // =========================
  // FILE SELECT
  // =========================
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };


  // =========================
  // UPLOAD CSV
  // =========================
  const uploadCSV = async () => {

    if (!file) {
      alert("Please upload a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      const res = await API.post("/portfolio/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });

      // ✅ UPDATED (NEW API FORMAT SUPPORT)
      if (res.data?.status === "error") {
        alert(res.data.message);
        return;
      }

      setResult(res.data?.data || res.data);

    } catch (err) {
      console.error(err);
      alert("Error processing portfolio");
    }
  };


  return (
    <div style={{
      marginTop: "50px",
      background: "#1e293b",
      padding: "25px",
      borderRadius: "16px",
      textAlign: "center"
    }}>

      <h2>Portfolio ESG Analyzer (CSV Upload)</h2>


      {/* FILE INPUT */}
      <input
        type="file"
        accept=".csv"
        onChange={handleFileChange}
        style={{ marginTop: "15px" }}
      />


      <br />

      <button
        onClick={uploadCSV}
        style={{
          marginTop: "15px",
          padding: "10px 20px",
          background: "#38bdf8",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          fontWeight: "bold"
        }}
      >
        Upload & Calculate
      </button>


      {/* RESULT */}
      {result && (
        <div style={{
          marginTop: "20px",
          background: "#020617",
          padding: "20px",
          borderRadius: "12px"
        }}>
          <p>Environmental: {result.environmental}</p>
          <p>Social: {result.social}</p>
          <p>Governance: {result.governance}</p>
          <h3>Total ESG: {result.total}</h3>
        </div>
      )}

    </div>
  );
}

export default PortfolioAnalyzer;