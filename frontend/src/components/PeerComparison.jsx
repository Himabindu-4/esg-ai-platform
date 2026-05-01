import { useEffect, useState } from "react";

import API from "../services/api";

function PeerComparison() {

  const [companies, setCompanies] = useState([]);

  useEffect(() => {

    API.get("/peer-comparison")
      .then((res) => {

        console.log(res.data);

        setCompanies(res.data);

      })
      .catch((err) => console.error(err));

  }, []);


  return (

    <div
      style={{
        marginTop: "40px",
        background: "#1e293b",
        padding: "25px",
        borderRadius: "16px",
      }}
    >

      <h2
        style={{
          marginBottom: "25px",
          color: "white",
          textAlign: "center",
          fontSize: "30px",
        }}
      >
        Peer ESG Comparison
      </h2>


      <div
        style={{
          overflowX: "auto",
        }}
      >

        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
            color: "white",
            minWidth: "700px",
          }}
        >

          <thead>

            <tr
              style={{
                background: "#0f172a",
              }}
            >

              <th style={tableHeader}>Ticker</th>
              <th style={tableHeader}>Environmental</th>
              <th style={tableHeader}>Social</th>
              <th style={tableHeader}>Governance</th>
              <th style={tableHeader}>Total ESG</th>

            </tr>

          </thead>


          <tbody>

            {companies.length > 0 ? (

              companies.map((company, index) => (

                <tr
                  key={index}
                  style={{
                    textAlign: "center",
                    borderBottom: "1px solid #334155",
                  }}
                >

                  <td style={tableCell}>
                    {company.ticker}
                  </td>

                  <td style={tableCell}>
                    {company.environmental}
                  </td>

                  <td style={tableCell}>
                    {company.social}
                  </td>

                  <td style={tableCell}>
                    {company.governance}
                  </td>

                  <td
                    style={{
                      ...tableCell,
                      color: "#38bdf8",
                      fontWeight: "bold",
                    }}
                  >
                    {company.total}
                  </td>

                </tr>
              ))

            ) : (

              <tr>

                <td
                  colSpan="5"
                  style={{
                    padding: "40px",
                    textAlign: "center",
                    color: "#94a3b8",
                  }}
                >
                  No peer comparison data found.
                </td>

              </tr>
            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}


const tableHeader = {
  padding: "18px",
  fontSize: "18px",
  color: "#38bdf8",
};


const tableCell = {
  padding: "16px",
  fontSize: "17px",
};


export default PeerComparison;