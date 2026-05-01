function EvidenceViewer({ quotes }) {

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
          color: "white",
          marginBottom: "20px",
          textAlign: "center",
        }}
      >
        ESG Evidence
      </h2>

      {quotes.length === 0 ? (
        <p
          style={{
            color: "#94a3b8",
            textAlign: "center",
          }}
        >
          No relevant evidence found
        </p>
      ) : (
        quotes.map((q, i) => (
          <div
            key={i}
            style={{
              borderBottom: "1px solid #334155",
              padding: "12px",
              color: "#e2e8f0",
            }}
          >
            {q}
          </div>
        ))
      )}

    </div>
  );
}

export default EvidenceViewer;