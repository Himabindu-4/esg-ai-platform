function GreenwashingPanel({ flags }) {

  return (

    <div
      style={{
        background: "#1e293b",
        padding: "20px",
        borderRadius: "12px",
        marginTop: "40px",
      }}
    >

      <h2
        style={{
          color: "white",
          marginBottom: "20px",
        }}
      >
        Greenwashing Risk Signals
      </h2>


      {flags.length === 0 ? (

        <p
          style={{
            color: "#94a3b8",
          }}
        >
          No major greenwashing signals detected.
        </p>

      ) : (

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "15px",
          }}
        >

          {flags.map((flag, index) => (

            <div
              key={index}
              style={{
                background: "#0f172a",
                padding: "15px",
                borderRadius: "10px",
                borderLeft: "4px solid #ef4444",
              }}
            >

              <h3
                style={{
                  color: "#ef4444",
                  marginBottom: "10px",
                }}
              >
                Risk Signal
              </h3>

              <p
                style={{
                  color: "#e2e8f0",
                  lineHeight: "1.6",
                }}
              >
                {typeof flag === "string"
                  ? flag
                  : JSON.stringify(flag)}
              </p>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default GreenwashingPanel;