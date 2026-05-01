function ControversyTimeline({ news }) {

  return (
    <div style={{
      marginTop: "40px",
      background: "#1e293b",
      padding: "25px",
      borderRadius: "16px",
    }}>

      <h2 style={{
        color: "white",
        marginBottom: "20px",
        textAlign: "center"
      }}>
        Live ESG News Intelligence
      </h2>

      {news.length === 0 ? (
        <p style={{ color: "#94a3b8", textAlign: "center" }}>
          No news available
        </p>
      ) : (

        news.map((item, index) => (

          <div key={index} style={{
            borderBottom: "1px solid #334155",
            padding: "15px 0"
          }}>

            <a
              href={item.url}
              target="_blank"
              style={{
                color: "#38bdf8",
                fontSize: "18px",
                textDecoration: "none"
              }}
            >
              {item.title}
            </a>

            <p style={{ color: "#94a3b8" }}>
              {item.source}
            </p>

            <span style={{
              color:
                item.severity === "high"
                  ? "#ef4444"
                  : item.severity === "medium"
                  ? "#f59e0b"
                  : "#22c55e"
            }}>
              {item.severity.toUpperCase()}
            </span>

          </div>
        ))
      )}

    </div>
  );
}

export default ControversyTimeline;