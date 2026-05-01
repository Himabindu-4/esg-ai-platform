import React from "react";

function ESGTrendChart({ trendData }) {

  // ✅ HANDLE EMPTY DATA
  if (!trendData || trendData.length === 0) {
    return (
      <div style={{
        marginTop: "50px",
        background: "#1e293b",
        padding: "40px",
        borderRadius: "16px",
        textAlign: "center",
        color: "#94a3b8",
        fontSize: "18px"
      }}>
        No ESG trend data available
      </div>
    );
  }

  return (
    <div style={{
      marginTop: "50px",
      background: "#1e293b",
      padding: "30px",
      borderRadius: "16px"
    }}>

      <h2 style={{
        textAlign: "center",
        marginBottom: "20px"
      }}>
        ESG Trend Over 5 Years
      </h2>

      {/* SIMPLE TABLE VIEW */}
      <table style={{
        width: "100%",
        color: "white",
        borderCollapse: "collapse"
      }}>

        <thead>
          <tr>
            <th>Year</th>
            <th>Env</th>
            <th>Soc</th>
            <th>Gov</th>
            <th>Total</th>
          </tr>
        </thead>

        <tbody>
          {trendData.map((item, index) => (
            <tr key={index} style={{ textAlign: "center" }}>
              <td>{item.year}</td>
              <td>{item.environmental}</td>
              <td>{item.social}</td>
              <td>{item.governance}</td>
              <td>{item.total}</td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}

export default ESGTrendChart;